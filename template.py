# Import libraries
import os, sys
from pathlib import Path
import logging

# Create files
while True:
    directory_name = input('Enter your directory name: ')
    if directory_name != "":
        break

# src/__init__.py
# src/components.py
list_of_files = [
    f"{directory_name}/__init__.py",
    f"{directory_name}/components/__init__.py",
    f"{directory_name}/config/__init__.py",
    f"{directory_name}/constants/__init__.py",
    f"{directory_name}/entity/__init__.py",
    f"{directory_name}/exception/__init__.py",
    f"{directory_name}/logger/__init__.py",
    f"{directory_name}/pipeline/__init__.py",
    f"{directory_name}/utils/__init__.py",
    f"config/config.yaml",
    "shema.yaml",
    "app.py",
    "main.py",
    "logs.py",
    "exception.py",
    # "setup.py"
]

for fp in list_of_files:
    filepath = Path(fp)
    filedir, filename = os.path.split(filepath)  # to split in different directories

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass

    else:
        logging.info("File already exists at: {filepath}")
