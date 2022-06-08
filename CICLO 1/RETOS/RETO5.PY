
import pandas as pd
def listaPeliculas(rutaFileCsv: str) -> str:
    #validar extension 
    if '.csv' in rutaFileCsv:
        try: 
            archivo = pd.read_csv(rutaFileCsv)
            subconjunto = archivo[["Country", "Language","Gross Earnings"]]
            tabla_resumen = pd.pivot_table(subconjunto,index= ["Country", "Language"] ).head(10)
            print(tabla_resumen)
        except:
            print('Error al leer el archivo de datos.')
    else:
        print('Extensión  inválida.')

rutaFileCsv='rostro.txt'    
print(listaPeliculas(rutaFileCsv))

