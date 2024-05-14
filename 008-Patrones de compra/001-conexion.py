import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='crm',
    password='crm',
    database='crm'
)

cursor = connection.cursor()

cursor.execute(
    '''
    SELECT
    matriculas.Identificador,
    matriculas.FK_Alumnos_Apellidos_Apellido2_Nombre_FechaDeAlta,
    Ciclos.Ciclo
    FROM matriculas
    LEFT JOIN ciclos
    ON matriculas.FK_Ciclos_Ciclo = Ciclos.Identificador
    ''')

for row in cursor.fetchall():
    id = row[0]
    cliente = row[1]
    producto = row[2]
    print(id,cliente,producto)
    

cursor.close()
connection.close()
