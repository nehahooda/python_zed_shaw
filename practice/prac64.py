def msort(nlist):
    print("splitting",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lhalf= nlist[:mid]
        rhalf=nlist[mid:]

        msort(lhalf)
        msort(rhalf)
        i=j=k=0
        while i<len(lhalf) and j<len(rhalf):
            if lhalf[i]<rhalf[j]:
                nlist[k]=lhalf[i]
                i=i+1

            else:
                nlist[k]=rhalf[j]
                j=j+1
            k=k+1

        while i<len(lhalf):
            nlist[k]=lhalf[i]
            i=i+1
            k=k+1

        while j<len(rhalf):
            nlist[k]=rhalf[j]
            j=j+1
            k=k+1
    print("merging",nlist)


nlist =[1,5,67,88,4,55,89,56,0]
msort(nlist)
print(nlist)