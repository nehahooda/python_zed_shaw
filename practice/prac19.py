print "input 2 values"
c = raw_input(">a")
b = raw_input(">b")
print (isinstance(c,int))
if not (isinstance(c,int) and isinstance(b,int)):
    print "sum is", c+b
else:
    print"sorry..wrong type variables"