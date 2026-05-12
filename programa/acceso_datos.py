def control_acceso():
    usuarios_cargados = cargar_usuarios()
    if not usuarios_cargados:
        print("Error: No se encontraron usuarios disponibles")
    else:
        usuario_valido = False
        usuario_encontrado = []
        while not usuario_valido:
            usuario_ingresado = input("Ingrese su nombre de usuario ( o s para salir): ")
            if usuario_ingresado == "s":
                return 2
            for usuarios in usuarios_cargados:
                usuario = usuarios.strip().split(";")[0]
                clave = usuarios.strip().split(";")[1]
                if usuario_ingresado == usuario:
                    usuario_encontrado = [usuario,clave]
                    usuario_valido = True
            if not usuario_encontrado:
                print("Error: El usuario ingresado no existe")
        
        clave_valida = False
        while not clave_valida:
            clave_ingresada = input("Ingrese su contraseña ( o s para salir): ")

            if clave_ingresada == usuario_encontrado[1]:
                clave_valida = True
                return 1
            elif clave_ingresada == "s":
                return 2
            else:
                print("Error: La contraseña es incorrecta")	 

def limpiar_contenido(contenido):
    resultado = []
    for linea in contenido:
        resultado += [linea.strip()]
    return resultado

def limpiar_lista(lista):
    resultado = []
    for linea in lista:
        resultado += linea.strip().split(";")
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
        return []

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
        return []

def cargar_aerolineas():
    ruta_archivo = "archivos/aerolineas.txt"
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.readlines()
        contenido = limpiar_contenido(contenido)
        return contenido
    except:
        return []

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
        print("Error: el archivo acceso.txt no existe ")
        return []

def cargar_aviones():
    ruta_archivo = "archivos/avionesAerolineas.txt"
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.readlines()
        contenido = limpiar_contenido(contenido)
        return contenido
    except:
        return []

def guardar_avion(matricula, marca, modelo, año, aerolinea):
    ruta_archivo = "archivos/avionesAerolineas.txt"
    try:
        with open(ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"{matricula};{marca};{modelo};{año};{aerolinea}\n")
    except:
        print("Error: el archivo avionesAerolineas.txt no existe")

def reescribir_aviones(contenido):
    ruta_archivo = "archivos/avionesAerolineas.txt"
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            for avion in contenido:
                archivo.write(avion + "\n")
    except:
        print("Error: el archivo avionesAerolineas no existe")

def guardar_vuelo(numero_vuelo, codigo_salida, fecha_salida, hora_salida, codigo_arribo, fecha_arribo, hora_arribo, aerolinea, matricula, monto_ejecutiva, monto_turista, monto_economica):
    ruta_archivo = "archivos/vuelos.txt"
    try:
        with open(ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"{numero_vuelo};{codigo_salida};{fecha_salida};{hora_salida};{codigo_arribo};{fecha_arribo};{hora_arribo};{aerolinea};{matricula};{monto_ejecutiva};{monto_turista};{monto_economica}\n")
    except:
        print("Error: el archivo vuelos.txt no existe")

def reescribir_vuelos(contenido):
    ruta_archivo = "archivos/vuelos.txt"
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            for vuelo in contenido:
                archivo.write(vuelo + "\n")
    except:
        print("Error: el archivo vuelos.txt no existe")

def cargar_vuelos():
    ruta_archivo = "archivos/vuelos.txt"
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.readlines()
        contenido = limpiar_contenido(contenido)
        return contenido
    except:
        return []

def obtener_cantidad_asientos(matricula):
    aviones_cargados = cargar_aviones()
    resultado = []
    for avion in aviones_cargados:
        if avion.strip().split(";")[0] == matricula:
            resultado += [avion]
    resultado = limpiar_lista(resultado)
    return obtener_cantidad_asientos_aux(resultado)

def obtener_cantidad_asientos_aux(avion):
    modelos_cargados = cargar_modelos()
    marca_avion = avion[1]
    modelo_avion = avion[2]
    asientos_ejecutiva = 0
    asientos_turista = 0
    asientos_economica = 0
    resultado = []
    for modelo in modelos_cargados:
        if modelo.strip().split(";")[1] == marca_avion:
            if modelo.strip().split(";")[0] == modelo_avion:
                asientos_ejecutiva = modelo.strip().split(";")[2]
                asientos_turista = modelo.strip().split(";")[3]
                asientos_economica = modelo.strip().split(";")[4]
                resultado = [int(asientos_ejecutiva),int(asientos_turista),int(asientos_economica)]
    return resultado