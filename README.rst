====================================
Vondrák's Long Term Precession Model
====================================

.. image:: https://img.shields.io/pypi/pyversions/vondrak
   :alt: PyPI - Python Version

.. image:: https://img.shields.io/github/license/dreamalligator/vondrak
   :alt: GitHub License

.. image:: https://img.shields.io/pypi/v/vondrak
   :alt: PyPI - Version

A Python implementation of Vondrák's long term precession model and Fortran code.

* `Some New Thoughts About Long-Term Precession <http://syrte.obspm.fr/jsr/journees2010/pdf/Vondrak.pdf>`_ (2010)
* `New Long-Term Expressions for Precession <http://syrte.obspm.fr/jsr/journees2011/pdf/vondrak.pdf>`_ (2011)
* `New precession expressions, valid for long time intervals <http://www.aanda.org/articles/aa/pdf/2011/10/aa17274-11.pdf>`_ (2011)
* `New precession expressions, valid for long time intervals (Corrigendum) <http://www.aanda.org/articles/aa/abs/2012/05/aa17274e-11/aa17274e-11.html>`_ (2012)

Dependencies
============

The only dependency is `numpy <https://github.com/numpy/numpy>`_.

Install
=======

To install the `Vondrak Python package <https://pypi.python.org/pypi/vondrak>`_ via `PyPI <https://pypi.python.org/pypi>`_, simply ``pip3 install vondrak``. For Python 2, use ``pip``. All code is hosted at `github.com/digitalvapor/vondrak <https://github.com/digitalvapor/vondrak>`_.

Alternatively, clone the repo ``git clone https://github.com/digitalvapor/vondrak``, and install from source with ``python3 setup.py install``.

Documentation
=============

View the docs at `digitalvapor.github.io/vondrak <https://digitalvapor.github.io/vondrak>`_, or generate with ``make html`` in the ``docs`` folder.

Development
=====
Setup a conda environment by simply running ``conda env create --file environment.yml`` and activate by ``conda activate vondrak``

Tests
=====

Tests use the `pyttest <https://github.com/pytest-dev/pytest>`_ framework. Simply run ``py.test``.

License
=======

This work is licensed under a `Creative Commons Attribution-ShareAlike 4.0 International License <http://creativecommons.org/licenses/by-sa/4.0/>`_.
