from flask import Flask,request
import mysql.connector
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
@app.route('/std-reg',methods=['POST'])
def fnReg():
    name=request.json['name']
    rno=request.json['rno']
    loc=request.json['loc']
    try:
        con=mysql.connector.connect(
            host='localhost',
            user="root",
            password="",
            database="school"
        )
        myCursor=con.cursor()
        query='INSERT INTO students VALUES ("{}","{}","{}")'.format(name,rno,loc)
        print(query)
        myCursor.execute(query)
        con.commit()
        return str(myCursor.rowcount) + ' inserted'
    except BaseException as error:
        print("Failed to update record into MySQL table {}".format(error))
    finally:
        if con.is_connected():
            myCursor.close()
            con.close()
            print("MySQL connection is closed")

@app.route("/test-query",methods=['POST'])
def fnCheckQuery():
    n=request.args.get('name')
    l=request.args.get('loc')
    return 'Hello this is {} , am from {} '.format(n,l)

@app.route("/test-path/<name>/<loc>",methods=['POST'])
def fnCheckPath(name,loc):
    return 'Hello this is {} , am from {} '.format(name,loc)

@app.route("/test-headers",methods=['PUT'])
def fnCheckHeaders():
    n=request.headers['name']
    l=request.headers['loc']
    return 'Hello this is {} , am from {} '.format(n,l)

@app.route("/test-body",methods=['POST'])
def fnCheckBody():
    n=request.json['name']
    l=request.json['loc']
    return 'Hello this is {} , am from {} '.format(n,l)

if __name__=='__main__':
    app.run()