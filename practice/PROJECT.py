import pandas as pd
import matplotlib.pyplot as plt


'''#DATA FOR 2014 TO 2015
data1 = pd.read_csv('jun2014-jul2015.csv')
headers1 = [ 'Date','Open','High', 'Low','Close','Volume']
results1 = pd.DataFrame(data1)
print(results1.head())
results1['Average']= (results1['High'] + results1['Low'])/2
data12 = data1[['Date','Close','High','Average']]
avg = data12["Close"].mean()

data12.plot(grid = True).axhline(y = avg,color = "black",lw= 2)

plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET IN JUNE 2014 to 2015')
plt.show()



#DATA FOR 2015 TO 2016
data2 = pd.read_csv('jun2015-jul2016.csv')
headers2 = [ 'Date','Open','High', 'Low','Close','Volume']
results2 = pd.DataFrame(data2)
print(results2.head())
results2['Average']= (results2['High'] + results2['Low'])/2
data22 = data2[['Date','Close','High','Average']]
avg = data22["Close"].mean()

data22.plot(grid = True).axhline(y = avg,color = "black",lw=2)
plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET IN JUNE 2015 to 2016')
plt.show()



#DATA FOR 2016 TO 2017
data3 = pd.read_csv('jun2016tojul2017.csv')
headers3 = [ 'Date','Open','High', 'Low','Close','Volume']
results3 = pd.DataFrame(data3)
print(results3.head())
results3['Average']= (results3['High'] + results3['Low'])/2
data32 = data3[['Date','Close','High','Average']]

avg = data32["Close"].mean()
data32.plot(grid = True).axhline(y = avg,color= "black",lw =2)
plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET IN JUNE 2016 to 2017')
plt.show()

'''
#DATA FOR 2014 TO 2017
data4 = pd.read_csv('JUN2014-2017.csv')
headers4 = [ 'Date','Open','High', 'Low','Close','Volume']

results4 = pd.DataFrame(data4)
print(results4.head())
results4['Average']= (results4['High'] + results4['Low'])/2
print("THE DAYS WHEN THE CLOSING POINT WAS HIGHER THAN AVERAGE")
print(data4[data4['Close'] > data4['Average']])
data42 = data4[['Date','Close','High','Average']]
avg = data42["Close"].mean()

data42.plot(grid = True).axhline(y= avg,color = "black",lw =2)

print(data4[data4.max()])

plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET IN JUNE 2014 to 2017')
plt.show()










