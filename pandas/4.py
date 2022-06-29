#DataFrame

import pandas as pd

data=[['Sachin',20000],['Dhoni',10000],['Kohli',3000]]
df=pd.DataFrame(data,columns=['Name','Runs'])
print(df)