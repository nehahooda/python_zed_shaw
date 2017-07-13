import pandas as pd
import matplotlib.pyplot as plt


data1 = pd.read_csv('12-13.csv')    #year 2012

headers1 = [ 'Date','Close']
results1 = pd.DataFrame(data1)
print(results1.head())
results1.plot(grid = True)

plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET IN JAN 2012 to 2013')
plt.show()




data2 = pd.read_csv('13-14.csv')        #year 2013

headers2 = [ 'Date','Close']
results2 = pd.DataFrame(data1)
print(results2.head())
results2.plot(grid = True)

plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET IN JAN 2013 to 2014')
plt.show()

t = results1.concat([results2,results1],axis1 =0)         #trying to concatenate them and plot for 2012 to 2014
print(t.head())
t.plot(grid = True)

plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET IN JAN 2012 to 2014')
plt.show()







