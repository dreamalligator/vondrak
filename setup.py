#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Vondrak Python package setup."""

import os
import sys
from setuptools import setup
from vondrak import __version__


def read(*filenames):
    """It is handy to have both a readme and load it for long_description"""
    return open(os.path.join(os.path.dirname(__file__), *filenames)).read()

setup(
    name='vondrak',
    version=__version__,
    description=("A Python implementation of Vondrák's long term precession "
                 "model and Fortran code."),
    long_description=read('README.rst'),
    url='https://github.com/digitalvapor/vondrak',
    download_url='https://github.com/digitalvapor/vondrak/tarball/{0}'
        .format(__version__),
    author='Tom Spalding',
    author_email='tom@antivapor.net',
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
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: Astronomy'
    ],
    tests_require=['pytest'])
