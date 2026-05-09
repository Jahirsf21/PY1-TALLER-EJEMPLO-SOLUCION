from validadores import validar_nombre, existe_marca, existe_marca_asociada
from acceso_datos import cargar_usuarios
from vistas import mostrar_marcas

def menu_principal():
    print("Bienvenido al sistema de reservación de vuelos")
    while True:
        print("====== Opciones disponibles ======")
        print("(1) Opciones administrativas")
        print("(2) Opciones de Usuario")
        print("(3) Salir")
        opcion_ingresada = input("Ingresa una opción: ")
        if opcion_ingresada != "":
            try:
                opcion_ingresada = int(opcion_ingresada)
            except:
                print("Error: la opción debe ser un número\n")
        if opcion_ingresada == 1:
            return control_acceso()
        elif opcion_ingresada == 2:
            "menu_usuario()"
        elif opcion_ingresada == 3:
            exit()
        else:
            print("Error: la opción ingresada no existe\n")

def control_acceso():
    usuarios_cargados = cargar_usuarios()
    if not usuarios_cargados:
        print("Error: No se encontraron usuarios disponibles")
    else:
        for usuarios in usuarios_cargados:
            usuario = usuarios.strip().split(";")[0]
            clave = usuarios.strip().split(";")[1]
            usuario_valido = False
            while not usuario_valido:
                usuario_ingresado = input("Ingrese su nombre de usuario ( o s para salir): ")
                if usuario_ingresado == usuario:
                    usuario_valido = True
                elif usuario_ingresado == "s":
                    return menu_principal()
                else:
                    print("Error: El usuario ingresado no existe")
            clave_valida = False
            while not clave_valida:
                clave_ingresada = input("Ingrese su contraseña ( o s para salir): ")
                if clave_ingresada == clave:
                    clave_valida = True
                    menu_administrador()
                elif clave_ingresada == "s":
                    return menu_principal()
                else:
                    print("Error: La contraseña es incorrecta")


def menu_administrador():
    print("\n    Panel de administrador")
    while True:
        print("====== Opciones disponibles ======")
        print("(1) Gestión de marcas de aviones")
        print("(2) Gestión de modelos de aviones")
        print("(3) Gestión de aerolíneas")
        print("(4) Gestión de aviones por aerolínea")
        print("(5) Gestión de vuelos")
        print("(6) Estadísticas de vuelo")
        print("(7) Consultar historial de reservaciones")
        print("(8) Regresar al menú principal")
        opcion_ingresada = input("Ingresa una opción: ")
        if opcion_ingresada != "":
            try:
                opcion_ingresada = int(opcion_ingresada)
            except:
                print("Error: la opción debe ser un número\n")
        if opcion_ingresada == 1:
            return menu_gestion_marcas()
        elif opcion_ingresada == 2:
            return menu_gestion_modelos()
        elif opcion_ingresada == 3:
            "menu_gestion_aerolineas()"
        elif opcion_ingresada == 4:
            "menu_gestion_aviones_aerolineas()"
        elif opcion_ingresada == 5:
            "menu_gestion_vuelos()"
        elif opcion_ingresada == 6:
            "estadisticas_vuelos()"
        elif opcion_ingresada == 7:
            "historial_reservaciones()"
        elif opcion_ingresada == 8: 
            return menu_principal()
        else:
            print("Error: la opción ingresada no existe\n")

def menu_gestion_marcas():
    print("\nPanel de administrador - gestión marcas")
    while True:
        print("====== Opciones disponibles ======")
        print("(1) Incluir marca")
        print("(2) Eliminar marca")
        print("(3) Modificar marca")
        print("(4) Mostrar marcas")
        print("(5) Regresar al menú principal")
        opcion_ingresada = input("Ingresa una opción: ")
        if opcion_ingresada != "":
            try:
                opcion_ingresada = int(opcion_ingresada)
            except:
                print("Error: la opción debe ser un número\n")
        if opcion_ingresada == 1:
            return incluir_marca()
        elif opcion_ingresada == 2:
            eliminar_marca()
        elif opcion_ingresada == 3:
            modificar_marca()
        elif opcion_ingresada == 4:
            mostrar_marcas()
        elif opcion_ingresada == 5: 
            return menu_administrador()
        else:
            print("Error: la opción ingresada no existe\n")


def incluir_marca():
    ruta_archivo = "archivos/aviones.txt"
    marca_valida = False
    while not marca_valida:
        marca_ingresada = input("Ingrese el nombre de la marca (o s para salir): ")
        if marca_ingresada != "":
            if existe_marca(marca_ingresada):
                print("Error: esta marca ya existe")
            elif not validar_nombre(marca_ingresada):
                print("Error: el nombre no puede ser solo números")
            else:
                with open(ruta_archivo, "a", encoding="utf-8") as archivo:
                    archivo.write(marca_ingresada + "\n")
                print(f"Marca {marca_ingresada} agregada exitosamente")
                mostrar_marcas()
                marca_valida = True
        else:
            print("Error: la marca ingresada no puede ser vacio")
    return menu_gestion_marcas()


def eliminar_marca():
    ruta_archivo = "archivos/aviones.txt"
    mostrar_marcas()

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.readlines()
    contenido_anterior = []
    for marcas in contenido:
        marca = marcas.strip()
        contenido_anterior += [marca]
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el indice de la marca que desea eliminar (o 0 para salir): ")
        if indice_ingresado == "":
            print("Error: El indice no puede ser vacio")
        else:
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: el indice debe ser un valor númerico")
        if indice_ingresado < 0 or indice_ingresado > len(contenido_anterior):
            print("Error: el indice ingresado no existe")
        elif indice_ingresado == 0:
            return menu_gestion_marcas()
        elif existe_marca_asociada(contenido_anterior[indice_ingresado-1]):
            print("Error: no se puede eliminar ya que esta asociado a un modelo")
        else:
            indice_valido = True

    contenido_nuevo = contenido_anterior[:indice_ingresado-1] + contenido_anterior[indice_ingresado:]
    print(f"Marca {contenido_anterior[indice_ingresado-1]} eliminada con exito")
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        for marca in contenido_nuevo:
            archivo.write(marca + "\n")
    mostrar_marcas()
    return menu_gestion_marcas()
        
def modificar_marca():
    ruta_archivo = "archivos/aviones.txt"
    mostrar_marcas()

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.readlines()
    contenido_anterior = []
    for marcas in contenido:
        marca = marcas.strip()
        contenido_anterior += [marca]

    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el indice de la marca que desea editar (o s para salir): ")
        if indice_ingresado == "":
            print("Error: El indice no puede ser vacio")
        else:
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: el indice debe ser un valor númerico")
        if indice_ingresado <= 0 or indice_ingresado > len(contenido_anterior):
            print("Error: el indice ingresado no existe")
        elif indice_ingresado == "s":
            return menu_gestion_marcas()
        else:
            indice_valido = True
    
    marca_valida = False
    while not marca_valida:
        marca_ingresada = input("Ingrese el nuevo nombre de la marca (o s para salir): ")
        if marca_ingresada != "":
            if existe_marca(marca_ingresada):
                print("Error: esta marca ya existe")
            elif not validar_nombre(marca_ingresada):
                print("Error: el nombre no puede ser solo números")
            else:
                contenido_anterior[indice_ingresado-1] = marca_ingresada
                with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                    for marca in contenido_anterior:
                        archivo.write(marca + "\n")
                print("Marca modificada exitosamente")
                mostrar_marcas()
                marca_valida = True

    return menu_gestion_marcas()