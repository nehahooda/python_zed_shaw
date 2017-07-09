import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

headers = [ 'Date','Open','High', 'Low','Close','Volume']
data = pd.read_csv('goog.csv',names = headers)

data2 = data[['Date','Close']]
print(data2.head())
data2.plot()
plt.show()
'''
x= data['Date']
y = data['Close']


plt.plot(x,y)
plt.gcf().autofmt_xdate()

plt.xlabel('DATE')
plt.ylabel('CLOSING')
plt.title('FINANCE OVER JUNE 2016 TO JUNE2017')
plt.show()
'''