def SI(a,b,c):
    return a*((1+(0.01*b))**c)


print "helloo..iam here to calculate simple interest\npls enter pricipal amount \n rate of interes \nand number of years"
p = int(raw_input(">"))
i = float(raw_input(">"))
y = int(raw_input(">"))
t= int(p*i*y)
print t
s = SI(p,i,y)
print"the simple interest is",s