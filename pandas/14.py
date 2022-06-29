import pandas as pd

df=pd.read_json('dataset.json')
print(df)

#print(df.dropna())
#print(df.dropna(axis=1))
print(df.fillna('ss'))