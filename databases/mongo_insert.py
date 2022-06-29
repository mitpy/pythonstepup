import pymongo

url="mongodb://localhost:27017"
mongoClient=pymongo.MongoClient(url)
db=mongoClient['mydb']
collection=db['students']
document={"name":"s2"}
result=collection.insert_one(document)
print(result.inserted_id)