'''a = int(raw_input("sub1>>"))
b = int(raw_input("sub2>>"))
c = int(raw_input("sub3>>"))
avg = (a+b+c)/3
if avg>40:
    print "PASS"
    print "AVERAGE",avg
else:
    print "FAIL"
    print "AVERAGE",avg
   

no = int(raw_input(">>"))
if no%2==0 and no>0:
    print "even and positive"
elif no%2==0 and no<0:
    print "EVEN AND NEGATIVE"
elif no%2!=0 and no>0:
    print "ODD AND POSITIVE"
else:
    print "ODD AND NEGATIVE" 
    



r = int(raw_input("input radius:"))
print "enter a for area and c for circumference"
ch = raw_input(">>")
if ch == 'a':
    print "area",3.14*r*r

elif ch =='c':
    print "circumference",2*3.14*r
else:
    print "wrong choice"


b = raw_input("enter your choice of bank:p for PNB and s for SBI")
p = int (raw_input("PRINCIPLE>>"))
t = int(raw_input("TIME>>"))
r=7
if b=='p':
    r = 7.5/100
elif b =='s':
    r = 7/100
else:
    print "you entered wrong bank"

print "AMOUNT:",(p*r*t)/100
'''
a = int(raw_input("no1>>"))
b = int(raw_input("no2>>"))
symb = raw_input("symbol:+ or -")
if (symb=='+'):
    print "ADD",a+b
elif symb =='-':
    print "SUBTRACT",a-b
else:
    print "wrong symbol"
    