'''
c= 'y'
p=0
tot=0
while(c=='y'):
    p= int(raw_input("price>>"))
    d= (p*5.5)/100
    p=p-d
    tot=tot+p
    print "final price",p
    print "enter your choice"
    c = raw_input("c>>")

no = int(raw_input(">>"))
rev=0
while no>0:
    d1= no%10
    rev=rev*10+d1
    no=no/10
print rev


sum=0
for i in range(1,6):
    no=int(raw_input(">>"))
    if no>sum:
        sum=no

print "largest is",sum
'''
c=0
while c<67:
    print c
    c=c+9
else:
    print "OVER"