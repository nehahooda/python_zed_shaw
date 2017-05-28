a = [1,2,3,4,5,4,3,2,3,4,5,6,7,8,7,8,9,6,7,5,7,4,5,4,4,2,3,1]
dp =set()
ui =[]
for x in a:
    if x not in dp:
        ui.append(x)
        dp.add(x)
print(dp)