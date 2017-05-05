def print_two(*args):
	arg1, arg2 = args
	print "agrg1: %r ,arg2:%r" %(arg1,arg2)

def print_two_again(arg1,arg2):
	print"arg1: %r ,arg2: %r" %(arg1,arg2)

def print_one(arg1):
	print "agr1:%r" %arg1

def print_none():
	print  "nothing"

print_two("neha","hooda")
print_two_again("neha","hoooda")
print_one("first")
print_none()