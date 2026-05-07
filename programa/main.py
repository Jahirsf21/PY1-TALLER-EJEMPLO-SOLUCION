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
        
def cargar_usuarios():
    ruta_archivo = "archivos/acceso.txt"
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.readlines()
        return contenido
    except:
        print("Error: el archivo no existe")


def menu_administrador():
    print("\n    Panel de administrador    ")
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
            "menu_gestion_marcas()"
        elif opcion_ingresada == 2:
            "menu_gestion_modelos()"
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




menu_principal()
        

        
