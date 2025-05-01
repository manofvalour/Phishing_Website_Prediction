from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """

    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()

            ## process each lines
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e.
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print('Requirements.txt file not found')

    return requirement_lst

setup(
    name='NewtworSecurity',
    version='0.0.1',
    author='Emmanuel Ajala',
    author_email='ajalae2@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)