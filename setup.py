from setuptools import setup
from typing import List

def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()
   
    
# Declaring variables for setup function

PROJECT_NAME="Housing_predictor"
AUTHOR= "Jayesh"
VERSION="0.0.1"
DESCRIPTION="This is first major project in machine learning"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"


setup(
project_name=PROJECT_NAME,
author=AUTHOR,
version=VERSION,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()

)