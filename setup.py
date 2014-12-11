# -*- coding: utf-8 -*-
import os
from setuptools import setup

def read(*filenames):
    return open(os.path.join(os.path.dirname(__file__),*filenames)).read()

setup(name='vondrak',
      version='0.01',
      description="a Python implementation of Vondrák's long term precession model",
      long_description = read('readme.md'),
      url='https://github.com/digitalvapor/vondrak',
      author='Thomas C. Spalding',
      author_email='tommycs@mail.sfsu.edu',
      license='Creative Commons Attribution-ShareAlike 4.0 International License',
      packages=['vondrak'],
      classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Astronomy',
      ],
      zip_safe=False
      )
