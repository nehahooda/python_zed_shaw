'''import os
import math
a = [0]*20

for i in range(0,4):
    a[i]=int (raw_input(">>"))

os.system('cls')
for i in range(0,4):
    print "number",a[i]
    print "square root",math.sqrt(a[i])
    print "square",a[i]*a[i]
    print "******************"


a= [0]*5
b= [0]*5
c= [0]*5
for i in range(0,4):
    a[i]= int(raw_input("a>>"))
    b[i]= int (raw_input("b>>"))
    c[i]= a[i] +b[i]

for i in range(0,4):
    print "C",c[i]
   
print "enter prices for 10"
p=[0]*10
c=0
for i in range(0,10):
    p[i]=int(raw_input("p>>"))

v= int(raw_input(" price>>"))
for i in range(0,10):
    if p[i]==v:
        c=0
        break
    else:
        c=c+1
        continue

if c!=0:
    print "SORRY THE VALUE WAS not present"
else:
    print"value found"
'''
import os
a=[0]*10
b=[0]*5
c=[0]*15
for i in range(0,10):
    a[i]= int(raw_input(">>"))
for i in range(0,5):
    b[i]= int(raw_input(">>"))

for i in range(0,5):
    c[i]=b[i]
for i in range(0,10):
    c[i+5]= a[i]

os.system('cls')
for i in range(0,15):
    print "C",c[i]

