class Other(object):
    def override(self):
        print"OTHER OVERRIDE()"
    def implicit(self):
        print "PTHER IMPLICIT()"
    def altered(self):
        print "OTHER ALTERED()"

class Child(object):
    def __init__(self):
        self.other =Other()
    def implicit(self):
        self.other.implicit()
    def override(self):
        print"CHILD OVERRIDE()"
    def altered(self):
        print "CHILD ,BEFORE OTHER ALTERED()"
        self.other.altered()
        print "CHILD,AFTER OTHER ALTERED()"

son = Child()

son.implicit()
son.override()
son.altered()
