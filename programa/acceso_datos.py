from vistas import mostrar_marcas


def limpiar_contenido(contenido):
    resultado = []
    for linea in contenido:
        resultado += [linea.strip()]
    return resultado

def cargar_marcas():
    ruta_archivo = "archivos/aviones.txt"
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.readlines()
        contenido = limpiar_contenido(contenido)
        return contenido
    except:
        print("Error: el archivo aviones.txt no existe")

def cargar_modelos():
    ruta_archivo = "archivos/modeloAviones.txt"
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.readlines()
        contenido = limpiar_contenido(contenido)
        return contenido
    except:
        print("Error: el archivo aviones.txt no existe")


def cargar_usuarios():
    ruta_archivo = "archivos/acceso.txt"
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.readlines()
        contenido = limpiar_contenido(contenido)
        return contenido
    except:
        print("Error: el archivo aviones.txt no existe")


def cargar_aviones():
    ruta_archivo = "archivos/avionesAerolineas.txt"
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.readlines()
        contenido = limpiar_contenido(contenido)
        return contenido
    except:
        print("Error: el archivo aviones.txt no existe")


