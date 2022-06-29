from GoogleNews import GoogleNews 
from newspaper import Article
import pandas as pd

googleNews= GoogleNews(start='01-01-2022', end="31-12-2022")
googleNews.search('Corona')
result=googleNews.result()
df=pd.DataFrame(result)
print(df)
print('Data downloaded into csv file')
df.to_csv('output.csv')