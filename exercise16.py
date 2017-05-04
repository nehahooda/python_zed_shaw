from sys import argv

script ,filename = argv

print "we are going ton erase %r" %filename
print "if you dnt want that hit CTRL-C(^C)."
print"if you do want that,hit RETURN"
raw_input("?")

print  "opening the file: "
target =open(filename,'w')

print "truncating the file.goodbye"
target.truncate()

print "now type 3 lines as following"
line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "Im going to write these line in the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print"and finally close it"

target.close()