import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#read the dataset provided
data= pd.read_csv('dataset.csv')
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

#removing user name as it doesnt help anywhere
del data['username']
del data['time']
del data['date']


# Moving on to the activity column
print('Dataset contains ' + str(pd.value_counts(data['activity'].values)[0]) + ' "walk" data samples as well as ' + str(pd.value_counts(data['activity'].values)[1]) + ' "run" data samples')

unique_a = set(data['activity'].values)
a_popularity = data['activity'].value_counts()
print(a_popularity)
f = plt.figure(figsize=(10,5))
sns.barplot(a_popularity.index, a_popularity.values, alpha=0.7)
plt.xlabel('Activity', fontsize=14)
plt.ylabel('Count of Activities', fontsize=14)
plt.title('Activity 0 (WALK) and Activity 1(RUN) count')
plt.show()


# Moving on to the wrist column
print('The dataset contains ' + str(pd.value_counts(data['wrist'].values)[0]) + ' data samples collected on the left wrist as well as ' + str(pd.value_counts(data['wrist'].values)[1]) + ' data samples collected on the right wrist')
unique_w = set(data['wrist'].values)
w_popularity = data['wrist'].value_counts()

f = plt.figure(figsize=(10,5))
sns.barplot(w_popularity.index, w_popularity.values, alpha=0.7)
plt.xlabel('Wrist', fontsize=14)
plt.ylabel('Count of Events', fontsize=14)
plt.title('Wrist 0(LEFT) or 1(RIGHT) count')
plt.show()



SENSOR_DATA_COLUMNS = ['acceleration_x', 'acceleration_y', 'acceleration_z', 'gyro_x', 'gyro_y', 'gyro_z']

# populate dataframe with 'left' wrist only
df_left_wrist_data = pd.DataFrame()
df_left_wrist_data = data[data.wrist == 0]

# populate dataframe with 'right' wrist only
df_right_wrist_data = pd.DataFrame()
df_right_wrist_data = data[data.wrist == 1]

#plotting against acceleration and gyrometer
for c in SENSOR_DATA_COLUMNS:
    plt.figure(figsize=(10,5))
    plt.title("Sensor data distribution for both wrists")
    sns.distplot(df_left_wrist_data[c], label='left')
    sns.distplot(df_right_wrist_data[c], label='right')
    plt.legend()
    plt.show()