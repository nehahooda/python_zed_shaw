import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#read the dataset providedn
data= pd.read_csv('all.csv')
print("Total number of samples in file : ", data.shape[0])

# Let's look at the data first
print("A view of the  dataframe")
print(data.head())
print("\nColumns in  dataset : ", data.columns)
print("\n")
print("Overall description of the dataset : ")
print(data.info())
print("Overall numerical description of the data set")
print(data.describe())