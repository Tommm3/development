from datetime import datetime
import pandas as pd



df = pd.read_excel('silka.xlsx', skiprows=0, usecols=[0,1,4], nrows=8)
df['new'] = pd.Series([0]*len(df), index=df.index)
df.index+=1


print(df.to_records(index=True))
# print(df)
