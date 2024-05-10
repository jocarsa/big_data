#pip install unidecode
import os
import xml.etree.ElementTree as ET
import sqlite3
import unidecode
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
print(f"Correctos:{round((correctos/(incorrectos+correctos))*100)}%")
print(f"Incorrectos:{round((incorrectos/(incorrectos+correctos))*100)}%")
conexion.commit()
cursor.close()
conexion.close()
