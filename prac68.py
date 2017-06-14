def tostring(n,base):
    convertstring ="0123456789ABCDEF"
    if n< base:
        return convertstring[n]
    else:
        return tostring(n//base,base) + convertstring[n% base]


print(tostring(2835,16))