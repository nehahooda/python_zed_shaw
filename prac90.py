class polygon:
    def __init__(self,nos):
        self.n=nos
        self.sides=[0 for i in range(nos)]

    def isides(self):
        self.sides=[float (input("Enter side"+str(i+1)+":")) for i in range(self.n)]

    def disp(self):
        for i in range(self.n):
            print("side",i+1,"is",self.sides[i])



class Triangle(polygon):
    def __init__(self):
        polygon.__init__(self,3)
    def Area(self):
        a,b,c = self.sides
        s= (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))** 0.5
        print("area %0.2f",area)


t=Triangle()
t.isides()
t.disp()
t.Area()

print isinstance(t,Triangle)
isinstance(t,polygon)
isinstance(t,int)
isinstance(t,object)
issubclass(polygon,Triangle)
issubclass(Triangle,polygon)
issubclass(bool,int)
