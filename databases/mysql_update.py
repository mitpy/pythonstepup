import mysql.connector
try:
    con=mysql.connector.connect(
        host='localhost',
        user="root",
        password="",
        database="mydb"
    )
    myCursor=con.cursor()
    query='UPDATE `students` SET `rno`=100,`loc`="SKLM" WHERE name="S1" '
   
    myCursor.execute(query)
    con.commit()
    print(myCursor.rowcount,' updated')
except BaseException as error:
    print("Failed to update record into MySQL table {}".format(error))
finally:
    if con.is_connected():
        myCursor.close()
        con.close()
        print("MySQL connection is closed")