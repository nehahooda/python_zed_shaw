import pandas as pd
import matplotlib.pyplot as plt


da1 = pd.read_csv('1month.csv')
da = pd.DataFrame(da1)
da =da[::-1]
da.plot(x = 'Date', y = ['Close','Open','Low','High'],grid =True)
plt.show()


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