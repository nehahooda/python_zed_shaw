import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#read the dataset provided
data= pd.read_csv('Book1.csv')
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


#cleaning the dataset
data.dropna(axis=0, how='all')
print(data.Date.nunique())
del data['Date']
print(data.Assist.nunique())
del data['Assist']
del data['Calling Party']
del data['DialedNumber']
del data['AnsLogid']
del data['CallID']


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
sns.boxplot(x="Skill", y="DT", data=data)
plt.title("skills for disposition time")
plt.xlabel("SKILLS")
plt.ylabel("DISPOSITION TIME")
plt.grid()
plt.show()



#showing the mean Dispsoition Time according to skills
var = data.groupby('Skill').TT.mean()
var.plot(kind='line',grid=True)


var = data.groupby('Skill').WT.mean()
var.plot(kind='line',grid=True)

var=data.groupby('Skill').HT.mean()
var.plot(kind='line',grid=True)

plt.legend(["TALKTIME", "WAITING TIME","HOLD TIME"])

t= [0,31,32,33,39,41,45,46,48,53,54,58,60]
plt.xlabel("SKILL")
plt.ylabel("MEAN")
plt.title("SKILL VERSUS MEAN TIME ON CALL")
plt.xticks(t)
plt.xlim(xmin=30)
plt.show()


'''
#specific project analysis
print('PROJECT A')
project1 = data[data.Skill == 60]
print(project1.head())

#printing number of calls attended and number of calls abandoned in the project A
print('The Project A has '+ str(pd.value_counts(project1['Disposition'].values)['ANS'])+
      ' Answered calls and '+ str(pd.value_counts(project1['Disposition'].values)['ABAN'])+
      ' Abandoned calls')

#Disposition of calls in project 1
sns.countplot(x='Disposition',data =project1 )
plt.title("Disposition of incoming calls - PROJECT A")
plt.show()

#call records of abandoned calls
print("ABANDONED CALLS RECORD FOR PROJECT A")
aban= project1[project1.Disposition == 'ABAN']
print(aban.head())

#function to separate active and exception calls
def gtcall(x):
    if x < 60:
        return "Exception"
    else:
        return "Active"

aban['call']=aban['DT'].apply(gtcall)
print(aban.head())




#plotting number of exception calls and active calls
print(sns.countplot(x='call',data = aban))
plt.title("Number of exception and active calls for PROJECT A")
plt.show()

#percent of exception and active calls
percent = aban['call'].value_counts()
print(percent)
fig = plt.figure(figsize=(10,5))
plt.axis("equal")
plt.pie(percent, labels=percent.index,autopct="%1.1f%%")
plt.title("Percent of active calls and exceptions that were abandoned for PROJECT A")
plt.show()

