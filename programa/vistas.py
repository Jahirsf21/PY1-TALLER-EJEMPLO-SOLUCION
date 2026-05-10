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

def mostrar_aerolineas():
    ruta_archivo = "archivos/aerolineas.txt"
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.readlines()
        print("\nAerolineas disponibles:")
        i = 1
        for aerolineas in contenido:
            aerolinea = aerolineas.strip().split(";")[0]
            centro_operaciones = aerolineas.strip().split(";")[1]
            print(f"{i}: Nombre aerolinéa: {aerolinea} Centro de operaciones en: {centro_operaciones}")
            i+=1
    except:
        print("Error: el archivo aerolineas.txt no existe")

