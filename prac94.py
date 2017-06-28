class neha(object):
    def __init__(self,n):
        self.name = n

class slaves(neha):
    def __init__(self,n,s):
        neha.name=n
        self.srname=s

    def printt(self):
        print(neha.name,self.srname)


s= slaves("neha","hooda")
s.printt()