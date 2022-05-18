# ingresar notas de un estudiante, el programa regresa los datos ingresados 

infoEstudiante={}


infoEstudiante['nombre'] = input('ingrese el nombre : ')
infoEstudiante['nota1'] = float(input('ingrese el n1: '))
infoEstudiante['nota2'] = float(input('ingrese el n2: '))
infoEstudiante['nota3'] = float(input('ingrese el n3: '))


def nota_final(info:dict)-> float:
    nota = info['nota1']*0.3 + info['nota2'] * 0.4 + info['nota3']* 0.3
    return nota


infoEstudiante['nota_final'] = nota_final(infoEstudiante)

def aprueba(nota:float):
    if nota >= 3.0 :
        mensaje = 'Aprueba'
    else:
        mensaje = 'reprueba'
    return mensaje

infoEstudiante['aprueba']= aprueba(infoEstudiante['nota_final'])



for etiqueta in infoEstudiante:
    print(f"{etiqueta} : {infoEstudiante[etiqueta]}") 

