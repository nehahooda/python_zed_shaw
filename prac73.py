'''bars = int(raw_input("bars="))
boxes = int (raw_input("boxes="))
noboxes= bars/40
left= bars%40
print "number odf boxes filled:",noboxes
print "leftovers:",left

print "**************"
inch = int (raw_input(">>"))
feet = inch/12
inches = inch%12
print inch,"inch=",feet,"feets",inches,"inches"

mm = int(raw_input("enter a length in mm"))
m = mm/1000
x = mm%1000
cm = x/10
mm1 = cm %10
print mm,"mm=",m,"m",cm,"cms",mm1,"mm"

no = int (raw_input("enter a 3 digit number:"))
x = no/100
y = no%100
z= y/10
i = y%10
print "sum of the digits are:",x+z+i
'''
no = int (raw_input("enter a 4 digit number:"))
x = no/1000
y = no%1000
t=y/100
q= y%100
z= q/10
i = q%10
print "sum of the digits are:",x+t+z+i