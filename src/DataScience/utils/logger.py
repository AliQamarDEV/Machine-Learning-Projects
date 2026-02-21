import os # for making files / dir
import sys # for printing logs in terminal 
import logging # for making logs 

logging_format = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]" 

log_dir = 'logs'
file_path = os.path.join(log_dir,'logging.log')
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_format,
    handlers=[
        logging.FileHandler(file_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('Data_Science_Logger')