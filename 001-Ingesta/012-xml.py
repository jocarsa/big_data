import xml.etree.ElementTree as ET
file_path = "clientes.xml"
tree = ET.parse(file_path)
root = tree.getroot()
for person in root.findall('cliente'):
    nombre = person.find('nombre').text
    apellidos = person.find('apellidos').text
    correo = person.find('email').text
    print(f"Nombre: {nombre}, Apellidos: {apellidos}, Correo: {correo}")
