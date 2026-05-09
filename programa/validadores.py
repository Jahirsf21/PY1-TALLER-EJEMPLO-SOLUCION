from acceso_datos import cargar_marcas, cargar_modelos

def validar_nombre(nombre):
    contador_digitos = 0
    contador_letras = 0
    for caracter in nombre:
        if caracter.isdigit():
            contador_digitos += 1
        else:
            contador_letras += 1
    if len(nombre) == contador_digitos:
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
            if marca_ingresada == marca:
                return True
        return False
    
def existe_marca_asociada(marca_ingresada):
    modelos_cargados = cargar_modelos()
    if not modelos_cargados:
        return False
    else:
        for modelos in modelos_cargados:
            marca = modelos.strip().split(";")[1]
            if marca_ingresada == marca:
                return True
        return False
