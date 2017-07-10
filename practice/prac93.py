class base(object):
    def __init__(self,x):
        self.x=x

class derived(base):
    def __init__(self,x,y):
        base.x=x
        self.y=y

    def printxy(self):
        print(base.x,self.y)


d= derived(10,29)
d.printxy()

