def limpiar_contenido(contenido):
    resultado = []
    for linea in contenido:
        resultado += [linea.strip()]
    return resultado

def guardar_marca(contenido):
    try:
        ruta_archivo = "archivos/aviones.txt"
        with open(ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(contenido.strip() + "\n")
    except:
        print("Error: el archivo aviones.txt no existe")

def reescribir_marcas(contenido):
    try:
        ruta_archivo = "archivos/aviones.txt"
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            for marca in contenido:
                archivo.write(marca + "\n")
    except:
        print("Error: el archivo aviones.txt no existe")

def cargar_marcas():
    ruta_archivo = "archivos/aviones.txt"
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.readlines()
        contenido = limpiar_contenido(contenido)
        return contenido
    except:
        print("Error: el archivo aviones.txt no existe")

def guardar_modelo(modelo,marca,asientos_ejecutiva,asientos_turista,asientos_economica):
    ruta_archivo = "archivos/modeloAviones.txt"
    try:
        with open(ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"{modelo};{marca};{asientos_ejecutiva};{asientos_turista};{asientos_economica}\n")
    except:
        print("Error: el archivo modeloAviones.txt no existe")

def reescribir_modelos(contenido):
    ruta_archivo = "archivos/modeloAviones.txt"
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            for modelo in contenido:
                archivo.write(modelo + "\n")
    except:
        print("Error: el archivo modeloAviones.txt no existe")

def cargar_modelos():
    ruta_archivo = "archivos/modeloAviones.txt"
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.readlines()
        contenido = limpiar_contenido(contenido)
        return contenido
    except:
        print("Error: el archivo modeloAviones.txt no existe")

def cargar_aerolineas():
    ruta_archivo = "archivos/aerolineas.txt"
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.readlines()
        contenido = limpiar_contenido(contenido)
        return contenido
    except:
        print("Error: el archivo aerolineas.txt no existe")

def guardar_aerolinea(nombre,centro_operaciones):
    ruta_archivo = "archivos/aerolineas.txt"
    try:
        with open(ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre};{centro_operaciones}\n")
    except:
        print("Error: el archivo aerolineas.txt no existe")

def reescribir_aerolineas(contenido):
    ruta_archivo = "archivos/aerolineas.txt"
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            for aerolinea in contenido:
                archivo.write(aerolinea + "\n")
    except:
        print("Error: el archivo modeloAviones.txt no existe")

def cargar_usuarios():
    ruta_archivo = "archivos/acceso.txt"
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.readlines()
        contenido = limpiar_contenido(contenido)
        return contenido
    except:
        print("Error: el archivo acceso.txt no existe")

def cargar_aviones():
    ruta_archivo = "archivos/avionesAerolineas.txt"
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.readlines()
        contenido = limpiar_contenido(contenido)
        return contenido
    except:
        print("Error: el archivo avionesAerolineas.txt no existe")


