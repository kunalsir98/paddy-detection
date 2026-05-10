import sys 
import os 
from src.logger import logging
from src.exception import CustomException
from src.utils import load_object
import pandas as pd 

class Predictpipeline:
    def __init__(self):
        pass 

    def predict(self,feautures):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(feautures)

            pred=model.predict(data_scaled)
            return pred 
        

        except Exception as e:
            logging.info('Exception Occured at prediction pipeline')
            raise CustomException(e,sys)

class CustomData:
    def __init__(
        self,
        hectares: float,
        agriblock: str,
        variety: str,
        soil_types: str,
        seedrate_in_kg: float,
        lp_mainfield_in_tonnes: float,
        nursery: str,
        nursery_area_cents: float,
        lp_nurseryarea_in_tonnes: float,
        dap_20days: float,
        weed28d_thiobencarb: float,
        urea_40days: float,
        potassh_50days: float,
        micronutrients_70days: float,
        pest_60day_in_ml: float,
        rain_30d_mm: float,
        ai_30d_mm: float,
        rain_30_50d_mm: float,
        ai_30_50d_mm: float,
        rain_51_70d_mm: float,
        ai_51_70d_mm: float,
        rain_71_105d_mm: float,
        ai_71_105d_mm: float,
        min_temp_d1_d30: float,
        max_temp_d1_d30: float,
        min_temp_d31_d60: float,
        max_temp_d31_d60: float,
        min_temp_d61_d90: float,
        max_temp_d61_d90: float,
        min_temp_d91_d120: float,
        max_temp_d91_d120: float,
        wind_speed_d1_d30: float,
        wind_speed_d31_d60: float,
        wind_speed_d61_d90: float,
        wind_speed_d91_d120: float,
        wind_direction_d1_d30: str,
        wind_direction_d31_d60: str,
        wind_direction_d61_d90: str,
        wind_direction_d91_d120: str,
        humidity_d1_d30: float,
        humidity_d31_d60: float,
        humidity_d61_d90: float,
        humidity_d91_d120: float,
        trash_in_bundles: float
    ):

        self.hectares = hectares
        self.agriblock = agriblock
        self.variety = variety
        self.soil_types = soil_types
        self.seedrate_in_kg = seedrate_in_kg
        self.lp_mainfield_in_tonnes = lp_mainfield_in_tonnes
        self.nursery = nursery
        self.nursery_area_cents = nursery_area_cents
        self.lp_nurseryarea_in_tonnes = lp_nurseryarea_in_tonnes
        self.dap_20days = dap_20days
        self.weed28d_thiobencarb = weed28d_thiobencarb
        self.urea_40days = urea_40days
        self.potassh_50days = potassh_50days
        self.micronutrients_70days = micronutrients_70days
        self.pest_60day_in_ml = pest_60day_in_ml
        self.rain_30d_mm = rain_30d_mm
        self.ai_30d_mm = ai_30d_mm
        self.rain_30_50d_mm = rain_30_50d_mm
        self.ai_30_50d_mm = ai_30_50d_mm
        self.rain_51_70d_mm = rain_51_70d_mm
        self.ai_51_70d_mm = ai_51_70d_mm
        self.rain_71_105d_mm = rain_71_105d_mm
        self.ai_71_105d_mm = ai_71_105d_mm
        self.min_temp_d1_d30 = min_temp_d1_d30
        self.max_temp_d1_d30 = max_temp_d1_d30
        self.min_temp_d31_d60 = min_temp_d31_d60
        self.max_temp_d31_d60 = max_temp_d31_d60
        self.min_temp_d61_d90 = min_temp_d61_d90
        self.max_temp_d61_d90 = max_temp_d61_d90
        self.min_temp_d91_d120 = min_temp_d91_d120
        self.max_temp_d91_d120 = max_temp_d91_d120
        self.wind_speed_d1_d30 = wind_speed_d1_d30
        self.wind_speed_d31_d60 = wind_speed_d31_d60
        self.wind_speed_d61_d90 = wind_speed_d61_d90
        self.wind_speed_d91_d120 = wind_speed_d91_d120
        self.wind_direction_d1_d30 = wind_direction_d1_d30
        self.wind_direction_d31_d60 = wind_direction_d31_d60
        self.wind_direction_d61_d90 = wind_direction_d61_d90
        self.wind_direction_d91_d120 = wind_direction_d91_d120
        self.humidity_d1_d30 = humidity_d1_d30
        self.humidity_d31_d60 = humidity_d31_d60
        self.humidity_d61_d90 = humidity_d61_d90
        self.humidity_d91_d120 = humidity_d91_d120
        self.trash_in_bundles = trash_in_bundles


    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
            "Hectares ": [self.hectares],
            "Agriblock": [self.agriblock],
            "Variety": [self.variety],
            "Soil Types": [self.soil_types],
            "Seedrate(in Kg)": [self.seedrate_in_kg],
            "LP_Mainfield(in Tonnes)": [self.lp_mainfield_in_tonnes],
            "Nursery": [self.nursery],
            "Nursery area (Cents)": [self.nursery_area_cents],
            "LP_nurseryarea(in Tonnes)": [self.lp_nurseryarea_in_tonnes],
            "DAP_20days": [self.dap_20days],
            "Weed28D_thiobencarb": [self.weed28d_thiobencarb],
            "Urea_40Days": [self.urea_40days],
            "Potassh_50Days": [self.potassh_50days],
            "Micronutrients_70Days": [self.micronutrients_70days],
            "Pest_60Day(in ml)": [self.pest_60day_in_ml],
            "30DRain( in mm)": [self.rain_30d_mm],
            "30DAI(in mm)": [self.ai_30d_mm],
            "30_50DRain( in mm)": [self.rain_30_50d_mm],
            "30_50DAI(in mm)": [self.ai_30_50d_mm],
            "51_70DRain(in mm)": [self.rain_51_70d_mm],
            "51_70AI(in mm)": [self.ai_51_70d_mm],
            "71_105DRain(in mm)": [self.rain_71_105d_mm],
            "71_105DAI(in mm)": [self.ai_71_105d_mm],
            "Min temp_D1_D30": [self.min_temp_d1_d30],
            "Max temp_D1_D30": [self.max_temp_d1_d30],
            "Min temp_D31_D60": [self.min_temp_d31_d60],
            "Max temp_D31_D60": [self.max_temp_d31_d60],
            "Min temp_D61_D90": [self.min_temp_d61_d90],
            "Max temp_D61_D90": [self.max_temp_d61_d90],
            "Min temp_D91_D120": [self.min_temp_d91_d120],
            "Max temp_D91_D120": [self.max_temp_d91_d120],
            "Inst Wind Speed_D1_D30(in Knots)": [self.wind_speed_d1_d30],
            "Inst Wind Speed_D31_D60(in Knots)": [self.wind_speed_d31_d60],
            "Inst Wind Speed_D61_D90(in Knots)": [self.wind_speed_d61_d90],
            "Inst Wind Speed_D91_D120(in Knots)": [self.wind_speed_d91_d120],
            "Wind Direction_D1_D30": [self.wind_direction_d1_d30],
            "Wind Direction_D31_D60": [self.wind_direction_d31_d60],
            "Wind Direction_D61_D90": [self.wind_direction_d61_d90],
            "Wind Direction_D91_D120": [self.wind_direction_d91_d120],
            "Relative Humidity_D1_D30": [self.humidity_d1_d30],
            "Relative Humidity_D31_D60": [self.humidity_d31_d60],
            "Relative Humidity_D61_D90": [self.humidity_d61_d90],
            "Relative Humidity_D91_D120": [self.humidity_d91_d120],
            "Trash(in bundles)": [self.trash_in_bundles]
        }
            
            df=pd.DataFrame(custom_data_input_dict)
            logging.info('reading as pandas Dataframe')
            return df
        except Exception as e:
            logging.info('Exception Occured at get data frame')
            raise CustomException(e,sys)

