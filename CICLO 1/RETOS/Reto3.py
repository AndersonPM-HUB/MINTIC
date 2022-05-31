def AutoPartes(ventas: list): 
    diccionario={}
    for x  in ventas:
        if diccionario.get(x[0]) == None: 
            #lista con tuplas de su descripcion 
            diccionario[x[0]] = []
        diccionario[x[0]].append((x[1], x[2],x[3], x[4],x[5], x[6], x[7]))
    return diccionario


def consultaRegistro(ventas, idProducto): 
    if idProducto in ventas:
        for dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta in ventas[idProducto]:
            print(f'Producto consultado : {idProducto}  Descripción  {dProducto}  #Parte  {pnProducto}  Cantidad vendida  {cvProducto}  Stock  {sProducto}  Comprador {nComprador}  Documento  {cComprador}  Fecha Venta  {fVenta}')
    else: 
        print("No hay registro de venta de ese producto")


""" 
REGISTRO DE VENTAS : 
        id_producto 
        descripcion
        numero de partes
        cantidad vendida,
        stock del producto
        nombre comprador,
        id del comprador,
        fecha de venta
    """
    
ventas1 =([
 (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
 (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
 (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'), 
 (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
 (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')])

ventas2= ([(5489,'tornillo','RS8512',2,33,'JulioPerez',3654213,'13/06/2020'),
           (3215,'zocalo','UM8587',2,125,'LauraMacias',1256321,'13/06/2020'),
           (3698,'biela','PT3218',1,78,'LuisPeña',14565487,'13/06/2020'),
           (8795,'cilindro','AZ8794',2,96,'CarlosCasio',5612405,'13/06/2020')])

ventas3=([(9852,'Culata','XC9875',2,165,'LuisMolero',3455846,'14/06/2020'),
          (9852,'Culata','XC9875',2,165,'JoseMejia',1355846,'14/06/2020'),
          (2564,'Cárter','PT29872',2,32,'PeterCerezo',8545436,'14/06/2020'),
          (5412,'válvula','AZ8798',2,11,'JuanPeña',568975,'14/06/2020')])

x = consultaRegistro(AutoPartes(ventas1), 2010)


y= consultaRegistro(AutoPartes(ventas2), 2001)


z = consultaRegistro(AutoPartes(ventas3), 9852)


