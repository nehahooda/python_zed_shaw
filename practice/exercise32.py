count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change =[1,'pennies',2,'dimes',3,'quarters']

#this first kind of for loops goes through a list

for number in count:
	print "this is count%d" %number

for fruit in fruits:
	print "a fruit of types:%s" %fruit

for i in change:
	print "I got %r" %i

elements = []
for i in range(0,6):
	print "adding %d to the list "%i
	elements.append(i)

for i in elements:
	print "elements was :%d" %i