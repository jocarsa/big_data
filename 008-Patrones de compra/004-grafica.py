import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='crm',
    password='crm',
    database='crm'
)

cursor = connection.cursor()
cursor2 = connection.cursor()
cursor.execute(
    '''
    SELECT
    matriculas.Identificador,
    matriculas.FK_Alumnos_Apellidos_Apellido2_Nombre_FechaDeAlta,
    Ciclos.Ciclo
    FROM matriculas
    LEFT JOIN ciclos
    ON matriculas.FK_Ciclos_Ciclo = Ciclos.Identificador
    WHERE Ciclos.Ciclo = 'AC'
    ''')
ciclos = {}

for row in cursor.fetchall():
    try:
        id = row[0]
        cliente = row[1]
        producto = row[2]
        #print(id,cliente,producto)
        cursor2.execute(
        '''
        SELECT
        matriculas.Identificador,
        matriculas.FK_Alumnos_Apellidos_Apellido2_Nombre_FechaDeAlta,
        Ciclos.Ciclo
        FROM matriculas
        LEFT JOIN ciclos
        ON matriculas.FK_Ciclos_Ciclo = Ciclos.Identificador
        WHERE matriculas.identificador > '''+str(id)+'''
        AND
        matriculas.FK_Alumnos_Apellidos_Apellido2_Nombre_FechaDeAlta = "'''+str(cliente)+'''"
        AND Ciclos.Ciclo != "'''+producto+'''"
        
        ''')
        for row2 in cursor2.fetchall():
            print("El alumno que primero compró "+producto+" luego ha comprado "+str(row2[2]))
            if row2[2] in ciclos:
                ciclos[row2[2]] += 1
            else:
                ciclos[row2[2]] = 0

    except:
        pass
    
print(ciclos)
cursor.close()
connection.close()
