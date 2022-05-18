def AutoPartes(ventas: list): 
    """_summary_

    Args:
        ventas (list): _description_
    """
    
    for venta in ventas:
        
    Diccionario ={
        'Producto consultado' : {idProducto},
        'Descripción': {dProducto} ,
        'Parte' : {pnProducto},
        'Cantidad vendida' : {cvProducto},
        'Stock' : {sProducto},
        'Comprador': {nComprador},
        'Documento': {cComprador},
        'Fecha Venta' : {fVenta}
    }
    
    return diccionario


def consultaRegistros(ventas , id_producto): 
    pass







""" REGISTRO DE VENTAS : 
        id_producto 
        descripcion
        numero de partes
        cantidad vendida,
        stock del producto
        nombre comprador,
        id del comprador,
        fecha de venta
    """
ventas =([
 (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
 (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
 (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'), 
 (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
 (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')])

print(len(ventas))
