# pip install mysql-connector

import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="bigdata",
    password="bigdata",
    database="bigdata"
)
cursor = connection.cursor()
query = "SELECT * FROM clientes"
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
connection.close()
