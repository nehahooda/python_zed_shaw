import pandas as pd
import numpy as np
import seaborn as sna
import matplotlib.pylot as plt

data = pd.read_csv('train.csv')
print(data.head())
print(data.shape)
print(data.describe())
data['Age'].fillna(data['Age'].median() , inplace =True)
print(data.describe())
#based on gender
print(sns.countplot(x='Survived',data = data,hue ='Sex'))

#based on age
fig = plt.figure(figsize=(12,9))
plt.hist(  [data[data['Survived']==1]['Age'],data[data['Survived']==0] ['Age']],stacked = True,color =['g','r'],
           bins = 30,label=['Survived','Dead'])
plt.xlabel('Age')
plt.ylabel('Number of passengers')
plt.legend()

#based on fare
fig1 = plt.figure(figsize=(15,7))
plt.hist(  [data[data['Survived']==1]['Fare'],data[data['Survived']==0] ['Fare']],stacked = True,color =['g','r'],
           bins = 50,label=['Survived','Dead'])
plt.xlabel('Fare')
plt.ylabel('Number of passengers')
plt.legend()


#age fare and survival on same scale
plt.figure(figsize =(15,8))
ax = plt.subplot()
ax.scatter(data[data['Survived']==1]['Age'],data[data['Survived']==1]['Fare'],c='green',s=40)
ax.scatter(data[data['Survived']==0]['Age'],data[data['Survived']==0]['Fare'],c='red',s=40)
ax.set_xlabel('Age')
ax.set_ylabel('Fare')


#taking class consider
ax=plt.subplot()
ax.set_ylabel('Average fare')
data.groupby('Pclass').mean()
['Fare'].plot(kind = 'bar' ,figsize = (15,8),ax =ax)

#sire of embarkment
sns.countplot('Survived',data = data,hue = 'Embarked')


sns.pairplot(data)








