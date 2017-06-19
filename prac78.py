import math
n = int(raw_input("n>>"))
x = int (raw_input("x>>"))
sum=0
for i in range(1,n+1,2):
    sum=sum+ math.pow(x,i)
print "sum",sum


'''n = int(raw_input(">>"))
sum=0
sign=1
for i in range(1,n,3):
    sum=sum+i*sign
    sign= sign *-1
print "sum",sum

print '%5s'%'*'
for i in range(1,5):
    for j in range(1,2*i):
        print ('*')

print '%5s'%'\n'

for i in range(1,5):
    print "$"

'''
