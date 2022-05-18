def cliente(informacion:dict)->dict:
    """ aventuras extremas 
    Args:
        informacion (dict): diccionario con datos de cliente 
    Returns:
        dict: con la informacion de la atraccion y precio de la misma
    """  
    
    if informacion['edad'] >18 and informacion['primer_ingreso']== True: 
        valor_boleta=20000 - (20000 * 0.05) 
        atraccion = 'X-Treme'
        apto = True
    elif informacion['edad'] >18:
        valor_boleta=20000 
        atraccion = 'X-Treme'
        apto = True
        
    elif  informacion['edad'] >=15 and informacion['edad'] <=18 and informacion['primer_ingreso']== True:
        valor_boleta= 5000 -(5000 * 0.07)
        atraccion= 'Carros chocones'
        apto = True
    elif informacion['edad'] >=15 and informacion['edad'] <=18:
        valor_boleta=5000
        atraccion = 'Carros chocones'
        apto = True
        
    elif informacion['edad'] >=7 and informacion['edad'] <15 and informacion['primer_ingreso']== True: 
        valor_boleta= 10000 -(10000 * 0.05)
        atraccion= 'Sillas voladoras'
        apto = True
    elif informacion['edad'] >=7 and informacion['edad'] <15:
        valor_boleta=10000
        atraccion = 'Sillas voladoras'
        apto = True
        
    else:
        valor_boleta='N/A'
        atraccion='N/A'
        apto = False
        
        
    resultado ={
        'nombre': informacion['nombre'],
        'edad': informacion['edad'], 
        'atraccion': atraccion,
        'apto': apto,
        'primer_ingreso':informacion['primer_ingreso'],
        'total_boleta': valor_boleta,
    }
    
    return resultado
    
    
    
# pruebas para validar el codigo
cli1 = {
    'id_cliente': 1,
    'nombre': 'johana fernandez', 
    'edad': 20,
    'primer_ingreso': True,    
}

cli2 = {
    'id_cliente': 1,
    'nombre': 'johana fernandez', 
    'edad': 20,
    'primer_ingreso': False,    
}


cli3 = {
    'id_cliente': 2,
    'nombre': 'Gloria Suarez', 
    'edad': 3,
    'primer_ingreso': True,    
}

cli4 = {
    'id_cliente': 3,
    'nombre': 'tatiana Suarez', 
    'edad': 17,
    'primer_ingreso': True,    
}
cli5 = {
    'id_cliente': 3,
    'nombre': 'tatiana Suarez', 
    'edad': 17,
    'primer_ingreso': False,    
}

cli6 = {
    'id_cliente': 4,
    'nombre': 'tatiana Ruiz', 
    'edad': 8,
    'primer_ingreso': True,    
}
print(f"""
      {cliente(cli1)}
      {cliente(cli2)}
      {cliente(cli3)}
      {cliente(cli4)}
      {cliente(cli5)}
      {cliente(cli6)}
      """)
