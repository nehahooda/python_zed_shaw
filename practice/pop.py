import pandas as pd
import matplotlib.pyplot as plt


data1 = pd.read_csv('12-13.csv')
results1 = pd.DataFrame(data1)


data2 = pd.read_csv('13-14.csv')
results2 = pd.DataFrame(data2)
results1.concat(results2)

data3 = pd.read_csv('14-15.csv')
results3 = pd.DataFrame(data3)
t= results2.concat(results3)

results3.plot(grid = True)
plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET IN JUNE 2012 to 2015')
plt.show()