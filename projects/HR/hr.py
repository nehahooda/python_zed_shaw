import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#read the dataset provided
data= pd.read_csv('HR.csv')
print("Total number of samples in file : ", data.shape[0])

# Let's look at the data first
print("A view of the  dataframe")
print(data.head())
print("\nColumns in  dataset : ", data.columns)
print("\n")
print("Overall description of the dataset : ")
print(data.info())
print("Overall numerical description of the data set")
print(data.describe())

print(data.StandardHours.nunique())#all 3 have same value for the all ids hence useless for analysis
print(data.EmployeeCount.nunique())
print(data.Over18.nunique())
del data['StandardHours']
del data['EmployeeCount']
del data['Over18']
print(pd.value_counts(data['YearsAtCompany'].values)[0]) #new joinees


print(data.Department.nunique()) #unique departments-3
print(data.PerformanceRating.nunique())#shows only 2 values 3 and 4 hence we cant trust the coloumn

print('Dataset contains ' + str(pd.value_counts(data['Gender'].values)['Male']) + ' male  employees and ' + str(pd.value_counts(data['Gender'].values)['Female']) + ' female candidate')
#gender wise view
gend = data['Gender'].value_counts()
print(gend)
f = plt.figure(figsize=(10,5))
sns.barplot(gend.index, gend.values, alpha=0.7)
plt.xlabel('Gender', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.title('Gender count of the company')
plt.show()


#deparment wise view
dept = data['Department'].value_counts()
print(dept)
f = plt.figure(figsize=(10,5))
plt.axis("equal")
plt.pie(dept, labels=dept.index,autopct="%1.1f%%")
plt.title("Departments in the company")
plt.show()

#Age in the Company
fig=plt.figure()
ax = fig.add_subplot(1,1,1)
ax.boxplot(data['Age'])
plt.show()
#relating age and the gender
sns.violinplot(data['Gender'], data['Age'])
sns.despine()
plt.show()


#relating job satisfaction and gender
var = data.groupby(['JobSatisfaction','Gender']).HourlyRate.sum()
var.unstack().plot(kind='bar',stacked=True,  color=['red','blue'], grid=False)
plt.show()


#look at the years in the company and their hourly rate
var = data.groupby('YearsAtCompany').HourlyRate.mean()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('Years at Company')
ax1.set_ylabel('Hourly rate')
ax1.set_title("Years at company wise Mean of Hourly rates")
var.plot(kind='line',grid=True)
plt.show()
