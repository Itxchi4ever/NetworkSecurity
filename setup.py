'''
This setup.py file is an essential part of packaging and distributing Python Projects.
It is use by setuptools (or distutils in older python versions.) To define the configuration
of your project, such as its metadata, dependencies, and more.
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements 
    """

    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Read lines from the file
            line=file.readlines()
            ## Process each line
            for line in line:
                requirement=line.strip()
                ## Ignore the empty lines and -e .
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirement.txt file not found")

    return requirement_lst

setup(
    name="Network Security",
    version="0.0.1",
    author="Harsh Shukla",
    author_email="hjsshukla@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)