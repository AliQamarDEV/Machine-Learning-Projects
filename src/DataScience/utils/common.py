import os 
import yaml 
from src.DataScience.utils.logger import logger 
import json 
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError
import joblib

@ensure_annotations
def read_yaml_file(path_to_yaml : Path) -> ConfigBox :
    ''' 
    Read yaml file and returns a cofing box 

    Args : 
        path to yaml file 
    except :
        if the yaml file is empty 
        or any other error 
    Returns 
    a config box 
    '''

    try : 
        with open(path_to_yaml) as yaml_file : 
            yaml_file = yaml.safe_load(yaml_file)
            logger.info('Loaded A Yaml File.')
            return ConfigBox(yaml_file)
    except BoxValueError : 
        raise ValueError(f'Yaml File Is Empty')
    except Exception as e : 
        raise e 
    
@ensure_annotations 
def create_directories(path_to_directory : list ,verbose=True) : 
    """
    Creating a list of dictionary 
    making logging history 
    Args : 
        path of a dictionay 

    """
    for path in path_to_directory : 
        os.makedirs(path,exist_ok=True)
        if verbose : 
            logger.info(f'Maked Dictionary at {path}')

@ensure_annotations 
def save_json (path : Path , data:dict):
    '''
    save json data 
    Args : 
        path(path to json file)
        data(dict to be saved in json file)'''
    
    with open(path,'w') as f : 
        json.dump(data,f,indent=4)

@ensure_annotations 
def load_json_file(path : Path)-> ConfigBox: 
    '''
    returns data as a class attributes instead of a dictionary 
    '''
    with open(path) as f : 
        data = json.load(f)
    logger.info(f'Json file loaded sucesfully from {path}')
    return ConfigBox(data)

@ensure_annotations
def save_bin(data:Any,path : Path) : 
    '''
    input : 
    data -> to save 
    path -> location to save 
    '''
    joblib.dump(value=data,filename=path)
    logger.info('Saved Bin File')

@ensure_annotations
def Load_Bin(path:Path) -> Any : 
    '''
    Load Binary Data
    Return 
        any format in the file 

    '''
    data = joblib.load(path)
    logger.info('Loaded Bin File')
    return data