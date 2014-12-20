# -*- coding: utf-8 -*-
import os
from setuptools import setup
from vondrak import __version__

def read(*filenames):
    return open(os.path.join(os.path.dirname(__file__), *filenames)).read()

setup(
    name='vondrak',
    version = __version__,
    description = "A Python implementation of Vondrák's long term precession model and Fortran code.",
    long_description = read('readme.rst'),
    url = 'https://github.com/digitalvapor/vondrak',
    download_url = 'https://github.com/digitalvapor/vondrak/tarball/{0}'.format(__version__),
    author = 'Tom Spalding',
    author_email = 'tommycs@mail.sfsu.edu',
    keywords = ['astronomy', 'precession', 'vondrak', 'space', 'proper motion'],
    license = 'Creative Commons Attribution-ShareAlike 4.0 International License',
    packages = [
        'vondrak',
        'vondrak.tests',
    ],
    package_data = {
        'vondrak': ['docs/*.rst'],
    },
    install_requires = ['numpy'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering :: Astronomy',
    ])
