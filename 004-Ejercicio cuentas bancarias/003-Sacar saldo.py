import pandas as pd

df = pd.read_excel('usuarios_ficticios.xlsx')

for index, row in df.iterrows():
    #print(f"Row {index}: {row.to_dict()}")
    fila = row.to_dict()
    print(fila['Saldo'])

