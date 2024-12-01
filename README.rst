====================================
Vondrák's Long Term Precession Model
====================================

.. image:: https://img.shields.io/pypi/pyversions/vondrak
   :alt: PyPI - Python Version

.. image:: https://img.shields.io/github/license/dreamalligator/vondrak
   :alt: GitHub License

.. image:: https://img.shields.io/pypi/v/vondrak
   :alt: PyPI - Version

.. image:: https://img.shields.io/badge/linting-pylint-yellowgreen
   :alt: Pylint

A Python implementation of Vondrák's long term precession model and Fortran code.

* `Some New Thoughts About Long-Term Precession <https://syrte.obspm.fr/jsr/journees2010/pdf/Vondrak.pdf>`_ (2010)
* `New Long-Term Expressions for Precession <https://syrte.obspm.fr/jsr/journees2011/pdf/vondrak.pdf>`_ (2011)
* `New precession expressions, valid for long time intervals <https://www.aanda.org/articles/aa/pdf/2011/10/aa17274-11.pdf>`_ (2011)
* `New precession expressions, valid for long time intervals (Corrigendum) <https://www.aanda.org/articles/aa/pdf/2012/05/aa17274e-11.pdf>`_ (2012)

Install
=======

There are no dependencies for Vondrák!

To install the `Vondrak Python package <https://pypi.python.org/pypi/vondrak>`_ via `PyPI <https://pypi.python.org/pypi>`_, simply ``pip install vondrak``. All code is hosted at `github.com/dreamalligator/vondrak <https://github.com/dreamalligator/vondrak>`_ and mirrored at `gitlab.com/dreamalligator/vondrak <https://gitlab.com/dreamalligator/vondrak>`.

Alternatively, clone the repo ``git clone https://github.com/dreamalligator/vondrak``, and install from source with ``python setup.py install``.

Documentation
=============

View the docs at `dreamalligator.github.io/vondrak <https://dreamalligator.github.io/vondrak>`_, or generate with ``make html`` in the ``docs`` folder.

Development
===========

Setup a conda environment by simply running ``conda env create --file environment.yml`` and activate by ``conda activate vondrak``.

Tests
=====

Tests use the `pytest <https://github.com/pytest-dev/pytest>`_ framework. Simply run ``pytest``.

License
=======

MIT
