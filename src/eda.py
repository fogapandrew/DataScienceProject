from data_collection import Rawdata

print(Rawdata.head(4))
print("Describe and exploration of data set")
print(Rawdata.describe())

print(Rawdata.info())

print("Number of missing values: ", Rawdata.isnull().sum().sum())
