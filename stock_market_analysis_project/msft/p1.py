import pandas as pd

import matplotlib.pyplot as plt

data = pd.read_csv('MSFT.csv')
st = pd.DataFrame(data)
st.plot()

plt.xlabel('DAYS')
plt.ylabel(' CLOSING VALUES')
plt.title('STOCK MARKET IN JUNE 2012 to 2015')
plt.show()

