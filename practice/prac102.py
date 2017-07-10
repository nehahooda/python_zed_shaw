import numpy as np
import matplotlib.pyplot as plt
x= np.ones((3,4))
y= np.random.random((5,1,4))
x+y
print (x)

my_array=np.array([[1,2,3,4],[5,6,7,8]],dtype =np.int64)
print(my_array)
print(my_array[0:2])
print(my_array[my_array<2])

#histogram

my_3d_array =np.array([[[1,2,3,4],[5,6,7,8],[1,2,3,4],[9,10,11,12]]],dtype=np.int64)
print(np.histogram(my_3d_array))
print(np.histogram(my_3d_array,bins=range(0,13)))

plt.hist(my_3d_array.ravel(),bins=range(0,13))
plt.title("frequency of 3D array")
plt.show()


#using meshgrid

points =np.arange(-5,5,0.01)
xs,ys = np.meshgrid(points,points)
z= np.sqrt(xs**2 + ys **2)
plt.imshow(z,cmap=plt.cm.gray)
plt.colorbar()
plt.show()
