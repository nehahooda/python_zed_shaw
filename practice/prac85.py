'''n1 = raw_input("n1>>")
n2 = raw_input("n2>>")
if n1 == n2:
    print"same strings"
else:
    print"not equal"
   
n= raw_input("string>>")
n1= n.split()
print ("number of at",sum(1 for c in n1 if c =='at'))
'''
n1 = raw_input("string>>>")
n= n1.split()

print n1.replace("at","on")
print n1.title()
n2 = raw_input("string2>>")
print n1+n2
