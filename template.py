from src.DataScience.utils.logger import logger
import os 

project_name = 'DataScience'

files_list = [".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/data_ingestion_pipeline.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
    "templates/results.html",
    "app.py",]

for i in files_list : 
    if '.' not in os.path.basename(i) : 
        os.makedirs(i,exist_ok=True)
    else : 
        os.makedirs(os.path.dirname(i),exist_ok=True)
        with open(i,'w') as f : 
            pass

logger.info('Files/Folder Created')