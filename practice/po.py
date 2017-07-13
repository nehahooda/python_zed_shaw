import pandas as pd
import matplotlib.pyplot as plt


data1 = pd.read_csv('12-13.csv')
data2 = pd.read_csv('13-14.csv')
data3 = pd.read_csv('14-15.csv')




plt.figure(1)
plt.subplot(221)
plt.plot(data1)
plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET-NIFTY ADITYA BIRLA IN 15 JAN 2012 to 1 JAN 2013')
plt.plot(grid = True)

plt.subplot(222)
plt.plot(data2)
plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET-NIFTY ADITYA BIRLA IN 15 JAN 2013 to 1 JAN 2014')
plt.plot(grid = True)

plt.subplot(223)
plt.plot(data3)
plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET-NIFTY ADITYA BIRLA IN 15 JAN 2014 to 1 JAN 2015')
plt.plot(grid = True)


plt.show()