import pandas as pd
import os

data = pd.read_csv("test.csv", skiprows=4)
data.head()
data2 = pd.read_csv("test12.csv", skiprows=4)
data2.head()
data3 = pd.concat([data, data2], ignore_index=True)
