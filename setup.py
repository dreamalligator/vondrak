#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Vondrak Python package setup."""

import os
import sys
from setuptools import setup
from vondrak import __version__

"""It is handy to have both a readme and load it for long_description"""
with open("README.rst", "r") as f:
	long_description_readme = f.read()

setup(
    name='vondrak',
    version=__version__,
    description=("A Python implementation of Vondrák's long term precession "
                 "model and Fortran code."),
    long_description=long_description_readme,
    url='https://github.com/dreamalligator/vondrak',
    download_url='https://github.com/dreamalligator/vondrak/tarball/{0}'
        .format(__version__),
    author='Tom Spalding',
    author_email='tom@blackforestbotanics.com',
    keywords=['astronomy', 'precession', 'vondrak', 'space', 'proper motion'],
    license='MIT',
    packages=[
        'vondrak',
        'vondrak.tests',
    ],
    package_data={
        'vondrak': ['docs/*.rst'],
    },
    install_requires=['numpy'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Scientific/Engineering :: Astronomy'
    ],
    tests_require=['pytest'])
