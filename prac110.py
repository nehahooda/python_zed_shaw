import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('goog.csv')
headers = [ 'Date','Open','High', 'Low','Close','Volume']
results = pd.DataFrame(data)
print(results.head())
data2 = data[['Date','Close']]
print(data2.head())
data2.plot()
plt.xlabel('days')
plt.ylabel(' closing VALUES')
plt.title('FINANCE IN JUNE 2016 to 2017')
plt.show()



