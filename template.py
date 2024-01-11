import os
import sys 
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

#specify the project name 
project_name = "text_summarizer"

#specify list of files

#CI/CD deployment we need this .github file
# empty folder cannot be created so we kept .gitkeep
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    "notebook/trials.ipynb"
]

for filepath in list_of_files:
     # converting into the operating system's path which is mac's path
    filepath = Path(filepath)

    # convert it into head and tail (folder and file)
    file_dir, filename = os.path.split(filepath) 

    if file_dir != "":
        os.makedirs(file_dir, exist_ok = True)
        logging.info(f"Creating Directory")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'wb') as file:
            pass
            logging.info(f"Creating empty file path {filepath}")
    else:
        logging.info(f"{filename} already exists")

