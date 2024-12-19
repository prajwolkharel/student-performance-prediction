from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'


def get_requirements(file_path:str)->List[str]:
    """Returns the list of requirements"""
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [x.replace('\n', '') for x in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='student-performance-prediction',
    version='0.0.1',
    author='prajwol',
    author_email='abc@prajwol.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
