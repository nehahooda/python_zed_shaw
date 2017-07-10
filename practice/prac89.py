'''class complex:
    def __init__(self,r=0,i=0):
        self.real=r
        self.ima=i

    def get(self):
        print ("{0} + {1}j".format(self.real,self.ima))



c1=complex(2,3)
c1.get()
c2= complex(5)
c2.aat=10
print(c2.real,c2.ima,c2.aat)
'''
class student:
    global roll
    global name
    global mark1
    global mark2
    global avg

    def input(self):
        roll= int(raw_input("roll no>>"))
        name = raw_input("name>>")
        mark1=int(raw_input("m1>>"))
        mark2 =int(raw_input("m2>>"))
        avg= (mark1 +mark2)/2

    def show(self):
        print "roll no:",roll
        print "name",name
        print "averge",avg



ob1=student()
ob1.input()
ob1.show()




