#take data from DB

import pymongo
import pandas as pd 

url="mongodb://localhost:27017"

client=pymongo.MongoClient(url)
db=client['school']
collection=db['students']
data=list(collection.find())
df=pd.DataFrame(data)
print(df)