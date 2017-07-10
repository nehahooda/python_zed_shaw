print "input numbers to fin their sum and average.input 0 to exit"

count =0
sum =0.0
no =1
while no!=0:
    no=int(input(""))
    sum+=no
    count+=1


if count ==0:
    print"input some number"
else:
    print ("average and sum of numbers",sum/(count-1),sum)

