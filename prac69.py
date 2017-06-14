def rlist(dlist):
    total=0
    for elt in dlist:
        if type(elt)==type([]):
            total = total+rlist(elt)
        else:
            total = total + elt
    return total
print(rlist([1,2,[3,4],[5,6]]))