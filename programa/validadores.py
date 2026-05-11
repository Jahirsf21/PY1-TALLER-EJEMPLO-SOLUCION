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
    
def validar_nombre_aerolinea(nombre):
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

def validar_nombre_centro_operaciones(nombre):
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
    
def validar_matricula(matricula):
    if len(matricula) <= 1:
        return False
    for caracter in matricula:
        if not caracter.isdigit() and not caracter.isalpha():
            return False  
    return True 

def validar_codigo_aeropuerto(codigo):
    if len(codigo) != 3:
        return False
    for caracter in codigo:
        if not caracter.isalpha():
            return False
    return True

def validar_fecha(fecha):
    partes = fecha.split("/")
    if len(partes) != 3:
        return False
    
    dia = partes[0]
    mes = partes[1]
    año = partes[2]
    if not dia.isdigit() or not mes.isdigit() or not año.isdigit():
        return False
    
    dia = int(dia)
    mes = int(mes)
    año = int(año)
    if dia < 1 or dia > 31:
        return False
    if mes < 1 or mes > 12:
        return False
    if año < 2026 or año > 2026:
        return False
    return True

def validar_hora(hora):
    partes = hora.split(":")
    if len(partes) != 2:
        return False
    
    horas = partes[0]
    minutos = partes[1]
    if not horas.isdigit() or not minutos.isdigit():
        return False
    
    horas = int(horas)
    minutos = int(minutos)
    if horas < 0 or horas > 23:
        return False
    if minutos < 0 or minutos > 59:
        return False
    return True

def validar_monto(monto):
    try:
        monto_valor = int(monto)
    except:
        return False
    if monto_valor <= 0:
        return False
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
    
def existe_aerolinea(aerolinea_ingresada):
    aerolineas_cargadas = cargar_aerolineas()
    if not aerolineas_cargadas:
        return  False
    else:
        for aerolineas in aerolineas_cargadas:
            aerolinea = aerolineas.strip().split(";")[0]
            if aerolinea_ingresada.strip() == aerolinea:
                return True
        return False
            
def existe_aerolinea_asociada(aerolinea_ingresada):
    aviones_cargados = cargar_aviones()
    if not aviones_cargados:
        return False
    else:
        for aviones in aviones_cargados:
            aerolinea = aviones.strip().split(";")[4]
            if aerolinea_ingresada.strip() == aerolinea:
                return True
        return False
    
def existe_avion(avion_ingresado):
    aviones_cargados = cargar_aviones()
    if not aviones_cargados:
        return False
    else:
        for aviones in aviones_cargados:
            matricula = aviones.strip().split(";")[0]
            if avion_ingresado.strip() == matricula:
                return True
        return False

def existe_avion_asociado(avion_ingresado):
    vuelos_cargados = cargar_vuelos()
    if not vuelos_cargados:
        return False
    else:
        for vuelos in vuelos_cargados:
            avion = vuelos.strip().split(";")[8]
            if avion_ingresado.strip() == avion:
                return True
        return False