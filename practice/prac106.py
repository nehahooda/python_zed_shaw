import numpy as np
a = np.arange(15).reshape(3,5)
print(a)
print(a.shape)
print(a.ndim)
print(a.itemsize)
print(type(a))

b= np.array([6,7,8])
print(b)
print(type(b))

c = np.array([[1,2],[3,4]],dtype=complex)
print(c)
print(np.zeros((3,5)))
print(np.ones((2,3,4),dtype=np.int16))
print(np.empty((2,3)))