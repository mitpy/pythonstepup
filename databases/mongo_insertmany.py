import pymongo

url="mongodb://localhost:27017"
mongoClient=pymongo.MongoClient(url)
db=mongoClient['mydb']
collection=db['students']
documents=[{"name":"s3","loc":"Hyd"},{"name":"s4","loc":"Pune","rno":1}]
result=collection.insert_many(documents)
print(result.inserted_ids)