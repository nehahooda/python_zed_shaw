def sum(nlist):
    if len(nlist)==1:
        return nlist[0]
    else:

        return nlist[0] +sum(nlist[1:])



print(sum([3,5,6,3,4]))