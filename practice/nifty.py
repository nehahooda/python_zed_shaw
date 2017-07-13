import pandas as pd
import matplotlib.pyplot as plt


data1 = pd.read_csv('12-13.csv')
data1.plot(grid = True)
plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET-NIFTY ADITYA BIRLA IN 15 JAN 2012 to 1 JAN 2013')
plt.show()


data2 = pd.read_csv('13-14.csv')
data2.plot(grid = True)
plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET-NIFTY ADITYA BIRLA IN 15 JAN 2013 to 1 JAN 2014')
plt.show()


data3 = pd.read_csv('14-15.csv')
data3.plot(grid = True)
plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET-NIFTY ADITYA BIRLA IN 15 JAN 2014 to 1 JAN 2015')
plt.show()

data4 = pd.read_csv('15-16.csv')
data4.plot(grid = True)
plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET-NIFTY ADITYA BIRLA IN 15 JAN 2015 to 1 JAN 2016')
plt.show()

data5 = pd.read_csv('16-17.csv')
data5.plot(grid = True)
plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET-NIFTY ADITYA BIRLA IN 15 JAN 2016 to 1 JAN 2017')
plt.show()

fig = plt.figure()

y1=fig.add_subplot(211)
y1.plot(data1)
y2=fig.add_subplot(212)
y2.plot(data2)

plt.show()
