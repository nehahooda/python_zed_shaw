def isort(nlist):
    for index in range(1,len(nlist)):
        cvalue = nlist[index]
        position = index
        while position > 0 and nlist[position-1]>cvalue:
            nlist[position] = nlist[position -1]
            position = position -1
        nlist[position] = cvalue
nlist = [1,36,4,20,63,21,5,3,45,34,8]
isort(nlist)
print(nlist)