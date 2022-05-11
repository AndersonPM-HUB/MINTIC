def CDT(usuario:str, capital: int, tiempo:int): 
    """ CDT
    Args:
        usuario (str): alfanumerico
        capital (int): monto a ingresar
        tiempo (int): tiempo del CDT
    """
    if tiempo >= 3:
        valor_interes = (capital * 0.03 * tiempo) / 12
        valor_total = valor_interes + capital    
    else :
        valor_perder = capital*0.02
        valor_total = capital -valor_perder
        
    mensaje = f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial { capital } para un tiempo de {tiempo} meses es: {valor_total}'
    
    return mensaje 


print(CDT("AB1012",1000000,3))