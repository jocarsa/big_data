import os
import xml.etree.ElementTree as ET
carpeta = "xml"
archivos = os.listdir(carpeta)
for archivo in archivos:
    print(archivo)
    xml = carpeta+"/"+archivo
    arbol = ET.parse(xml)
    raiz = arbol.getroot()
    print(raiz)
