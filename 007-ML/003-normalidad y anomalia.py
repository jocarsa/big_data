import pandas as pd

def get_max_index(arr):
    if not arr:  # Check if the list is empty
        return None
    
    max_val = max(arr)
    return arr.index(max_val)

df = pd.read_excel('usuarios_ficticios.xlsx')
# primero buscamos la normalidad
caracteres = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(caracteres)
for index, row in df.iterrows():
    fila = row.to_dict()
    saldo = fila['Saldo']
    redondeo = round(saldo)
    cadena = str(redondeo)
    longitud = len(cadena)
    #print(longitud)
    caracteres[longitud] += 1
print(caracteres)
maximo = get_max_index(caracteres)
print("maximo:",maximo)
# ahora buscamos lo que se sale de la normalidad
df = pd.read_excel('usuarios_ficticios.xlsx')
for index, row in df.iterrows():
    fila = row.to_dict()
    saldo = fila['Saldo']
    redondeo = round(saldo)
    cadena = str(redondeo)
    longitud = len(cadena)
    if longitud < maximo - 1 or longitud > maximo + 1:
        print("Anomalia:",index,fila['Nombre'],fila['Apellidos'],fila['Saldo'])
