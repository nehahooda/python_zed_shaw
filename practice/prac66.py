def csort(array1,max):
    m = max +1
    count = [0]*m
    for a in array1:
        count[a]+=1
    i=0
    for a in range(count[a]):
        for c in range(count[a]):
            array1[i]=a


    return array1


print(csort([1,2,3,2,1,2,4,2,3,3,1],4))