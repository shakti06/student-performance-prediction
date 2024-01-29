from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path : str)->List[str]:
    '''
    @return the list of arguments
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements ]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='student performance predictor',
    version='0.0.1',
    description='app that predicts the performance of the students',
    author='shakti',
    author_email='optional',
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
    
)