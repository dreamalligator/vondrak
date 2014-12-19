============
Introduction
============

The earth, like a wobbling top, has an axial precession which complete's one complete cycle in approximately 26,000 years. Astronomers often choose a favorite epoch, such as J2000, to express the coordinates of astronomical bodies in celestial coordinates. To convert between orientations, one must use a rotational matrix. This project implements the Vondrák long term precession model to create such a rotational precession matrix. This is relatively accurate for hundreds of thousands of years.

All credit for this precession model goes to Jan Vondrák and his colleagues.

Implementation
==============
A rotation matrix allows us to perform a rotation in Euclidean space. The rotation matrix obtained by using the Vondrák ltp model allows us to convert between the celestial orientation of J2000 and another epoch year.

A new position, or orientation, whether for the past or future, can be obtained by computing a rotation matrix for the epoch date of choice. This rotation matrix is then applied to the coordinates of the standard epoch to precess the position. **p₁** = **P·p₀**, where **P** is the precession matrix and **p₀** is the original position. **P** is computed for every epoch date that one wishes to orient to.

.. math::

    p_{1} = P\cdot p_{0} = \begin{pmatrix}
    P_{11} & P_{12} & P_{13} \\
    P_{21} & P_{22} & P_{23} \\
    P_{31} & P_{32} & P_{33}
    \end{pmatrix}
    \begin{pmatrix}
    x\\ y\\ z
    \end{pmatrix}
    =
    \begin{pmatrix}
    P_{11}x + P_{12}y + P_{13}z \\
    P_{21}x + P_{22}y + P_{23}z \\
    P_{31}x + P_{32}y + P_{33}z
    \end{pmatrix}

We now have the new celestial coordinates **p₁** expressed in the new reference epoch. The date is specified in the original computation of position with respect to the standard epoch and then maintained when the rotation matrix is applied.

Additionally, we can convert the coordinates of another epoch to the standard epoch by inverting the precession matrix. We transpose this like so

.. math::

    P^{-1} = \begin{pmatrix}
    P_{11} & P_{12} & P_{13} \\
    P_{21} & P_{22} & P_{23} \\
    P_{31} & P_{32} & P_{33}
    \end{pmatrix}

References
==========

* `Some New Thoughts About Long-Term Precession <http://syrte.obspm.fr/jsr/journees2010/pdf/Vondrak.pdf>`_ (2010)
* `New Long-Term Expressions for Precession <http://syrte.obspm.fr/jsr/journees2011/pdf/vondrak.pdf>`_ (2011)
* `New precession expressions, valid for long time intervals <http://www.aanda.org/articles/aa/pdf/2011/10/aa17274-11.pdf>`_ (2011)
* `New precession expressions, valid for long time intervals (Corrigendum) <http://www.aanda.org/articles/aa/abs/2012/05/aa17274e-11/aa17274e-11.html>`_ (2012)
