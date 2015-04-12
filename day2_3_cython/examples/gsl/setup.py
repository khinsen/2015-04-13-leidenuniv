# To compile:
#      python setup.py build_ext --inplace

from distutils.core import setup, Extension
from Cython.Distutils import build_ext
import os, sys

setup (name = "BesselI0",
       version = "0.1",

       ext_modules = [Extension('gsl_bessel',
                                ['gsl_bessel.pyx'],
                                include_dirs =['/usr/local/include'],
                                library_dirs = ['/usr/local/lib'],
                                libraries=['gsl', 'gslcblas', 'm'])],

       cmdclass = {'build_ext': build_ext}
       )
