import numpy as np
my_array=np.array([[1,2,3,4],[5,6,7,8]],dtype =np.int64)
print(my_array)

#make different types of array
np.ones((3,4))
#np.zeroes((2,3,4),dtype =np.int16)
np.random.random((2,2))
np.empty((3,2))
np.full((2,2),7)
np.arange(10,25,5)
np.linspace(0,2,9)


#importing data
x,y,z = np.loadtxt('data.txt',
                   skiprows=1,
                   unpack=True)

#importing another file
my_array2= np.genfromtxt('data2.txt',
                         skip_header =1,
                         filling_values=-999)
#saving files
x= np.arange(0.0,5.0,1.0)
np.savetext('test.out',x,delimiter=',')
