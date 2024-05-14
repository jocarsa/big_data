import pandas as pd
import multiprocessing

def calculo(entrada):
    for i in range(0, 100000000):
        entrada *= 1.000000000654
    print(entrada)
    return entrada

def calcular_saldo(filas):
    for index, row in filas.iterrows():
        fila = row.to_dict()
        valortemporal = fila['Saldo']
        filas.at[index, 'Saldo'] = calculo(valortemporal)
    return filas

if __name__ == '__main__':
    df = pd.read_excel('usuarios_ficticios.xlsx')
    
    procesos = round(multiprocessing.cpu_count()/2)
    print(f"Número de procesos disponibles: {procesos}")

    filas_por_proceso = len(df) // procesos
    sub_dfs = [df.iloc[i*filas_por_proceso:(i+1)*filas_por_proceso] for i in range(procesos)]

    with multiprocessing.Pool(processes=procesos) as pool:
        resultados = pool.map(calcular_saldo, sub_dfs)
    
    df_final = pd.concat(resultados)

    df_final.to_excel('usuarios_ficticios_resultado.xlsx', index=False)

    print("Cálculo completado y guardado en 'usuarios_ficticios_resultado.xlsx'")
