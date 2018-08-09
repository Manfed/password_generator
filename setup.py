#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(name='password_generator',
      version='1.0',
      packages=find_packages(exclude=["test/", "bin/"]),
      install_requires=[
            'flask==1.0.2',
            'flask-cors==3.0.6',
            'Flask-SQLAlchemy==2.3.2',
            'lxml==4.2.3',
            'apscheduler==3.5.1',
            'flasgger==0.5.14'
      ],
      scripts=['bin/start_generator.py']
)
