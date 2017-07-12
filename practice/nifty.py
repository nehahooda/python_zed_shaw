import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('12-13.csv')
data.plot(grid = True)
plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET-NIFTY ADITYA BIRLA IN 15 JAN 2012 to 1 JAN 2013')
plt.show()


data = pd.read_csv('13-14.csv')
data.plot(grid = True)
plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET-NIFTY ADITYA BIRLA IN 15 JAN 2013 to 1 JAN 2014')
plt.show()


data = pd.read_csv('14-15.csv')
data.plot(grid = True)
plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET-NIFTY ADITYA BIRLA IN 15 JAN 2014 to 1 JAN 2015')
plt.show()

data = pd.read_csv('15-16.csv')
data.plot(grid = True)
plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET-NIFTY ADITYA BIRLA IN 15 JAN 2015 to 1 JAN 2016')
plt.show()

data = pd.read_csv('16-17.csv')
data.plot(grid = True)
plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET-NIFTY ADITYA BIRLA IN 15 JAN 2016 to 1 JAN 2017')
plt.show()
