import mysql.connector
import json

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
    FLOOR(DATEDIFF(CURDATE(), Fecha_de_Nacimiento) / 365.25) - 		FLOOR(DATEDIFF(CURDATE(), Fecha_de_Alta) / 365.25) AS x,
    AVG(introduccionnotas.FK_Notas_Nota) AS y
FROM 
    alumnos
    LEFT JOIN introduccionnotas 
    ON alumnos.Identificador = introduccionnotas.FK_Alumnos_Apellidos_Nombre

WHERE 
    FLOOR(DATEDIFF(CURDATE(), Fecha_de_Nacimiento) / 365.25) IS NOT NULL
    AND 
    FLOOR(DATEDIFF(CURDATE(), Fecha_de_Alta) / 365.25) IS NOT NULL
    AND
    introduccionnotas.FK_Notas_Nota < 12
GROUP BY alumnos.Identificador
    ;
    ''')

lista = []

for row in cursor.fetchall():
    lista.append(row)

json_data = [{'x': x, 'y': y} for x, y in lista]
json_string = json.dumps(json_data, indent=4)
archivo = open("datos.json",'w')
archivo.write(json_string)
archivo.close()
