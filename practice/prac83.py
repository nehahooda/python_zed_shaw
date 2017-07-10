a=[[0]*4]*3
b=[[0]*3]*5
c=[[0]*4]*5
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j]= int(raw_input("A>>"))

for i in range(len(b)):
    for j in range(len(b[i])):
        b[i][j] = int(raw_input("B>>"))

for i in range(len(c)):
    for j in range(len(c[i])):
        c[i][j]=0
        for k in range(len(a)):
            c[i][j]= c[i][j]+a[i][k]*b[k][j]

for i in range(c):
    for j in range(len(c[i])):
        print c[i][j]