def fn(x):
    y=[]
    for i in x:
        if i not in y:
            y.append(i)
    return y


def dupe(x):
    return list(set(x))


a= [1,2,3,4,3,2,1]
print fn(a)
print dupe(a)


