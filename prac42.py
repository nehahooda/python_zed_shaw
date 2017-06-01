tuplex = (4,6,2,3,1)
print (tuplex)
tuplex = tuplex+(9,)
print (tuplex)
tuplex = tuplex[:5] + (15,20,50) +tuplex[:5]
print(tuplex)