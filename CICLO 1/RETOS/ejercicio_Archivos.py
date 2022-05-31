
from pprint import pprint #forma de inprimir chevere 


def cargarRostro(docu):
    
    archivo = open(docu)
    rostro =[] # mustra el rostro

    for linea in archivo:
        codigos= (linea.rstrip().split(','))
        linea=[]
        for c in codigos:
            linea.append(c.split('\t'))
        rostro.append(linea)
            
    return rostro


def imprimir_rostro(rostro):
    numero =

x = cargarRostro('C:/Users/Anderson Pedroza/Documents/rostro.txt')
pprint(x)