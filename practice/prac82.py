'''a = [[1,2,3],[4,5,6]]
print(a[0])
print(a[1])
b= a[0]
print b
print a[0][2]
a[0][1]=7
print(a)
print(b)
b[2]=9
print a[0]
print b

a=[[1,2,3,4],[5,6],[7,8,9]]
s=0
for i in range(len(a)):
    for j in range(len(a[i])):
        print (a[i][j])
        s+=a[i][j]

print "sum",s
for row in a:
    for elt in row:
        print elt
'''
n=3
m=4
a=[[0]*m for i in range(n)]
a[0][0]=5
print(a[0][2])


a=[]
for i in range(n):
    a.append([0]*m)
