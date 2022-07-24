from setuptools import setup,find_packages
from typing import List

def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")
   
    
# Declaring variables for setup function

PROJECT_NAME="housing_predictor"
AUTHOR= "Jayesh"
VERSION="0.0.4"
DESCRIPTION="This is first major project in machine learning"

REQUIREMENT_FILE_NAME="requirements.txt"


setup(
project_name=PROJECT_NAME,
author=AUTHOR,
version=VERSION,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()
)