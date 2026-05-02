import sys 
import os 
from src.logger import logging 
from src.exception import CustomException
import numpy as np 
import pickle
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
import numpy as np

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)


    except Exception as e:
        logging.info('Exception Occured in Save Object Function')
        raise CustomException(e,sys)