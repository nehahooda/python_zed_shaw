class Parent(object):
    def override(self):
        print"PARENT OVERRIDE()"
    def implicit(self):
        print"PARENT IMPLICIT()"
    def altered(self):
        print"PARENT ALTERED()"
class Child(Parent):
    def override(self):
        print"CHILD OVERRIDE()"
    def altered(self):
        print"CHILD,BEFORE PARENT ALTERED()"
        super(Child,self).altered()
        print "CHILD,AFTER PARENT ALTERED()"

dad=Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()


