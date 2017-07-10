'''

for i in range(ord('a'),ord('z')+1):
    print chr(i)

print "********************"
print "enter 10 numbers:"
a=[0]*10
for i in range(0,10):
    a[i]= int(raw_input(">>"))

for i in range (0,10):
    if a[i]%7 ==0:
        print a[i]

'''

print "enter two values:"
a = int(raw_input("a>>"))
b = int (raw_input("b>>"))
sum =0
for i in range(a,b):
    if i%5 ==0 and i%7==0 :
        print i
        sum = sum +i

print "sum",sum