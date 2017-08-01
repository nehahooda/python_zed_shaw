
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data= pd.read_csv('train.csv')
'''print(data.head())
print(data.shape)
print(data.describe())
'''

#showing unique id
print(data.id.nunique())
print(data.shape)

#removing passengers with count greater than 6
tf = data[(data.passenger_count >=1)&(data.passenger_count <=6) ]
print(tf.id.nunique())
print(tf.shape)
#removing rides with same pickup and drop point
tf =tf[(tf.pickup_latitude != tf.dropoff_latitude) & ( tf.pickup_longitude != tf.dropoff_longitude)]
print(tf.id.nunique())
print(tf.shape)

tf=tf.head(100)
mt=tf.vendor_id.groupby(tf.vendor_id).sum()

plt.figure(figsize=(16,8))
# plot chart
ax1 = plt.subplot(121, aspect='equal')
tf.plot(kind='pie', y = 'vendor_id', ax=ax1, autopct='%1.1f%%',
 startangle=90, shadow=False, labels=tf['vendor_id'], legend = False, fontsize=14)

plt.show()

#displaying trips on map
sns.swarmplot(x='pickup_latitude',y='pickup_longitude',data= tf)
tf.plot(x='vendor_id',y='trip_duration',grid=True)
plt.plot([tf['pickup_latitude'], tf['dropoff_latitude']], [tf['pickup_longitude'], tf['dropoff_longitude']])
plt.grid()
plt.xlabel("latitude")
plt.ylabel("longitude")
plt.title("Trips location points")
plt.show()

#considering number of passengers and vendor id
sns.countplot(x='passenger_count',data =tf,hue='vendor_id')
plt.show()


#considering number of passengers with the store and forward flag was used
sns.countplot(x='passenger_count',data =tf,hue='store_and_fwd_flag')
plt.show()
def getnum(x):
    if x in ['N']:
        return 0
    else:
        return 1

tf['snfno']=tf['store_and_fwd_flag'].apply(getnum)
print(tf.head())
sns.countplot(x='passenger_count',data =tf,hue='snfno')
plt.show()


#finding median by number of passengers
mt=tf.groupby('passenger_count',as_index=False)['trip_duration'].median()
mt['tdm']=mt['trip_duration']
del mt['trip_duration']

print(mt)

sns.swarmplot(x='passenger_count',y='tdm',data =mt)
plt.title("median trip duration for number of passenger")
plt.xlabel("number of passengers")
plt.ylabel("Median of Trip duration")
plt.grid()
plt.show()

