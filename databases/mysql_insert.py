import mysql.connector

con=mysql.connector.connect(
    host='localhost',
    user="root",
    password="",
    database="mydb"
)
myCursor=con.cursor()
query='INSERT INTO `students`(`name`, `rno`, `loc`) VALUES ("S2",2,"Delhi")'
myCursor.execute(query)
con.commit()
print(myCursor.rowcount,' inserted')