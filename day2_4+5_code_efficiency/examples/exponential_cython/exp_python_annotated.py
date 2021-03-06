import cython

@cython.locals(x=cython.double, terms=cython.int,
               sum=cython.double, power=cython.double, factorial=cython.double,
               i=cython.int)
def exp(x, terms = 50):
    sum = 0.
    power = 1.
    factorial = 1.
    for i in range(terms):
        sum += power/factorial
        power *= x
        factorial *= i+1
    return sum
