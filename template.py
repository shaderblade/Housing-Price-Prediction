import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    '.github/workflows/.gitkeep',
    'data/.gitkeep',
    'model/.gitkeep',
    'src/app/__init__.py',
    'src/app/utils/common.py',
    'requirements.txt',
    'notebooks/trials.ipynb',
    'templates/index.html',
    'static/css/index.css',
    'static/js/index.js',
    'static/images/.gitkeep'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f'{filename} already exists')