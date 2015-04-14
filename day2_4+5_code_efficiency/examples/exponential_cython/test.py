import exp_python
import exp_cython
import exp_cython_cdivision
import exp_python_annotated
import math
import time

print exp_python.exp(10.), \
      exp_cython.exp(10.), \
      exp_cython_cdivision.exp(10.),\
      exp_python_annotated.exp(10.), \
      math.exp(10.)

start = time.clock()
for i in range(50000):
    exp10 = exp_python.exp(10.)
print time.clock()-start

start = time.clock()
for i in range(50000):
    exp10 = exp_cython.exp(10.)
print time.clock()-start

start = time.clock()
for i in range(50000):
    exp10 = exp_cython_cdivision.exp(10.)
print time.clock()-start

start = time.clock()
for i in range(50000):
    exp10 = exp_python_annotated.exp(10.)
print time.clock()-start

start = time.clock()
for i in range(50000):
    exp10 = math.exp(10.)
print time.clock()-start

