import os
import xml.etree.ElementTree as ET
carpeta = "xml"
archivos = os.listdir(carpeta)
for archivo in archivos:
    xml = carpeta+"/"+archivo
    arbol = ET.parse(xml)
    raiz = arbol.getroot()
    for campo in raiz.findall(".//campo"):
        if campo.attrib.get("id") == "Localidad_de_residencia":
            print(campo.text)
