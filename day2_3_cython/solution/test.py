from error_functions import erf, erfc
import numpy

for x in numpy.arange(-5., 5., 0.5):
    assert erf(x) + erfc(x) - 1. < 1.e-7
