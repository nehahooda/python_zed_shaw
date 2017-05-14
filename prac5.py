a ='nehahooda'
num =int(input("please chosse a number to divide:"))
listrange = list(range(1,num+1))
divisorList =[]
for number in listrange:
    if num%number ==0:
        divisorList.append(number)

print(divisorList)