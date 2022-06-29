import pymongo

url="mongodb://localhost:27017"
mongoClient=pymongo.MongoClient(url)
db=mongoClient['mydb']
collection=db['students']
condition_query={"name":"s2"}
result=collection.delete_one(condition_query)
print(result.deleted_count)