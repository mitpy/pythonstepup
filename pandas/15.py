import pandas as pd 

df=pd.read_json('dataset.json')
print(df)

df.dropna(inplace=True)
print(df)
