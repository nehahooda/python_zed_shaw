def qsort(dlist):
    qsorthlp(dlist,0,len(dlist)-1)




def qsorthlp(dlist,first,last):
    if first<last:
        split = partition(dlist,first,last)

        qsorthlp(dlist,first,split-1)
        qsorthlp(dlist,split+1,last)



def partition(dlist,first,last):
    pivot = dlist[first]
    left =first+1
    right = last
    done = False

    while not done:
        while left<=right and dlist[left]<=pivot:
            left=left+1


        while dlist[right]>=pivot and right >left:
            right = right-1

        if right<left:
            done =True
        else:
            temp =dlist[left]
            dlist[left]=dlist[right]
            dlist[right]=temp

    temp = dlist[first]
    dlist[first]=dlist[right]
    dlist[right]= temp

    return right


dlist =[3,6,1,8,9,2]
qsort(dlist)
print(dlist)