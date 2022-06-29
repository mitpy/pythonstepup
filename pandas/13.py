import pandas as pd 

#df=pd.read_csv('data.csv')
#print(df)
#print(df.head())
#print(df.head(10))
#print(df.tail())
#print(df.tail(10))
#print(df.shape)
#print(df.columns)
#print(df.describe())
#print(df['Customer name'])
#print(df[['Order id','Customer name','Customer id']])


#print(df.iloc[10:15,1:4])
#print(df.iloc[1,3])

df1=pd.read_csv('data.csv',index_col='Customer name')
print(df1)
print(df1.iloc[1:10,0:2])
print(df1.loc['Partha'])
print(df1.loc[['Partha','Neelima']])



