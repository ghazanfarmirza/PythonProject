import csv 
import pandas as pd
import numpy as np
import datetime

data = pd.read_csv('Sheet12.csv')

df = pd.DataFrame(data)

df1 = pd.DataFrame(pd.DatetimeIndex(data['Timestamp']).month) 
df2 = pd.DataFrame(pd.DatetimeIndex(data['Timestamp']).year)

frames = [df1,df2]
result = pd.concat((df1,df2),axis=1)
result.columns=['Month','Year']
df['Timestamp'] = result['Month']
df['Year'] = result['Year']
df = df[['Timestamp','Year','Email Address']]
df.columns=['Month','Year','Email Address']
# print(df)

month = input("Enter your month: ") 
year = input("Enter your year: ") 

# print(df)
df3 = df.loc[df['Month'] == int(month)] 

df4 = df3.loc[df3['Year'] == int(year)] 
# print(df4)
# df5 = df4[df4.duplicated(['Email Address'])]
print(df4.groupby(df4.columns.tolist(),as_index=False).size())
# print(df5)
