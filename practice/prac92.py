class person:
    def __init__(self,f,l):
        self.fname=f
        self.lname=l

    def name(self):
        return self.fname+ " " +self.lname


class emp(person):
    def __init__(self,f,l,no):
        person.__init__(self,f,l)
        self.sno= no
    def getemp(self):
        return self.name() + "," + self.sno


x= person("karan","simpson")
y = emp("siran","gupta","1009")


print(x.name())
print(y.getemp())