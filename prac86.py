'''def max1(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c


x=int(raw_input("no1>>"))
y= int(raw_input("no2>>"))
z=int(raw_input("no3>>"))
max1 = max(x,y,z)
print "the maximum is:",max1

def sum(no):
    t=0
    for x in no:
        t+=x
    return t
print (sum((4,5,6,7,89,0)))

def rever(stg):
    s1=''
    i=len(stg)
    while i>0:
        s1+=stg[i-1]
        i=i-1
    return s1
n=raw_input("string>>")
print(rever(n))

def fact(n):
    if n==0:
        return 1
    else :
        return n*fact(n-1)

    
n1=int(raw_input("number>>"))
print("factorial of the number",fact(n1))

def search(no,li):
    if no in li:
        return "yes"
    else:
        return "NO"


print("search says",search(8,(1,2,3,4,5,6,7,8)))
'''
def see(strn):
    tu = sum(1 for c in strn if c.isupper())
    tl = sum(1 for c in strn if c.islower())
    return tu,tl


print("number of upper and lowercase",see("HI mt name is neha"))