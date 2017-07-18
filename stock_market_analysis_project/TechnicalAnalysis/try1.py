import pandas as pd
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go




da1 = pd.read_csv('1month.csv')
da = pd.DataFrame(da1)
print(da1['Close'].count())
da =da[::-1]

trace = go.Candlestick(x=da.index,
                       open=da.Open,
                       high=da.High,
                       low=da.Low,
                       close=da.Close)
data = [trace]
plt.show(data)


da2 = pd.read_csv('3months.csv')
da = pd.DataFrame(da2)
da =da[::-1]
da.plot(x = 'Date', y = ['Close','Open','Low','High'],grid=True)
plt.show()

da3 = pd.read_csv('1year.csv')
da = pd.DataFrame(da3)
da =da[::-1]
da.plot(x = 'Date', y = ['Close','Open','Low','High'],grid =True)
plt.show()