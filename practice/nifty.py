import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('12-13.csv')
data.plot(grid = True)
plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET-NIFTY ADITYA BIRLA IN JUNE 2012 to 2013')
plt.show()
