#understanding the dataset and exploratory data analysis
import pandas as pd
dat = pd.read_csv('test.csv')
data = pd.DataFrame(dat)

print("type data\n",type(data))
print("shape of data\n",data.shape)
print("data columns are as follow \n",data.columns)
print("type of data columns \n",type(data.columns))
print("data index \n",data.index)
print("type of data index\n",type(data.index))
print("head of data\n",data.head())
print("tail of data\n",data.tail())
print("slicing from row 10 to 15\n",data[10:15])
print("printing cont14\n",data["cont14"])
print("data count\n",data.count())
print("data describe\n",data.describe())

print("data info\n",data.info())

