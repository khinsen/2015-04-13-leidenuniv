# To compile:
#      python setup.py build_ext --inplace

from distutils.core import setup, Extension
from Cython.Distutils import build_ext

setup (name = "error_functions",
       version = "0.1",

       ext_modules = [Extension('error_functions',
                                ['error_functions.pyx',
                                 'ndtr.c', 'polevl.c'])],

       cmdclass = {'build_ext': build_ext}
       )
