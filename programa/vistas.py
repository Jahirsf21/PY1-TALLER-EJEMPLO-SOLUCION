def mostrar_marcas():
    ruta_archivo = "archivos/aviones.txt"
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.readlines()
        print("Marcas disponibles:")
        i = 1
        for marcas in contenido:
            marca = marcas.strip()
            print(f"{i}:{marca}")
            i+=1
    except:
        print("Error: el archivo aviones.txt no existe")

def mostrar_modelos():
    ruta_archivo = "archivos/modeloAviones.txt"
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.readlines()
        print("Modelos disponibles:")
        i = 1
        for modelos in contenido:
            modelo = modelos.strip().split(";")[0]
            print(f"{i}:{modelo}")
            i+=1
    except:
        print("Error: el archivo modeloAviones.txt no existe")

