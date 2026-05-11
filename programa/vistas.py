from acceso_datos import *

def mostrar_marcas():
    ruta_archivo = "archivos/aviones.txt"
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.readlines()
        print("\nMarcas disponibles:")
        i = 1
        for marcas in contenido:
            marca = marcas.strip()
            print(f"{i}: Nombre marca: {marca}")
            i+=1
    except:
        print("Error: el archivo aviones.txt no existe")

def mostrar_modelos():
    ruta_archivo = "archivos/modeloAviones.txt"
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.readlines()
        print("\nModelos disponibles:")
        i = 1
        for modelos in contenido:
            modelo = modelos.strip().split(";")[0]
            marca = modelos.strip().split(";")[1]
            asientos_ejecutiva = modelos.strip().split(";")[2]
            asientos_turista = modelos.strip().split(";")[3]
            asientos_economica = modelos.strip().split(";")[4]
            print(f"{i}:Nombre modelo: {modelo} Nombre marca: {marca} Asientos clase ejecutiva: {asientos_ejecutiva} Asientos clase turista: {asientos_turista} Asientos clase economica: {asientos_economica}")
            i+=1
    except:
        print("Error: el archivo modeloAviones.txt no existe")

def mostrar_modelos_marcas(marca):
    modelos_cargados = cargar_modelos()
    resultado = []
    if not modelos_cargados:
        return resultado
    for modelo in modelos_cargados:
        if modelo.strip().split(";")[1] == marca:
            resultado += [modelo]
    i = 1
    print("\nModelos disponibles para la marca seleccionada: ")
    for modelo in resultado:
        nombre = modelo.strip().split(";")[0]
        print(f"{i}: Nombre modelo: {nombre}")
        i += 1
    return resultado

def mostrar_aerolineas():
    ruta_archivo = "archivos/aerolineas.txt"
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.readlines()
        print("\nAerolineas disponibles:")
        i = 1
        for aerolineas in contenido:
            aerolinea = aerolineas.strip().split(";")[0]
            print(f"{i}: Nombre aerolinéa: {aerolinea}")
            i+=1
    except:
        print("Error: el archivo aerolineas.txt no existe")


def mostrar_aviones():
    ruta_archivo = "archivos/avionesAerolineas.txt"
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.readlines()
        print("\nAviones disponibles:")
        i = 1
        for aviones in contenido:
            matricula = aviones.strip().split(";")[0]
            marca = aviones.strip().split(";")[1]
            modelo = aviones.strip().split(";")[2]
            año = aviones.strip().split(";")[3]
            aerolinea = aviones.strip().split(";")[4]
            print(f"{i}: Matricula avion: {matricula} Marca: {marca} Modelo: {modelo} Año: {año} Aerolinea: {aerolinea}")
            i+=1
    except:
        print("Error: el archivo avionesAerolineas.txt no existe")

def mostrar_aviones_aerolinea(aerolinea):
    aviones_cargados = cargar_aviones()
    resultado = []
    if not aviones_cargados:
        return resultado
    for avion in aviones_cargados:
        if avion.strip().split(";")[4] == aerolinea:
            resultado += [avion]
    i = 1
    print("\nAviones disponibles para la aerolinea seleccionada:")
    for avion in resultado:
        matricula = avion.strip().split(";")[0]
        modelo = avion.strip().split(";")[2]
        print(f"{i}: Matricula: {matricula} Modelo: {modelo}")
        i += 1
    return resultado

def mostrar_vuelos():
    ruta_archivo = "archivos/vuelos.txt"
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.readlines()
        print("\nVuelos disponibles:")
        i = 1
        for vuelo in contenido:
            datos = vuelo.strip().split(";")
            numero_vuelo = datos[0]
            codigo_salida = datos[1]
            fecha_salida = datos[2]
            hora_salida = datos[3]
            codigo_arribo = datos[4]
            fecha_arribo = datos[5]
            hora_arribo = datos[6]
            aerolinea = datos[7]
            matricula = datos[8]
            monto_ejecutiva = datos[9]
            monto_turista = datos[10]
            monto_economica = datos[11]
            print(f"{i}: Numero vuelo: {numero_vuelo} | Salida: {codigo_salida} {fecha_salida} {hora_salida} | Arribo: {codigo_arribo} {fecha_arribo} {hora_arribo} | Aerolinea: {aerolinea} | Matricula avion: {matricula} | Montos: {monto_ejecutiva}/{monto_turista}/{monto_economica}")
            i+=1
    except:
        print("Error: el archivo vuelos.txt no existe")