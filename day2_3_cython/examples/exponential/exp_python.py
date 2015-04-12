def exp(x, terms = 50):
    sum = 0.
    power = 1.
    factorial = 1.
    for i in range(terms):
        sum += power/factorial
        power *= x
        factorial *= i+1
    return sum
