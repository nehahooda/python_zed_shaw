print "lets practice everything."
print "You'd \'d need to know about escapes with \\ that do \n new lines and \t tabs."
poem = """
The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires n explanation
\n\t\t where there is none.
"""

print "------------"
print poem
print "------------"

five =10-2+4-6
print "this should be five: %s " %five

def secret_formula(started):
	jelly=started *500
	jars = jelly /1000
	crates =jars/100
	return jelly,jars,crates

sp=10000
beans,jars,crates =secret_formula(sp)

print "the starting point of :%d"% sp
print "we'd have %d,%djars and %d crates."%(beans,jars,crates)

sp=sp/10
print "we can also do thta this way"
print "we'd have %d beans,%d jars, and %d crates."%secret_formula(sp)