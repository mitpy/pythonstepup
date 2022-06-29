import mysql.connector
try:
    con=mysql.connector.connect(
        host='localhost',
        user="root",
        password="",
        database="mydb"
    )
    
    myCursor=con.cursor()
    query='SELECT * FROM `students`'
   
    myCursor.execute(query)
    rows=myCursor.fetchall()
    for row in rows:
        print(row)
except BaseException as error:
    print("Failed to fetch record into MySQL table {}".format(error))
finally:
    if con.is_connected():
        myCursor.close()
        con.close()
        print("MySQL connection is closed")