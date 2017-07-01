from sys import argv
script,fn = argv
txt = open(fn)
print "here is your file " % fn
print txt.read()
print "type filename again"
fa=raw_input(">>")
ta=open(fa)
print ta.read()
