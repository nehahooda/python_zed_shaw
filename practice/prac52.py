def m2(x,y):
    if x>y:
        return x
    return y
def m3(x,y,z):
    return m2(x,m2(y,z))
print (m3(3,6,-5))




def st(s):
    uc =0
    lc =0
    for c in s:
        if c.isupper():
            uc+=1
        elif c.islower():
            lc+=1
        else:
            pass
    print("original string",s)
    print("uppercase elements",uc)
    print("lower case,",lc)

st("MY Name is Neha and why do you care")