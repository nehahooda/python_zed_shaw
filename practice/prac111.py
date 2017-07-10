import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')
data.plot()

plt.xlabel('TIME')
plt.ylabel('VALUES')
plt.title('FINANCE OVER 2014')
plt.show()