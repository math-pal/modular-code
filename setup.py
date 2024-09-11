from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "FYP CHATBOT"
VERSION = "0.0.1"
DESCRIPTION = "Final Year Project to create an AI-based chatbot to be integrated into a website"
AUTHOR_NAME = "Arshad Hussain"
AUTHOR_EMAIL = "dummy@abc.com"

REQUIREMENTS_FILE = "requirements.txt"
HYPHEN_E_DOT = "-e ."

# requirements.txt file open
def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE) as req_file:
        req_list = req_file.readlines()
        req_list = [req_name.replace("\n", "") for req_name in req_list]

        if HYPHEN_E_DOT in req_list:
            req_list.remove(HYPHEN_E_DOT)

    return  req_list

setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
    #   url='https://www.python.org/sigs/distutils-sig/',
      packages=find_packages(),
      install_reuires = get_requirements_list()
     )