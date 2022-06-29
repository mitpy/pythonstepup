import mysql.connector
try:
    con=mysql.connector.connect(
        host='localhost',
        user="root",
        password="",
        database="mydb"
    )
    myCursor=con.cursor()
    query='INSERT INTO `students`(`name`, `rno`, `loc`) VALUES (%s,%s,%s)'
    data=[
        ('s3','3','Hyd'),
        ('s4','4','VSKP')
    ]
    myCursor.executemany(query,data)
    con.commit()
    print(myCursor.rowcount,' inserted')
except BaseException as error:
    print("Failed to insert record into MySQL table {}".format(error))
finally:
    if con.is_connected():
        myCursor.close()
        con.close()
        print("MySQL connection is closed")