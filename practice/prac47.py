n1 =[]
for x in range(1500,2700):
    if (x%7 == 0) and (x%5==0):
        n1.append(str(x))
print(','.join(n1))
