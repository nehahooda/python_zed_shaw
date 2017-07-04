import numpy as np
x= np.ones((3,4))
y= np.random.random((5,1,4))
x+y
print (x)

my_array=np.array([[1,2,3,4],[5,6,7,8]],dtype =np.int64)
print(my_array)
print(my_array[0:2])
print(my_array[my_array<2])