import sqlite3
connection = sqlite3.connect('basededatos.db')
cursor = connection.cursor()
query = "SELECT * FROM ciudades"
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
connection.close()
