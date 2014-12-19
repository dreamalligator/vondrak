#Vondrák's Long Term Precession Model

[![Build Status](https://travis-ci.org/digitalvapor/vondrak.svg)](https://travis-ci.org/digitalvapor/vondrak)

This is a Python implementation of Vondrák's long term precession model and Fortran code. This code stems from an IPython notebook ([vondrak.ipynb](http://nbviewer.ipython.org/github/digitalvapor/asterisms/blob/master/notebooks/vondrak.ipynb)) I wrote to figure out how to implement a long term precession model.

* [Some New Thoughts About Long-Term Precession](http://syrte.obspm.fr/jsr/journees2010/pdf/Vondrak.pdf) (2010)
* [New Long-Term Expressions for Precession](http://syrte.obspm.fr/jsr/journees2011/pdf/vondrak.pdf) (2011)
* [New precession expressions, valid for long time intervals](http://www.aanda.org/articles/aa/pdf/2011/10/aa17274-11.pdf) (2011)
* [New precession expressions, valid for long time intervals (Corrigendum)](http://www.aanda.org/articles/aa/abs/2012/05/aa17274e-11/aa17274e-11.html) (2012)

#Dependencies
The only dependency is [numpy](https://github.com/numpy/numpy).

#Install
To install the [Vondrak Python package](https://pypi.python.org/pypi/vondrak), simply `pip install vondrak`. All code is hosted at [github.com/digitalvapor/vondrak](https://github.com/digitalvapor/vondrak).

#Documentation
View [here](http://nbviewer.ipython.org/github/digitalvapor/vondrak/blob/master/vondrak/docs/documentation.ipynb), generate with `ipython nbconvert --to html documentation.ipynb`, or run `ipython notebook`.

The Sphinx docs can be generated with `make html`.

#License
This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
