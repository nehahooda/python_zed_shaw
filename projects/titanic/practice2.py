import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
titanic_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")
print(titanic_df.head())
print(test_df.head())
print (titanic_df.shape,test_df.shape)
def get_title(name):
    if '.' in name:
        return name.split(',')[1].split('.')[0].strip()
    else:
        return 'Unknown'

def title_map(title):
    if title in ['Mr']:
        return 1
    elif title in ['Master']:
        return 3
    elif title in ['Ms','Mlle','Miss']:
        return 4
    elif title in ['Mme','Mrs']:
        return 5
    else:
        return 2
titanic_df['title'] = titanic_df['Name'].apply(get_title).apply(title_map)
test_df['title'] = test_df['Name'].apply(get_title).apply(title_map)
print(titanic_df.head())

print(test_df.head())
