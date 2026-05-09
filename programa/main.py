from validadores import *
from acceso_datos import *
from acceso_datos import *
from acceso_datos import *
from vistas import *

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
            if control_acceso() == 1:
                return menu_administrador()
        elif opcion_ingresada == 2:
            "menu_usuario()"
        elif opcion_ingresada == 3:
            exit()
        else:
            print("Error: la opción ingresada no existe\n")


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
        marcas = cargar_marcas()
        opcion_ingresada = input("Ingresa una opción: ")
        if opcion_ingresada != "":
            try:
                opcion_ingresada = int(opcion_ingresada)
            except:
                print("Error: la opción debe ser un número\n")
        if opcion_ingresada == 1:
            return incluir_marca()
        elif opcion_ingresada == 2:
            if not marcas:
                print("Error: No se pueden eliminar marcas ya que no hay marcas registradas")
            else:
                return eliminar_marca()
        elif opcion_ingresada == 3:
            if not marcas:
                print("Error: No se pueden modificar marcas ya que no hay marcas registradas")
            else:
                return modificar_marca()
        elif opcion_ingresada == 4:
            if not marcas:
                print("Error: No hay marcas registradas para mostrar")
            else:
                mostrar_marcas()
        elif opcion_ingresada == 5: 
            return menu_administrador()
        else:
            print("Error: la opción ingresada no existe\n")


def incluir_marca():
    marca_valida = False
    while not marca_valida:
        marca_ingresada = input("Ingrese el nombre de la marca (o s para salir): ")
        if marca_ingresada != "":
            if existe_marca(marca_ingresada):
                print("Error: esta marca ya existe")
            elif not validar_nombre_marca(marca_ingresada):
                print("Error: el nombre de la marca no puede ser solo números o de un solo caracter")
            else:
                marca_valida = True
        else:
            print("Error: la marca ingresada no puede ser vacio")

    guardar_marca(marca_ingresada)
    print(f"Marca {marca_ingresada} agregada exitosamente")
    mostrar_marcas()
    return menu_gestion_marcas()


def eliminar_marca():
    mostrar_marcas()
    contenido_anterior = cargar_marcas()
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el número de opción de la marca que desea eliminar (o 0 para salir): ")
        if indice_ingresado == "":
            print("Error: el número de opción no puede ser vacio")
        else:
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: el número de opción debe ser un valor númerico")
        if indice_ingresado < 0 or indice_ingresado > len(contenido_anterior):
            print("Error: la opción ingresada no existe")
        elif indice_ingresado == 0:
            return menu_gestion_marcas()
        elif existe_marca_asociada(contenido_anterior[indice_ingresado-1]):
            print("Error: no se puede eliminar ya que esta asociado a un modelo")
        else:
            indice_valido = True

    contenido_nuevo = contenido_anterior[:indice_ingresado-1] + contenido_anterior[indice_ingresado:]
    reescribir_marcas(contenido_nuevo)
    mostrar_marcas()

    return menu_gestion_marcas()
        
def modificar_marca():
    mostrar_marcas()
    contenido_anterior = cargar_marcas()
    print(len(contenido_anterior))
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el número de opción de la marca que desea editar (0 para salir): ")
        if indice_ingresado == "":
            print("Error: El número de opción no puede ser vacio")
        else:
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: el número de opción debe ser un valor númerico")
        if indice_ingresado < 0 or indice_ingresado > len(contenido_anterior):
            print("Error: la opcion ingresada no existe")
        elif indice_ingresado == 0:
            return menu_gestion_marcas()
        else:
            indice_valido = True
    
    marca_valida = False
    while not marca_valida:
        marca_ingresada = input("Ingrese el nuevo nombre de la marca (o s para salir): ")
        if marca_ingresada != "":
            if existe_marca(marca_ingresada):
                print("Error: esta marca ya existe")
            elif not validar_nombre_marca(marca_ingresada):
                print("Error: el nombre de la marca no puede ser solo números o de un solo caracter")
            else:
                marca_valida = True

    contenido_anterior[indice_ingresado-1] = marca_ingresada.strip()
    reescribir_marcas(contenido_anterior)
    print("Marca modificada exitosamente")
    mostrar_marcas()
    return menu_gestion_marcas()

def menu_gestion_modelos():
    print("\nPanel de administrador - gestión modelos")
    while True:
        print("====== Opciones disponibles ======")
        print("(1) Incluir modelo")
        print("(2) Eliminar modelo")
        print("(3) Modificar modelo")
        print("(4) Mostrar modelos")
        print("(5) Regresar al menú principal")
        marcas = cargar_marcas()
        modelos = cargar_modelos()
        opcion_ingresada = input("Ingresa una opción: ")
        if opcion_ingresada != "":
            try:
                opcion_ingresada = int(opcion_ingresada)
            except:
                print("Error: la opción debe ser un número\n")
        if opcion_ingresada == 1:
            if not marcas:
                print("Error: no se pueden crear modelos ya que no hay marcas registradas")
            else:
                return incluir_modelo()
        elif opcion_ingresada == 2:
            if not modelos:
                print("Error: no hay modelos registrados")
            else:
                "return eliminar_modelo())"
        elif opcion_ingresada == 3:
            "modificar_marca()"
        elif opcion_ingresada == 4:
            "mostrar_marcas()"
        elif opcion_ingresada == 5: 
            return menu_administrador()
        else:
            print("Error: la opción ingresada no existe\n")

