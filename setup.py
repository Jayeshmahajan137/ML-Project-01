from setuptools import setup
from typing import List

def get_requirements_list()->List[str]:
    """
    Description- this function is going to return list 
    of requirements mentioned in requirements.txt file

    Return - this function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

PROJECT_NAME="housing_predictor"
VERSION= "0.0.1"
AUTHOR="Jayesh"
DESCRIPTION= "First major project of machine learning "
PACKAGES= ["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()

)