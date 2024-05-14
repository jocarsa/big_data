import pandas as pd

df = pd.read_excel('usuarios_ficticios.xlsx')

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
