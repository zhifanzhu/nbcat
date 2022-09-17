from setuptools import find_packages, setup

setup(
    name='nbcat',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'nbcat = nbcat:app_main',
        ]
    }
)