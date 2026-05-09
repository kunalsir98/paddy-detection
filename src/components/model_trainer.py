import sys 
import os 
from src.logger import logging 
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor,AdaBoostRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from sklearn.svm import SVR
from src.utils import evaluate_models,save_object
@dataclass 
class ModelTrainerConfig:
    model_trainer_file_path=os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    
    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info('Intiating train test Split')

            X_train, X_test, y_train, y_test = (
                train_array[:, :-1],
                test_array[:, :-1],
                train_array[:, -1],
                test_array[:, -1]
            )

            models={
                'RandomForestRegressor':RandomForestRegressor(),
                'DecissionTreeRegressor':DecisionTreeRegressor(),
                "GradientBoodst":GradientBoostingRegressor(),
                "LinearRegression":LinearRegression(),
                "KneighbourRegressor":KNeighborsRegressor(),
                "XGBRegressor":XGBRegressor(),
                "CatboostRegressor":CatBoostRegressor(),
                "SVM":SVR(),
                "AdaBoostRegressor":AdaBoostRegressor(),

            }
            model_report:dict=evaluate_models(X_train,y_train,X_test,y_test,models)
            print(model_report)
            print('==================')
            logging.info('Model Report : {model_report}') 

            best_model_score=max(sorted(model_report.values()))

            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model=models[best_model_name]

            print(f"Best Model Selection, Model Name:{best_model_name} Model Score:{best_model_score}")
            print('\n======================')
            logging.info(f"Best Model Selection, Model Name:{best_model_name} Model Score:{best_model_score}")


            save_object(
                self.model_trainer_config.model_trainer_file_path,
                obj=best_model
            )

        except Exception as e:
            logging.info('Exception Occured at Model Trainer stage')
            raise CustomException(e,sys)

