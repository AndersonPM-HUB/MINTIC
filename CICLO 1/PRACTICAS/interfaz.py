
import easygui as v
from Reto1 import CDT


lista=['Nombre', 'Cantidad', 'Tiempo']

caja =v.multenterbox(msg="CDT- MISION TIC", title="Reto1", fields=lista)

nombre= caja[0]
capital = int(caja[1])
tiempo=int(caja[2])

resultado = CDT(nombre, capital, tiempo)

v.msgbox(msg=resultado, title="Reto 1", ok_button='ok')

