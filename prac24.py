
#print path of the current working directory

import os
print ("Current File Name:",os.path.realpath(__file__))

#print OS name,platform and release

import platform
print("OS NAME",os.name)
print("PLATFORM SYSTEM",platform.system())
print("PLATFORM RELEASE",platform.release())


#print no. of cpus using it

import multiprocessing
print("NO OF CPU",multiprocessing.cpu_count())


#print list of all directories

from os import listdir
from os.path import isfile,join
file_list = [f for f in listdir('d:/neha/python ')if isfile (join('d:/neha/python',f))]
print(file_list);