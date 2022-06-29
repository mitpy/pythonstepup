import pymongo

url="mongodb://localhost:27017"
mongoClient=pymongo.MongoClient(url)
db=mongoClient['mydb']
collection=db['students']

condition_query={"name":"s4"}
updated_data = { "$set": {"rno":100,"loc":'NEW DELHI'} }
result=collection.update_one(condition_query,updated_data)
print(result.modified_count)