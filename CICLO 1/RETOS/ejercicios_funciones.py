from functools import reduce
#Map : transforma valores de un iterable en todos los elementos de iterable
numeros=[0,1,2,3,4,5]

cuadrado = list(map(lambda x : pow(x,2), numeros))
print(cuadrado)

nombres =['anderson', 'diana', 'lucas', 'juan']
conteo= list(map(lambda x : x +':' + str(len(x)),nombres))
print(conteo)

# Filter : devuelve los que cumplan con el filtro v o f, fucnion 

mayor = list(filter(lambda x : x < 3 , numeros))
print(mayor)

par = list(filter(lambda x : x%2 == 0 , numeros))
print(par)

buscar= list(filter(lambda x : (len(x))>5 ,nombres))
print(buscar)

# REDUCE: reducir los elementos 

suma = reduce(lambda x, y : x + y , numeros)
print(suma)
            