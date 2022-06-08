import pandas as pd

#manipula datos PANDAS 
diccionario={
    'nombres': ['anderson', 'lady', 'jlo'],
    'apellidos': ['pedroza', 'Gaga', 'lopez'],
    'edad': [23, 33, 50],
    'carrara': ['ingeniero', 'cantante', 'cantante'], 
}
#usar dataframe
df1 = pd.DataFrame(diccionario)
print(df1, '\n')

#convertir a csv  o a un excel con separacion funciona o relaciona con un diccionario
df1.to_csv('ejemplocsv.csv')#mas parametros para la manipulacion de datos

#leer archivo y convertir en dataframe
pd.options.display.max_rows =2000
df2 = pd.read_csv('C:/Users/Anderson Pedroza/Documents/GitHub/MINTIC/CICLO 1/PRACTICAS/CasosCovid.csv')
print(df2)
# a la hora de leer un archivo largo saco un formato 
#print(df2.to_string())#imprimir todo el contenido 

df3=pd.read_csv('ejemplocsv.csv')
print(df3)
print(df2.head)