def osearch(olist,item):
    if len(olist)== 0:
        return False
    else:
        midpoint = len(olist)// 2
        if olist[midpoint] == item:
            return True
        else:
            if item < olist[midpoint]:
                return bs(olist[:midpoint],item)
            else:
                return bs(olist[midpoint+1:],item)



def bs(alist,item):

    first =0
    last = len(alist) -1
    found = False
    while first <=last and not found:
        midpoint = (first +last) //2
        if alist[midpoint] == item:
          found = True
        else:
            if item <alist[midpoint]:
                last = midpoint -1
            else:
                first = midpoint +1


    return found

print(osearch([0,1,3,5,6,7,8,9,10,14],3))
print(osearch([0,1,3,4,5,6,7,8,9,10,14],17))