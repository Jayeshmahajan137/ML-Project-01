
from setuptools import setup,find_packages
import os
from typing import List

def get_requirements_list()->List[str]:
          
 with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

  

       
# declaring variables for setup function
PROJECT_NAME="housing-predictor"
AUTHOR="Jayesh"
VERSION="0.0.2"
DISCRIPTION="This is first Major project in Machine Learning"

REQUIREMENT_FILE_NAME="requirements.txt"

setup( 
    name=PROJECT_NAME,
    author=AUTHOR,
    version=VERSION,
    discription=DISCRIPTION,
    packages=find_packages,
    install_requires=get_requirements_list()
)