def incluir_modelo():
    modelo_valido = False
    while not modelo_valido:
        modelo_ingresado = input("Ingrese el nombre del modelo (o s para salir): ")
        if modelo_ingresado != "":
            if existe_modelo(modelo_ingresado):
                print("Error: el nombre de este modelo ya existe")
            elif modelo_ingresado == "s":
                return menu_gestion_modelos()
            elif not validar_nombre_modelo(modelo_ingresado):
                print("Error: el nombre del modelo no puede ser solo números o de un solo caracter")
            else:
                modelo_valido = True
        else:
            print("Error: el nombre del modelo ingresado no puede ser vacio")
            
    mostrar_marcas()
    contenido_marcas = cargar_marcas()
    indice_valido = False

    while not indice_valido:
        indice_ingresado = input("Ingrese el número de opcion de la marca que desea usar (0 s para salir): ")
        if indice_ingresado == "":
            print("Error: El número de opción no puede ser vacio")
        else:
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: el número de opción debe ser un valor númerico")
        if indice_ingresado < 0 or indice_ingresado > len(contenido_marcas):
            print("Error: la opcion ingresada no existe")
        elif indice_ingresado == 0:
            return menu_gestion_modelos()
        else:
            indice_valido = True
            marca_seleccionada = contenido_marcas[indice_ingresado-1]

    asiento_valido = False
    while not asiento_valido:
        cantidad_ingresada = input("Ingrese la cantidad de asiento para la clase ejecutiva (o -1 para salir): ")
        if cantidad_ingresada == "":
            print("Error: la cantidad de asiento no puede ser vacio")
        else:
            try:
                cantidad_ingresada = int(cantidad_ingresada)
            except:
                print("Error: el número de asientos debe ser un valor númerico")
        if cantidad_ingresada == -1:
            return menu_gestion_modelos()
        elif cantidad_ingresada <= 0:
            print("Error: la cantidad de asientos no puede menor a 0")
        else:
            asiento_valido = True
    asientos_clase_ejecutiva = cantidad_ingresada

    asiento_valido = False
    while not asiento_valido:
        cantidad_ingresada = input("Ingrese la cantidad de asiento para la clase turista (o -1 para salir): ")
        if cantidad_ingresada == "":
            print("Error: la cantidad de asiento no puede ser vacio")
        else:
            try:
                cantidad_ingresada = int(cantidad_ingresada)
            except:
                print("Error: el número de asientos debe ser un valor númerico")
        if cantidad_ingresada == -1:
            return menu_gestion_modelos()
        elif cantidad_ingresada <= 0:
            print("Error: la cantidad de asientos no puede menor a 0")
        else:
            asiento_valido = True
    asientos_clase_turista = cantidad_ingresada

    asiento_valido = False
    while not asiento_valido:
        cantidad_ingresada = input("Ingrese la cantidad de asiento para la clase economica (o -1 para salir): ")
        if cantidad_ingresada == "":
            print("Error: la cantidad de asiento no puede ser vacio")
        else:
            try:
                cantidad_ingresada = int(cantidad_ingresada)
            except:
                print("Error: el número de asientos debe ser un valor númerico")
        if cantidad_ingresada == -1:
            return menu_gestion_modelos()
        elif cantidad_ingresada <= 0:
            print("Error: la cantidad de asientos no puede menor a 0")
        else:
            asiento_valido = True

    asientos_clase_economica = cantidad_ingresada
    guardar_modelo(modelo_ingresado.strip(),marca_seleccionada,asientos_clase_ejecutiva,asientos_clase_turista,asientos_clase_economica)
    print(f"\nNombre del modelo: {modelo_ingresado.strip()}\nNombre de la marca: {marca_seleccionada}\nCantidad asientos clase ejecutiva: {asientos_clase_ejecutiva}\nCantidad asientos clase turista: {asientos_clase_turista}\nCantidad asientos clase economica: {asientos_clase_economica}\nNuevo modelo agregado existosamente")
    modelo_valido = True
    mostrar_modelos()
    return menu_gestion_modelos()

def eliminar_modelo():
    mostrar_modelos()       
    contenido_anterior = cargar_modelos()
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el número de opción del modelo que desea eliminar (o 0 para salir): ")
        if indice_ingresado == "":
            print("Error: el número de opción no puede ser vacio")
        else:
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: el número de opción debe ser un valor númerico")
        if indice_ingresado < 0 or indice_ingresado > len(contenido_anterior):
            print("Error: la opcion ingresada no existe")
        elif indice_ingresado == 0:
            return menu_gestion_modelos()
        elif existe_modelo_asociado((contenido_anterior[indice_ingresado-1]).split(";")[0]):
            print("Error: no se puede eliminar ya que esta asociado a un avion")
        else:
            indice_valido = True

    contenido_nuevo = contenido_anterior[:indice_ingresado-1] + contenido_anterior[indice_ingresado:]
    reescribir_modelos(contenido_nuevo)
    print(f"Modelo {contenido_anterior[indice_ingresado-1]} eliminado con exito")
    mostrar_modelos()
    return menu_gestion_modelos()

menu_principal()



