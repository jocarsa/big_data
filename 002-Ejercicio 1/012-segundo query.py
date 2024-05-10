#pip install unidecode
import os
import xml.etree.ElementTree as ET
import sqlite3
import unidecode
import matplotlib.pyplot as plt
conexion = sqlite3.connect('basededatos.db')
cursor = conexion.cursor()
carpeta = "xml"
archivos = os.listdir(carpeta)
peticion = "DELETE FROM ciudades;"
cursor.execute(peticion)
correctos = 0
incorrectos = 0
for archivo in archivos:
    try:
        xml = carpeta+"/"+archivo
        arbol = ET.parse(xml)
        raiz = arbol.getroot()
        for campo in raiz.findall(".//campo"):
            if campo.attrib.get("id") == "Localidad_de_residencia":
                texto = campo.text
                texto = texto.lower()
                texto = unidecode.unidecode(texto)
                texto = texto.strip()
                peticion = "INSERT INTO ciudades VALUES ('"+texto+"')"
                cursor.execute(peticion)
        correctos += 1
    except:
        incorrectos += 1
conexion.commit()
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
datos = [correctos,incorrectos]
etiquetas = ['correctos','incorrectos']
axs[0].pie(datos, labels=etiquetas, autopct='%1.1f%%', startangle=90)
axs[0].set_title('Validez de los datos')
ciudades = []
numeros = []
peticion = '''
SELECT 
ciudad,
COUNT(*) AS numero 
FROM ciudades 
GROUP BY ciudad
ORDER BY numero DESC
LIMIT 20
'''
cursor.execute(peticion)
filas = cursor.fetchall()
for fila in filas:
    ciudades.append(fila[0])
    numeros.append(fila[1])
axs[1].pie(numeros, labels=ciudades, autopct='%1.1f%%', startangle=90)
axs[1].set_title('Ciudades')
axs[0].axis('equal')
axs[1].axis('equal')
plt.tight_layout()
plt.show()

cursor.close()
conexion.close()
