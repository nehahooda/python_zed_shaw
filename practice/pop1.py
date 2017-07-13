import pandas as pd
import matplotlib.pyplot as plt


data1 = pd.read_csv('12-13.csv')
results1 = pd.DataFrame(data1)
results1['num_days'] = results1['Date']

headers1 = [ 'num_days','Close']



results11 = pd.DataFrame(results1[headers1])
print(results11.head())
results11.plot(grid = True)
plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET IN JUNE 2012 to 2013')
plt.show()