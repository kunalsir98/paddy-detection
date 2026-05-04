import sys 
import os 
from src.logger import logging 
from src.exception import CustomException
from src.utils import save_object 
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer 
from dataclasses import dataclass
import numpy as np 
import pandas as pd 
from sklearn.impute import SimpleImputer
from src.utils import save_object
@dataclass 
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformation_object(self):
        try:
            logging.info('Data Transformation initiated')

            numerical_cols=['Hectares ', 'Seedrate(in Kg)', 'LP_Mainfield(in Tonnes)',
       'Nursery area (Cents)', 'LP_nurseryarea(in Tonnes)', 'DAP_20days',
       'Weed28D_thiobencarb', 'Urea_40Days', 'Potassh_50Days',
       'Micronutrients_70Days', 'Pest_60Day(in ml)', '30DRain( in mm)',
       '30DAI(in mm)', '30_50DRain( in mm)', '30_50DAI(in mm)',
       '51_70DRain(in mm)', '51_70AI(in mm)', '71_105DRain(in mm)',
       '71_105DAI(in mm)', 'Min temp_D1_D30', 'Max temp_D1_D30',
       'Min temp_D31_D60', 'Max temp_D31_D60', 'Min temp_D61_D90',
       'Max temp_D61_D90', 'Min temp_D91_D120', 'Max temp_D91_D120',
       'Inst Wind Speed_D1_D30(in Knots)', 'Inst Wind Speed_D31_D60(in Knots)',
       'Inst Wind Speed_D61_D90(in Knots)',
       'Inst Wind Speed_D91_D120(in Knots)', 'Relative Humidity_D1_D30',
       'Relative Humidity_D31_D60', 'Relative Humidity_D61_D90',
       'Relative Humidity_D91_D120', 'Trash(in bundles)']
            categorical_cols=['Agriblock', 'Variety', 'Soil Types', 'Nursery',
       'Wind Direction_D1_D30', 'Wind Direction_D31_D60',
       'Wind Direction_D61_D90', 'Wind Direction_D91_D120']
            
            #creting preproceessor pipeline 
            num_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler())
                ]
            )
            cat_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('one_hot_encoder',OneHotEncoder(handle_unknown='ignore')),
                    ('scaler',StandardScaler(with_mean=False))
                ]
            )
            preprocessor=ColumnTransformer([
                ('num_pipeline',num_pipeline,numerical_cols),
                ('cat_pipeline',cat_pipeline,categorical_cols)
            ])

            logging.info('pipeline completed')

            return preprocessor
          

        except Exception as e:
            logging.info('Exception occured in Data Transformation Stage')
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
         try:
             logging.info('Reading Train and Test Data')
             train_df=pd.read_csv(train_path)
             test_df=pd.read_csv(test_path)

             logging.info(f'getting columns for train and test data')
             logging.info(f'Train Dataframe Head: \n :{train_df.head().to_string()}')
             logging.info(f'Test Dataframe Head: \n :{test_df.head().to_string()}')

             target_column_name='Paddy yield(in Kg)'
             drop_columns=[target_column_name]

             input_feature_train_df=train_df.drop(columns=drop_columns)
             target_feature_train_df=train_df[target_column_name]

             input_feature_test_df=test_df.drop(columns=drop_columns)
             target_feature_test_df=test_df[target_column_name]

             logging.info('Obtainig preprocessing Object')

             preprocessing_obj=self.get_data_transformation_object()

             input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
             input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

             logging.info('Applying preprocessor object on train arr and test arr')

             train_arr=np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
             test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

             save_object(
                 self.data_transformation_config.preprocessor_obj_file_path,obj=preprocessing_obj
             )

             logging.info('Saving preprocessor file')


             return(
                 train_arr,
                 test_arr,
                 self.data_transformation_config.preprocessor_obj_file_path 
             )

         except Exception as e:
             logging.info('Exception Occured at Initiate Data Transformtion')
             raise CustomException(e,sys)
