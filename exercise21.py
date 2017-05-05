def add(a,b):
 	print "add %d + %d" %(a,b)
 	return a+b

def sub(a,b):
  print "sub %d - %d" %(a,b)
  return a-b

def mul(a,b):
  print "mul %d * %d" %(a,b)
  return a*b

def div(a,b):
  	print"div %d / %d" %(a,b)
  	return a/b


print "lets do something fun"
age= add(20,2)
hg= sub(78,4)
wg =mul(90,3)
iq=div(100,2)

print "age: %d,hg: %d,wg:%d,iq:%d" %(age,hg,wg,iq)

print"heres a puzzle"
what = add(age,sub(hg,mul(wg,div(iq,2))))
print "that becomes",what,"can you do it by hand?"