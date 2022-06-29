import pandas as pd;

df=pd.read_csv('data.csv')
print(df)
#new_df=df[df['Product cost']>70000]
new_df=df[(df['Product cost']>70000) &(df['Product cost']<80000 )]
print(new_df)