
class Parent(object):
    def altered(self):
        print "PARENT ALTERED()"
class Child(Parent):
    def altered(self):
        print"CHILD ,BEFORE PARENT ALTERED()"
        super(Child,self).altered()
        print"CHILD ,AFTER PARENT ALTERED()"

dad =Parent()
son = Child()


dad.altered()
son.altered()