from flask import Flask,request
from flask_cors import CORS
import pymongo


app=Flask(__name__)
CORS(app)

@app.route('/reg-std',methods=['POST'])
def fnReg():
    try:
        name=request.json["name"]
        rno=request.json["rno"]
        add=request.json["add"]
        document={"name":name,"rno":rno,"address":add}
        url="mongodb+srv://u1:p1@cluster0.6kd7f1b.mongodb.net/?retryWrites=true&w=majority"
        mongoClient=pymongo.MongoClient(url)
        db=mongoClient["school"]
        collection=db["students"]
        res=collection.insert_one(document)
        return {"data":str(res.inserted_id)}
    except Exception as e:
        return {"data":e}
