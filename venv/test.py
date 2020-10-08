import mysql.connector

db = mysql.connector.connect(
    user='Amnyam',
    password='AkM@e!L4$%!',
    host='localhost')
print(db)

mycursor = db.cursor()

mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)
#mycursor.execute("CREATE DATABASE testdb")