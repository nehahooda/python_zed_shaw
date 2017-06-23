'''def fibo(n):
    if n==1 or n==2:
        return 1
    else:
        return (fibo(n-1)+ fibo(n-2))

print(fibo(8))

def check(a,b,c):
    if ((a*a) == (b*b) + (c*c)) or (b*b == a*a + c*c) or (c*c == a*a +b*b ) :
        print "YES "

    else :
        print "NO"
check(5,12,13)
'''
def check(no):
    n=2
    while(n<no):
        if no%n ==0:
            return False
        n=n+1

    return True

y = check(23)
print y