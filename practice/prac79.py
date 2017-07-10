'''a=1
b=1
c =0

for i in range(1,20):
    c=a+b
    print c
    a=b
    b=c    
   
n =int(raw_input(">>"))
ctr=0
for  i in range(1,n):
    if n%i==0:
        ctr=ctr+1
if ctr==0:
    print "PRIME NUMBER"


for i in range(4,1,-1):
    for j in range(4,1,-1):
        print j

'''
m= int(raw_input("m>>"))
n= int(raw_input("n>>"))
ctr=0
for i in range(m,n):
    for j in range(2,m-1):
        if i%j ==0:
            ctr=1

    if(ctr==0):
        print "PRIME",i