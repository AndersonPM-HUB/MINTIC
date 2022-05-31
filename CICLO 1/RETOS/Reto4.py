""" Reto 4"""
from functools import reduce

def ordenes(rutinaContable : list):
    diccionario ={}
    
    #Suma el total de cada tupla 
    for registro in rutinaContable:
        for item in registro:  
            if type(item) ==tuple: 
                total_tupla= lambda x,y: x* y #funcion con lambda 
                cantidad = item[1]
                precio =  item[2]
                if diccionario.get(registro[0])==None:
                    diccionario[registro[0]]=[]
                diccionario[registro[0]].append(total_tupla(cantidad,precio))
    #suma el total de cada lista   y el incremento de la compra         
    for orden, valores in diccionario.items():
        suma=reduce((lambda x, y: x+y), valores)
        diccionario[orden]=suma
        if diccionario[orden] <= 600000:
            x =diccionario[orden]
            diccionario[orden] =  x + 25000
    

    print('------------------------ Inicio Registro diario ---------------------------------')
    for x , y in diccionario.items():
        print('La factura {} tiene un total en pesos de {:,.2f}'.format(x,y))
    print('-------------------------- Fin Registro diario ----------------------------------')
    
    
    

r =[
    
[1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)], 
[1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
[1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
[1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]
]

print(ordenes(r))