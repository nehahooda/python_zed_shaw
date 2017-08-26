import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('menu.csv')
### For the purposes of this example, we store feature data from our
### dataframe `df`, in the `f1` and `f2` arrays. We combine this into
### a feature matrix `X` before entering it into the algorithm.
f1 = df['Total Fat'].values
f2 = df['Saturated Fat'].values
f3 = df['Trans Fat'].values
X=np.matrix(zip(f1,f2,f3))
kmeans = KMeans(n_clusters=3).fit(X)
