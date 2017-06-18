'''a =  int(raw_input("a>>"))
pro = 1
for i in range(1,a+1):
    pro= pro*i


print pro

import math
a = int(raw_input("a>>"))
b = int(raw_input("b>>"))

for i in range(a,b):
    if math.sqrt(i) * math.sqrt(i) == i:
        print "perfect number",i
    print i**3


a = int(raw_input("no>>"))
sum =0

for i in range(1,2*a-1,2):
    sum = sum+i

print "sum",sum

'''

print"enter 10 numbers:"
a = [0]*10
p=0
e=0
n=0
o=0
for i in range(0,10):
    a[i]= int(raw_input(">>"))
    if a[i]<0 :
        n = n+a[i]
    if a[i]%2==0:
        e=e+a[i]
    if a[i]%2!=0:
        o=o+a[i]
    if a[i]>0:
        p=p+a[i]

print "EVEN SUM",e
print "NEGATIVE SUM",n
print "ODD SUM",o
print "POSITVE SUM",p
