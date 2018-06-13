#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(name='password_generator',
      version='1.0',
      packages=find_packages(exclude=["test/", "bin/"]),
      install_requires=[
            'flask==1.0.2'
      ],
      scripts=['bin/password_generator.py']
)