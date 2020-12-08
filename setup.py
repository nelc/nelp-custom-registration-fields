#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports ###########################################################

import os
from setuptools import setup, find_packages


# Main ##############################################################

setup(
    name='nelp-custom-registration-fields',
    version='1.1',
    description='NELP - Custom LMS Registration Extension Form',
    author='OpenCraft',
    author_email='help@opencraft.com',
    url='https://github.com/open-craft/nelp-custom-registration-fields',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django',
    ],
)
