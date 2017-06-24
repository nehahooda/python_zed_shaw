a=2
print 'id(a)=',id(a)
a=a+1
print 'id(a)=',id(a)
print 'id(3)=',id(3)
b=2
print'id(2)=',id(2)
def hi():
    print "HELLO"
a= hi()
a
class Myclass:
    "this is my first class"
    a=10
    def fun(self):
        print "HELLO"

print(Myclass.a)
print(Myclass.fun)
print(Myclass.__doc__)
