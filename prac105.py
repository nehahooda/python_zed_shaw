import pandas as pd
cities=['Austin','Dallas','Austin','Dallas']
signups = [7,12,3,5]
visitors = [139,237,324,566]
weedays=['Sun','Sun','Mon','Mon']
list_labels=['city','Signups','vistors','Weedays']
list_cols=[cities,signups,visitors,weedays]
zipped = list(zip(list_labels,list_cols))

print(zipped)
data =dict(zipped)

users=pd.DataFrame(data)
print(users)
users['fees']=0
print(users)
