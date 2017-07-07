import numpy as np
from numpy import pi
print(np.arange(10,30,5))
print(np.linspace(0,2,9))
x= np.linspace(0,2*pi,100)
f = np.sin(x)
print(f)

print(np.arange(10000))
print(np.arange(10000).reshape(100,100))
np.set_printoptions(threshold='nan')
print(np.arange(10000))
print(np.arange(10000).reshape(100,100))
