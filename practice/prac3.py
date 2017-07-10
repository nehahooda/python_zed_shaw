a =[1,2,3,4,5,6,7,8,9,10]
num =int(raw_input("choose a number"))

new_list = []

for i in a:
     if i<num:
         new_list.append(i)

print new_list