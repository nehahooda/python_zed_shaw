from sys import argv

script,input_filr = argv

def print_all(f):
	print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
	print line_count,f.readline()

currnt_file =open(input_file)
print "first lets print the whole files:\n"
print_all(currnt_file)

print "now lets rewind ,kind of like a tape"
rewinf(currnt_file)

print "lets print 3 lines:"
currnt_line=1
print_a_line(currnt_line,currnt_file)
currnt_line=currnt_line+1
print_a_line(currnt_line,currnt_file)
currnt_line=currnt_line+1
print_a_line(currnt_line,currnt_file)