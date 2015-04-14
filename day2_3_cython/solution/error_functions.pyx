cdef extern from "mconf.h":
    # The C functions are renamed in order to prevent a naming conflict
    # with the Python functions defined below.
    double c_erf "erf" (double x)
    double c_erfc "erfc" (double x)

def erf(double x):
    return c_erf(x)

def erfc(double x):
    return c_erfc(x)
