#take data from web

import pandas as pd ;

url="https://en.wikipedia.org/wiki/Sachin_Tendulkar"

df_list=pd.read_html(url)
#print(df_list)
print(len(df_list))
print(df_list[0])