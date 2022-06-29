import pymongo
print('start')
try:
    url='mongodb://localhost:27017'
    mongoClient=pymongo.MongoClient(url)
    db=mongoClient['mydb']
    collection=db['students']
    documents=collection.find()
    for doc in documents:
        print(doc)
except:
    print('Exception raised')
print('End')