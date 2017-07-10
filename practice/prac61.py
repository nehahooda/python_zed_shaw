def ssort(nlist):
    for fillslot in range(len(nlist)-1,0,-1):
        maxpos=0
        for location in range(1,fillslot+1):
            if nlist[location]>nlist[maxpos]:
                maxpos = location

            temp = nlist[fillslot]
            nlist[fillslot] = nlist[maxpos]
            nlist[maxpos] = temp




nlist = [14,46,43,27,34,56,7,89,78,90]
ssort(nlist)
print(nlist)