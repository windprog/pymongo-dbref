#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   15/1/31
Desc    :   
"""
from setuptools import setup

from pymongo_dbref import __version__, __author__, __author_email__, __description__, __url__, __title__

INSTALL_REQUIRES = []
with open('requirements.txt') as f:
    INSTALL_REQUIRES = [r for r in f.read().split('\n') if len(r) > 0]

setup(
    name=__title__,
    version=__version__,
    description=__description__,
    url=__url__,
    author=__author__,
    author_email=__author_email__,
    packages=[__title__],
    install_requires=INSTALL_REQUIRES
)