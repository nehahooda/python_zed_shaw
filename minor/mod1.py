import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv('menu.csv')
plt.figure(figsize =(15,8))
ax = plt.subplot()
ax.scatter(df['Sodium'],df['Calories'])
plt.show()
### For the purposes of this example, we store feature data from our
### dataframe `df`, in the `f1` and `f2` arrays. We combine this into
### a feature matrix `X` before entering it into the algorithm.
f1 = df['Sodium'].values
f2 = df['Calories'].values
f3 = df['Cholesterol'].values
X=np.matrix(zip(f1,f2,f3))
kmeans = KMeans(n_clusters=3).fit(X)

plt.plot(kmeans.labels_)
plt.show()