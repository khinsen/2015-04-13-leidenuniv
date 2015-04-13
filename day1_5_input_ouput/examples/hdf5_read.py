import h5py
import numpy as np

h5file = h5py.File('test.h5', 'r')

for item in h5file:
    print item

foo = h5file['foo'][...]
foo_units = h5file['foo'].attrs['units']
print foo[0]

h5file.close()
