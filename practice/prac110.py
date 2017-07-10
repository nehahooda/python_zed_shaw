import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('jun2016tojul2017.csv')
headers = [ 'Date','Open','High', 'Low','Close','Volume']
results = pd.DataFrame(data)
print(results.head())
data2 = data[['Date','Close','High','Low']]
print(data2.head())
data2.plot()
y=data[['High','Close']]

y_mean = [pd.DataFrame.mean(y) for i in results]
print(y_mean)
plt.xlabel('days')
plt.ylabel(' closing VALUES')
plt.title('FINANCE IN JUNE 2016 to 2017')
plt.show()



