# -*- coding: utf-8 -*-
import os
from distutils.core import setup
from vondrak import __version__

def pypi_rst_long(readme):
    desc = 'See `github.com/digitalvapor/vondrak <http://github.com/digitalvapor/vondrak>`_ for source and documentation.' # A fallback in case can't convert md to rst
    try:
        import pypandoc
        desc = pypandoc.convert(readme,'rst')
    except (IOError, ImportError):
        pass
    return desc

setup(name='vondrak',
      version = __version__,
      description = "a Python implementation of Vondrák's long term precession model",
      long_description = pypi_rst_long('readme.md'),
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
      ],
      )
