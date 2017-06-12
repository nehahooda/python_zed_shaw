def shellsort(alist):
  sublistcount = len(alist)//2
  while sublistcount>0:
    for spos in range(sublistcount):
     gap_isort(alist,spos,sublistcount)

     print("after increment os size",sublistcount,"this list id ",nlist)
     sublistcount= sublistcount//2




def gap_isort(nlist,start,gap):
     for i in range(start+gap,len(nlist),gap):
        current_value = nlist[i]
        pos=i
        while pos>= gap and nlist[pos-gap]>current_value:
            nlist[pos]=nlist[pos-gap]
            pos=pos-gap

        nlist[pos]= current_value



nlist= [13,3,2,34,56,78,5,67,45]
shellsort(nlist)
print(nlist)