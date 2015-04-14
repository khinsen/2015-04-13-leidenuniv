cimport cython

@cython.cdivision(True)
def exp(double x, int terms = 50):
    cdef double sum
    cdef double power
    cdef double factorial
    cdef int i
    sum = 0.
    power = 1.
    factorial = 1.
    for 0 <= i < terms:
        sum += power/factorial
        power *= x
        factorial *= i+1
    return sum
