import h5py
import numpy as np

h5file = h5py.File('test.h5', 'w')
h5file.attrs['version'] = 42

foo = h5file.create_dataset('foo', (20, 3), dtype=np.float64)
foo[:,:] = 0.
foo[0,:] = [42., 42., 42.]
foo[:,1] = 1.
foo.attrs['units'] = "arbitrary"

bar = h5file.create_dataset('bar', (0, 20), dtype=np.int32,
                            chunks=(10, 10), maxshape=(None, 20))
for i in range(10):
    bar.resize((i+1, 20))
    bar[i, :] = i*np.ones((1, 20), np.int)

h5file.close()
