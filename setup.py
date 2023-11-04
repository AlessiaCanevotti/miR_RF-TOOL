from setuptools import setup, find_packages

setup(
    name='miR_RF_Tool',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'miR_RF_Tool=application:main',
        ],
    },
    install_requires=[
        'itertools',
        'pandas as pd'
        're'
        'sys'
    ],
)
