def bs(ilist,item):
    first =0
    last = len(ilist)-1
    found = False
    while(first <= last and not found):
        mid = (first +last)//2
        if ilist[mid] == item :
            found = True
        else:
            if item <ilist[mid]
                last = mid -1
            else:
                first = mid +1
    return found


print bs([1,2,3,4,5,6,7,8],6)
print bs([1,3,4,5,6,7,8,9,9,0,11,2,2,222],56)
def ss(dlist,item):
    pos =0
    found = False
    while pos < len(dlist) and not found:
        if dlist[pos]== item:
            found = True

        else:
            pos = pos +1
    return found,pos


print(ss(11,23,45,67,78,89,90,11),23)