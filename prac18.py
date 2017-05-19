#part1
color_list1 =["white","black","red"]
color_list2 =["red","green"]

for i in color_list1:
    if i not in color_list2:
        print i


print "enter 3 numbers"
a = raw_input("a:")
b = raw_input("b:")
c = raw_input("c:")

if ( a==b or c==a or b==c):
    sum =0
else:
    sum = a+b+c


print "sum of the numbers is:",sum