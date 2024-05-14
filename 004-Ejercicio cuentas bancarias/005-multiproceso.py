import pandas as pd
import multiprocessing

def calculo(entrada):
    for i in range(0,100000000):
        entrada *= 1.000000000654
    return entrada
    

if __name__ == '__main__':
    procesos = multiprocessing.cpu_count()
    print(procesos)
    filas = 100000
    filas_por_proceso = filas/procesos
    piscina = multiprocessing.Pool(processes=procesos)
    
    
    

df = pd.read_excel('usuarios_ficticios.xlsx')


for index, row in df.iterrows():
    #print(f"Row {index}: {row.to_dict()}")
    fila = row.to_dict()
    #print(fila['Saldo'])
    valortemporal = fila['Saldo']
    valortemporal = calculo(valortemporal)
    print(index,valortemporal)

