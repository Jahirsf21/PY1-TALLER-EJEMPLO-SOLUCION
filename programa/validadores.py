from acceso_datos import *

def validar_nombre_marca(nombre):
    contador_digitos = 0
    contador_letras = 0
    for caracter in nombre:
        if caracter.isdigit():
            contador_digitos += 1
        else:
            contador_letras += 1
    if len(nombre) == contador_digitos:
        return False
    elif len(nombre) == 1:
        return False
    else:
        return True
    
def validar_nombre_modelo(nombre):
    contador_digitos = 0
    contador_letras = 0
    for caracter in nombre:
        if caracter.isdigit():
            contador_digitos += 1
        else:
            contador_letras += 1
    if len(nombre) == contador_digitos:
        return False
    elif len(nombre) == 1:
        return False
    else:
        return True

        
def existe_marca(marca_ingresada):
    marcas_cargadas = cargar_marcas()
    if not marcas_cargadas:
        return False
    else:
        for marcas in marcas_cargadas:
            marca = marcas.strip()
            if marca_ingresada.strip() == marca:
                return True
        return False
    
def existe_marca_asociada(marca_ingresada):
    modelos_cargados = cargar_modelos()
    if not modelos_cargados:
        return False
    else:
        for modelos in modelos_cargados:
            marca = modelos.strip().split(";")[1]
            if marca_ingresada.strip() == marca:
                return True
        return False

def existe_modelo(modelo_ingresado):
    modelos_cargados = cargar_modelos()
    if not modelos_cargados:
        return False
    else:
        for modelos in modelos_cargados:
            modelo = modelos.strip().split(";")[0]
            if modelo_ingresado.strip() == modelo:
                return True
        return False
    
def existe_modelo_asociado(modelo_ingresado):
    aviones_cargados = cargar_aviones()
    if not aviones_cargados:
        return False
    else:
        for aviones in aviones_cargados:
            modelo = aviones.strip().split(";")[2]
            if modelo_ingresado.strip() == modelo:
                return True
        return False
