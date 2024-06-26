#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='nameko-examples-transport-a',
    version='0.0.1',
    description='Rental Car Transportations with Nameko',
    author='nameko',
    packages=find_packages(exclude=['test', 'test.*']),
    # py_modules=['user'],
    install_requires=[
        "marshmallow==2.19.2",
        "nameko==v3.0.0-rc6",
        "mysqlclient==1.4.6",  # Added MySQL client
        "mysql-connector-python==8.0.26",
        "boto3==1.34.133"  # Added boto3
    ],
    extras_require={
        'dev': [
            'pytest==4.5.0',
            'coverage==4.5.3',
            'flake8==3.7.7',
        ]
    },
    zip_safe=True,
)