# -*- coding: utf-8 -*-
import os
from distutils.core import setup
from vondrak import __version__

def pypi_rst_long(readme):
    desc = 'See `github.com/digitalvapor/vondrak <http://github.com/digitalvapor/vondrak>`_ for source and documentation.' # A fallback in case can't convert md to rst
    try:
        import pypandoc
        desc = pypandoc.convert(readme,'rst')
    except:
        pass
    return desc

setup(name='vondrak',
      version = __version__,
      description = "a Python implementation of Vondrák's long term precession model",
      long_description = pypi_rst_long('readme.md'),
      url = 'https://github.com/digitalvapor/vondrak',
      download_url = 'https://github.com/digitalvapor/vondrak/tarball/{}'.format(__version__),
      author = 'Tom Spalding',
      author_email = 'tommycs@mail.sfsu.edu',
      keywords = ['astronomy', 'precession', 'vondrak', 'space', 'proper motion'],
      license = 'Creative Commons Attribution-ShareAlike 4.0 International License',
      packages = ['vondrak'],
      classifiers = [
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Astronomy',
      ],
      )
