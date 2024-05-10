import os
import xml.etree.ElementTree as ET
import sqlite3
conexion = sqlite3.connect('basededatos.db')
cursor = connection.cursor()
carpeta = "xml"
archivos = os.listdir(carpeta)
for archivo in archivos:
    xml = carpeta+"/"+archivo
    arbol = ET.parse(xml)
    raiz = arbol.getroot()
    for campo in raiz.findall(".//campo"):
        if campo.attrib.get("id") == "Localidad_de_residencia":
            query = "INSERT INTO ciudades VALUES ('"+campo.text+"')"
            cursor.execute(query)
conexion.commit()
cursor.close()
conexion.close()
