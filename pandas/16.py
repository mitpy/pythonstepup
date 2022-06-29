import pandas as pd;

df=pd.read_json('dataset.json')
print(df)
df.rename(columns={'order_id':'o', 'cust_name':'cn'},inplace=True)
print(df)
