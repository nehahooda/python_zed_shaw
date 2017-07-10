import operator
d = {1:2,3:4,4:3,2:1,0:0}
print "original dictipnary",d
sd = sorted(d.items,key =operator.itemgetter(0))
print "dictionary in ascending order by value:",sd
sd = sorted(d.items(),key =operator.itemgetter(0),reverse =True)
print "sictionary in descending order",sd
