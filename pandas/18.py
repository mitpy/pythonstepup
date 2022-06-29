import pandas as pd

df=pd.read_csv('data.csv')
print(df)

df.sort_values(by='Product cost', ascending=False,inplace=True)
print(df)
