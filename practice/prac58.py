def ss(dlist,item):
    pos =0
    found = False
    while pos < len(dlist) and not found:
        if dlist[pos]== item:
            found = True

        else:
            pos = pos +1
    return found,pos


print(ss([11,23,45,67,78,89,90,11],23))