import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#read the dataset provided
data= pd.read_csv('Call.csv')
'''print("Total number of samples in file : ", data.shape[0])
# Let's look at the data first
print("A view of the  dataframe")
print(data.head())
print("\nColumns in  dataset : ", data.columns)
print("\n")
print("Overall description of the dataset : ")
print(data.info())
print("Overall numerical description of the data set")
print(data.describe())
'''

#cleaning the dataset
print(data.Date.nunique())
del data['Date']
print(data.Assist.nunique())
del data['Assist']
del data['LastCallWorkCode']



'''
#disposition plotting-what action was taken for the incoming calls
sns.countplot(x='Disposition',data =data )
plt.title("Disposition of incoming calls")
plt.show()

#segment wise report
seg = data['Segment'].value_counts()
print(seg)
f = plt.figure(figsize=(10,5))
plt.axis("equal")
plt.pie(seg, labels=seg.index,autopct="%1.1f%%")
plt.title("Segment wise calls")
plt.show()

#showing the count of calls as per skills
sns.countplot(x='Skill',data =data )
plt.title("number of calls as per skills")
plt.show()

#showing the calls that were transfered out
sns.countplot(x='TransferedOut',data =data )
plt.title("Transferred out calls")
plt.show()
#showing calls that were conferenced in
sns.countplot(x='ConferencedIn',data =data )
plt.title("conferenced  In calls")
plt.show()



#looking at the disposition time wise skill
sns.swarmplot(x='DispositionTime',y='Skill',data =data)

plt.title("skills for disposition time")
plt.xlabel("Disposition TIME")
plt.ylabel("SKILLS")
plt.grid()
plt.show()




#
sns.swarmplot(x="TalkTime", y="Skill", data=data)
plt.show()
'''
