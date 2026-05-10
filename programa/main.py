from validadores import *
from acceso_datos import *
from vistas import *

def menu_principal():
    while True:
        print("\nBienvenido al sistema de reservación de vuelos")
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
                continue
            if opcion_ingresada == 1:
                if control_acceso() == 1:
                    menu_administrador()
            elif opcion_ingresada == 2:
                "menu_usuario()"
            elif opcion_ingresada == 3:
                exit()
            else:
                print("Error: la opción ingresada no existe\n")
        else:
            print("Error: la opción ingresada no puede ser vacio")   

def menu_administrador():
    while True:
        print("\n    Panel de administrador")
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
                continue
            if opcion_ingresada == 1:
                menu_gestion_marcas()
            elif opcion_ingresada == 2:
                menu_gestion_modelos()
            elif opcion_ingresada == 3:
                menu_gestion_aerolineas()
            elif opcion_ingresada == 4:
                "menu_gestion_aviones_aerolineas()"
            elif opcion_ingresada == 5:
                "menu_gestion_vuelos()"
            elif opcion_ingresada == 6:
                "estadisticas_vuelos()"
            elif opcion_ingresada == 7:
                "historial_reservaciones()"
            elif opcion_ingresada == 8: 
                break
            else:
                print("Error: la opción ingresada no existe\n")
        else:
            print("Error: la opción ingresada no puede ser vacio")

def menu_gestion_marcas():
    while True:
        print("\nPanel de administrador - gestión marcas")
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
                continue
            if opcion_ingresada == 1:
                incluir_marca()
            elif opcion_ingresada == 2:
                if not marcas:
                    print("Error: No se pueden eliminar marcas ya que no hay marcas registradas")
                else:
                    eliminar_marca()
            elif opcion_ingresada == 3:
                if not marcas:
                    print("Error: No se pueden modificar marcas ya que no hay marcas registradas")
                else:
                    modificar_marca()
            elif opcion_ingresada == 4:
                if not marcas:
                    print("Error: No hay marcas registradas para mostrar")
                else:
                    mostrar_marcas()
            elif opcion_ingresada == 5: 
                break
            else:
                print("Error: la opción ingresada no existe\n")
        else:
            print("Error: la opción ingresada no puede ser vacio")

def incluir_marca():
    marca_valida = False
    while not marca_valida:
        marca_ingresada = input("Ingrese el nombre de la marca (o s regresar): ")
        if marca_ingresada != "":
            if existe_marca(marca_ingresada):
                print("Error: esta marca ya existe")
            elif marca_ingresada == "s":
                return 
            elif not validar_nombre_marca(marca_ingresada):
                print("Error: el nombre de la marca no puede ser solo números o de un solo caracter")
            else:
                marca_valida = True
        else:
            print("Error: la marca ingresada no puede ser vacio")

    guardar_marca(marca_ingresada)
    print(f"Marca {marca_ingresada} agregada exitosamente")
    mostrar_marcas()
    return 

def eliminar_marca():
    mostrar_marcas()
    contenido_anterior = cargar_marcas()
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el número de opción de la marca que desea eliminar (o 0 para regresar): ")
        if indice_ingresado != "":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: el número de opción debe ser un valor númerico")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(contenido_anterior):
                print("Error: la opción ingresada no existe")
            elif indice_ingresado == 0:
                return 
            elif existe_marca_asociada(contenido_anterior[indice_ingresado-1]):
                print("Error: no se puede eliminar ya que esta asociado a un modelo")
            else:
                indice_valido = True
        else:
            print("Error: la opción ingresada no puede ser vacio")

    contenido_nuevo = contenido_anterior[:indice_ingresado-1] + contenido_anterior[indice_ingresado:]
    reescribir_marcas(contenido_nuevo)
    print("Marca eliminada exitosamente")
    mostrar_marcas()
    return 
        
def modificar_marca():
    mostrar_marcas()
    contenido_anterior = cargar_marcas()
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el número de opción de la marca que desea editar (0 para regresar): ")
        if indice_ingresado !="":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: el número de opción debe ser un valor númerico")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(contenido_anterior):
                print("Error: la opcion ingresada no existe")
            elif indice_ingresado == 0:
                return 
            else:
                indice_valido = True
        else:
            print("Error: el número de opción no puede ser vacio")
    
    marca_valida = False
    marca_actual = contenido_anterior[indice_ingresado-1]
    while not marca_valida:
        marca_ingresada = input("Ingrese el nuevo nombre de la marca (s para regresar o enter para mantener el nombre de la marca actual): ")
        if marca_ingresada == "":
            marca_ingresada = marca_actual
            marca_valida = True
        else:
            if existe_marca(marca_ingresada) and marca_ingresada != marca_actual:
                print("Error: esta marca ya existe")
            elif marca_ingresada == "s":
                return 
            elif not validar_nombre_marca(marca_ingresada):
                print("Error: el nombre de la marca no puede ser solo números o de un solo caracter")
            else:
                marca_valida = True

    contenido_anterior[indice_ingresado-1] = marca_ingresada.strip()
    reescribir_marcas(contenido_anterior)
    print("Marca modificada exitosamente")
    mostrar_marcas()
    return

def menu_gestion_modelos():
    while True:
        print("\nPanel de administrador - gestión modelos")
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
                continue
            if opcion_ingresada == 1:
                if not marcas:
                    print("Error: no se pueden crear modelos ya que no hay marcas registradas")
                else:
                    incluir_modelo()
            elif opcion_ingresada == 2:
                if not modelos:
                    print("Error: no hay modelos registrados")
                else:
                    eliminar_modelo()
            elif opcion_ingresada == 3:
                if not modelos:
                    print("Error: no hay modelos registrados")
                elif not marcas:
                    print("Error: no hay marcas registradas")
                else:
                    modificar_modelo()
            elif opcion_ingresada == 4:
                if not modelos:
                    print("Error: no hay modelos registrados para mostrar")
                else:
                    mostrar_modelos()
            elif opcion_ingresada == 5: 
                break
            else:
                print("Error: la opción ingresada no existe\n")
        else:
            print("Error: el número de opción no puede ser vacio")

def incluir_modelo():
    modelo_valido = False
    while not modelo_valido:
        modelo_ingresado = input("Ingrese el nombre del modelo (o s regresar): ")
        if modelo_ingresado != "":
            if existe_modelo(modelo_ingresado):
                print("Error: el nombre de este modelo ya existe")
            elif modelo_ingresado == "s":
                return 
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
        indice_ingresado = input("Ingrese el número de opcion de la marca que desea usar ( o 0 para regresar): ")
        if indice_ingresado !="":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: el número de opción debe ser un valor númerico")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(contenido_marcas):
                print("Error: la opcion ingresada no existe")
            elif indice_ingresado == 0:
                return 
            else:
                indice_valido = True
                marca_seleccionada = contenido_marcas[indice_ingresado-1]
        else:
            print("Error: el número de opción no puede ser vacio")

    asiento_valido = False
    while not asiento_valido:
        cantidad_ingresada = input("Ingrese la cantidad de asientos para la clase ejecutiva (o -1 para regresar): ")
        if cantidad_ingresada != "":
            try:
                cantidad_ingresada = int(cantidad_ingresada)
            except:
                print("Error: el número de asientos debe ser un valor númerico")
                continue
            if cantidad_ingresada == -1:
                return 
            elif cantidad_ingresada <= 0:
                print("Error: la cantidad de asientos no puede menor a 0")
            else:
                asiento_valido = True
        else:
            print("Error: la cantidad de asientos no puede ser vacio")
    asientos_clase_ejecutiva = cantidad_ingresada

    asiento_valido = False
    while not asiento_valido:
        cantidad_ingresada = input("Ingrese la cantidad de asientos para la clase turista (o -1 para regresar): ")
        if cantidad_ingresada != "":
            try:
                cantidad_ingresada = int(cantidad_ingresada)
            except:
                print("Error: el número de asientos debe ser un valor númerico")
                continue
            if cantidad_ingresada == -1:
                return 
            elif cantidad_ingresada <= 0:
                print("Error: la cantidad de asientos no puede menor a 0")
            else:
                asiento_valido = True
        else:
            print("Error: la cantidad de asientos no puede ser vacio")
    asientos_clase_turista = cantidad_ingresada

    asiento_valido = False
    while not asiento_valido:
        cantidad_ingresada = input("Ingrese la cantidad de asientos para la clase economica (o -1 para regresar): ")
        if cantidad_ingresada != "":
            try:
                cantidad_ingresada = int(cantidad_ingresada)
            except:
                print("Error: el número de asientos debe ser un valor númerico")
                continue
            if cantidad_ingresada == -1:
                return 
            elif cantidad_ingresada <= 0:
                print("Error: la cantidad de asientos no puede menor a 0")
            else:
                asiento_valido = True
        else:
            print("Error: la cantidad de asientos no puede ser vacio")

    asientos_clase_economica = cantidad_ingresada
    guardar_modelo(modelo_ingresado.strip(),marca_seleccionada,asientos_clase_ejecutiva,asientos_clase_turista,asientos_clase_economica)
    print(f"\nNombre del modelo: {modelo_ingresado.strip()}\nNombre de la marca: {marca_seleccionada}\nCantidad asientos clase ejecutiva: {asientos_clase_ejecutiva}\nCantidad asientos clase turista: {asientos_clase_turista}\nCantidad asientos clase economica: {asientos_clase_economica}\nNuevo modelo agregado exitosamente")
    modelo_valido = True
    mostrar_modelos()
    return 

def eliminar_modelo():
    mostrar_modelos()       
    contenido_anterior = cargar_modelos()
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el número de opción del modelo que desea eliminar (o 0 para regresar): ")
        if indice_ingresado != "":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: el número de opción debe ser un valor númerico")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(contenido_anterior):
                print("Error: la opcion ingresada no existe")
            elif indice_ingresado == 0:
                return 
            elif existe_modelo_asociado((contenido_anterior[indice_ingresado-1]).split(";")[0]):
                print("Error: no se puede eliminar ya que esta asociado a un avion")
            else:
                indice_valido = True
        else:
            print("Error: el número de opción no puede ser vacio")

    contenido_nuevo = contenido_anterior[:indice_ingresado-1] + contenido_anterior[indice_ingresado:]
    reescribir_modelos(contenido_nuevo)
    print(f"Modelo {contenido_anterior[indice_ingresado-1]} eliminado con exito")
    mostrar_modelos()
    return 

def modificar_modelo():
    mostrar_modelos()
    contenido_anterior = cargar_modelos()
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el número de opción del modelo que desea modificar (o 0 para regresar): ")
        if indice_ingresado != "":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: el número de opción debe ser un valor númerico")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(contenido_anterior):
                print("Error: la opcion ingresada no existe")
            elif indice_ingresado == 0:
                return 
            else:
                indice_valido = True
        else:
            print("Error: el número de opción no puede ser vacio")

    modelo_seleccionado = contenido_anterior[indice_ingresado-1].split(";")
    return modificar_modelo_aux(modelo_seleccionado, contenido_anterior, indice_ingresado-1)

def modificar_modelo_aux(modelo_seleccionado,contenido_anterior, indice_seleccionado):
    print(f"\nModelo seleccionado para editar:\nNombre modelo: {modelo_seleccionado[0]}\nNombre de la marca: {modelo_seleccionado[1]}\nCantidad asientos clase ejecutiva: {modelo_seleccionado[2]}\nCantidad asientos clase turista: {modelo_seleccionado[3]}\nCantidad asientos clase economica: {modelo_seleccionado[4]}\n")
    while True:
        print("====== Opciones disponibles ======")
        print("(1) Editar nombre")
        print("(2) Editar marca")
        print("(3) Editar cantidad asientos")
        print("(4) Regresar al menú gestión de modelos")
        opcion_ingresada = input("Ingrese una opción: ")
        if opcion_ingresada != "":
            try:
                opcion_ingresada = int(opcion_ingresada)
            except:
                print("Error: la opción debe ser un número\n")
                continue
            if opcion_ingresada == 1:
                return modificar_modelo_nombre(modelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif opcion_ingresada == 2:
                return modificar_modelo_marca(modelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif opcion_ingresada == 3:
                return modificar_modelo_asientos(modelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif opcion_ingresada == 4:
                return 
        else:
            print("Error: la opción ingresada no puede ser vacio")

def modificar_modelo_nombre(modelo_seleccionado, contenido_anterior, indice_seleccionado):
    modelo_valido = False
    while not modelo_valido:
        modelo_ingresado = input("\nIngrese el nuevo nombre del modelo o (s para regresar o enter para mantener el nombre actual): ")
        if modelo_ingresado == "":
            modelo_ingresado = modelo_seleccionado[0]
            modelo_valido = True
        else:
            if existe_modelo(modelo_ingresado) and modelo_ingresado != modelo_seleccionado[0]:
                print("Error: el nombre de este modelo ya existe")
            elif modelo_ingresado == "s":
                return modificar_modelo_aux(modelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif not validar_nombre_modelo(modelo_ingresado):
                print("Error: el nombre del modelo no puede ser solo números o de un solo caracter")
            else:
                modelo_valido = True

    datos_modelo = contenido_anterior[indice_seleccionado].split(";")
    datos_modelo[0] = modelo_ingresado.strip()
    contenido_anterior[indice_seleccionado] = f"{datos_modelo[0]};{datos_modelo[1]};{datos_modelo[2]};{datos_modelo[3]};{datos_modelo[4]}"
    print("\nNombre del modelo modificado exitosamente")
    reescribir_modelos(contenido_anterior)
    return modificar_modelo_aux(contenido_anterior[indice_seleccionado].split(";"), contenido_anterior, indice_seleccionado)

def modificar_modelo_marca(modelo_seleccionado, contenido_anterior, indice_seleccionado):
    mostrar_marcas()
    contenido_marcas = cargar_marcas()
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el número de opcion de la marca que desea usar (0 para regresar o enter para mantener): ")
        if indice_ingresado == "":
            marca_seleccionada = modelo_seleccionado[1]
            indice_valido = True
        else:
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: el número de opción debe ser un valor númerico")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(contenido_marcas):
                print("Error: la opcion ingresada no existe")
            elif indice_ingresado == 0:
                return modificar_modelo_aux(modelo_seleccionado, contenido_anterior, indice_seleccionado)
            else:
                marca_seleccionada = contenido_marcas[indice_ingresado-1]
                if marca_seleccionada == modelo_seleccionado[1]:
                    print("Error: esta marca ya esta asociada a este modelo")
                else:
                    indice_valido = True

    datos_modelo = contenido_anterior[indice_seleccionado].split(";")
    datos_modelo[1] = marca_seleccionada
    contenido_anterior[indice_seleccionado] = f"{datos_modelo[0]};{datos_modelo[1]};{datos_modelo[2]};{datos_modelo[3]};{datos_modelo[4]}"
    print("\nMarca modificada exitosamente")
    reescribir_modelos(contenido_anterior)
    return modificar_modelo_aux(contenido_anterior[indice_seleccionado].split(";"), contenido_anterior, indice_seleccionado)

def modificar_modelo_asientos(modelo_seleccionado, contenido_anterior, indice_seleccionado):
    asiento_valido = False
    while not asiento_valido:
        cantidad_ingresada = input("Ingrese la nueva cantidad de asientos para la clase ejecutiva (-1 para regresar o enter para mantener la cantidad actual): ")
        if cantidad_ingresada == "":
            asientos_clase_ejecutiva = modelo_seleccionado[2]
            asiento_valido = True
        else:
            try:
                cantidad_ingresada = int(cantidad_ingresada)
            except:
                print("Error: el número de asientos debe ser un valor númerico")
                continue
            if cantidad_ingresada == -1:
                return modificar_modelo_aux(modelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif cantidad_ingresada <= 0:
                print("Error: la cantidad de asientos no puede menor a 0")
            else:
                asientos_clase_ejecutiva = cantidad_ingresada
                asiento_valido = True

    asiento_valido = False
    while not asiento_valido:
        cantidad_ingresada = input("Ingrese la nueva cantidad de asientos para la clase turista (-1 para regresar o enter para mantener la cantidad actual): ")
        if cantidad_ingresada == "":
            asientos_clase_turista = modelo_seleccionado[3]
            asiento_valido = True
        else:
            try:
                cantidad_ingresada = int(cantidad_ingresada)
            except:
                print("Error: el número de asientos debe ser un valor númerico")
                continue
            if cantidad_ingresada == -1:
                return modificar_modelo_aux(modelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif cantidad_ingresada <= 0:
                print("Error: la cantidad de asientos no puede menor a 0")
            else:
                asientos_clase_turista = cantidad_ingresada
                asiento_valido = True
        
    asiento_valido = False
    while not asiento_valido:
        cantidad_ingresada = input("Ingrese la nueva cantidad de asientos para la clase economica (-1 para regresar o enter para mantener la cantidad actual): ")
        if cantidad_ingresada == "":
            asientos_clase_economica = modelo_seleccionado[4]
            asiento_valido = True
        else:
            try:
                cantidad_ingresada = int(cantidad_ingresada)
            except:
                print("Error: el número de asientos debe ser un valor númerico")
                continue
            if cantidad_ingresada == -1:
                return modificar_modelo_aux(modelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif cantidad_ingresada <= 0:
                print("Error: la cantidad de asientos no puede menor a 0")
            else:
                asientos_clase_economica = cantidad_ingresada
                asiento_valido = True

    datos_modelo = contenido_anterior[indice_seleccionado].split(";")
    datos_modelo[2] = asientos_clase_ejecutiva
    datos_modelo[3] = asientos_clase_turista
    datos_modelo[4] = asientos_clase_economica
    contenido_anterior[indice_seleccionado] = f"{datos_modelo[0]};{datos_modelo[1]};{datos_modelo[2]};{datos_modelo[3]};{datos_modelo[4]}"
    reescribir_modelos(contenido_anterior)
    print(f"Cantidad de asientos actualizada exitosamente")
    return modificar_modelo_aux(contenido_anterior[indice_seleccionado].split(";"), contenido_anterior, indice_seleccionado)

def menu_gestion_aerolineas():
    while True:
        print("\nPanel de administrador - gestión marcas")
        print("====== Opciones disponibles ======")
        print("(1) Incluir aerolínea")
        print("(2) Eliminar aerolínea")
        print("(3) Modificar aerolínea")
        print("(4) Mostrar aerolíneas")
        print("(5) Regresar al menú principal")
        opcion_ingresada = input("Ingresa una opción: ")
        aerolineas = cargar_aerolineas()
        if opcion_ingresada != "":
            try:
                opcion_ingresada = int(opcion_ingresada)
            except:
                print("Error: la opción debe ser un número\n")
                continue
            if opcion_ingresada == 1:
                incluir_aerolinea()
            elif opcion_ingresada == 2:
                if not aerolineas:
                    print("Error: no hay aerolíneas registradas")
                else:
                    eliminar_aerolinea()
            elif opcion_ingresada == 3:
                if not aerolineas:
                    print("Error: no hay aerolíneas registradas")
                else:
                    modificar_aerolinea()
            elif opcion_ingresada == 4:
                if not aerolineas:
                    print("Error: no hay aerolíneas registradas para mostrar")
                else:
                    mostrar_aerolineas()
            elif opcion_ingresada == 5: 
                break
            else:
                print("Error: la opción ingresada no existe\n")
        else:
            print("Error: la opción ingresada no puede ser vacio")


def incluir_aerolinea():
    aerolinea_valida = False
    while not aerolinea_valida:
        aerolinea_ingresada = input("\nIngrese el nombre de la aerolinea (o s para regresar): ")
        if aerolinea_ingresada != "":
            if existe_aerolinea(aerolinea_ingresada):
                print("Error: esta aerolínea ya existe")
            elif aerolinea_ingresada == "s":
                return
            elif not validar_nombre_aerolinea(aerolinea_ingresada):
                print("Error: el nombre de la aerolínea no puede ser solo números o de un solo caracter")
            else:
                aerolinea_valida = True
        else:
            print("Error: la aerolínea ingresada no puede ser vacio")

    centro_operaciones_valido = False
    while not centro_operaciones_valido:
        centro_operaciones_ingresado = input("Ingrese el nombre del centro de operaciones (o s para regresar): ")
        if centro_operaciones_ingresado != "":
            if centro_operaciones_ingresado == "s":
                return
            elif not validar_nombre_centro_operaciones(centro_operaciones_ingresado):
                print("Error: el nombre del centro de operaciones no puede ser solo números o de un solo caracter")
            else:
                centro_operaciones_valido = True
        else:
            print("Error: el centro de operaciones ingresado no puede ser vacio")

    guardar_aerolinea(aerolinea_ingresada,centro_operaciones_ingresado)
    print(f"Aerolínea {aerolinea_ingresada} agregada exitosamente")
    return 

def eliminar_aerolinea():
    mostrar_aerolineas()
    contenido_anterior = cargar_aerolineas()
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingresé el número de opción de la aerolínea que desea eliminar (o 0 para regresar): ")
        if indice_ingresado != "":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: el número de opción debe ser un valor númerico")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(contenido_anterior):
                print("Error: la opción ingresada no existe")
            elif indice_ingresado == 0:
                return
            elif existe_aerolinea_asociada(contenido_anterior[indice_ingresado-1].split(";")[0]):
                print("Error: no se puede eliminar ya que esta asociada a un avion")
            else:
                indice_valido = True
        else: 
            print("Error: la opción ingresada no puede ser vacio")
            
    
    contenido_nuevo = contenido_anterior[:indice_ingresado-1] + contenido_anterior[indice_ingresado:]
    reescribir_aerolineas(contenido_nuevo)
    print(f"\nAerolínea:\nnombre aerolínea: {contenido_anterior[indice_ingresado-1].strip().split(";")[0]}\ncentro de operaciones en: {contenido_anterior[indice_ingresado-1].strip().split(";")[1]}\neliminada exitosamente")
    mostrar_aerolineas()
    return


def modificar_aerolinea():
    mostrar_aerolineas()
    contenido_anterior = cargar_aerolineas()

    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el número de opción de la aerolínea que desea editar (0 para regresar): ")
        if indice_ingresado !="":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: el número de opción debe ser un valor númerico")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(contenido_anterior):
                print("Error: la opcion ingresada no existe")
            elif indice_ingresado == 0:
                return 
            else:
                indice_valido = True
        else:
            print("Error: el número de opción no puede ser vacio")
    
    aerolinea_valida = False
    aerolinea_actual = contenido_anterior[indice_ingresado-1]
    while not aerolinea_valida:
        aerolinea_ingresada = input("Ingrese el nuevo nombre de la aerolínea (s para regresar o enter para mantener el nombre de la aerolinéa actual): ")
        if aerolinea_ingresada == "":
            aerolinea_ingresada = aerolinea_actual
            aerolinea_valida = True
        else:
            if existe_aerolinea(aerolinea_ingresada) and aerolinea_ingresada != aerolinea_actual:
                print("Error: esta aerolínea ya existe")
            elif aerolinea_ingresada == "s":
                return 
            elif not validar_nombre_aerolinea(aerolinea_ingresada):
                print("Error: el nombre de la aerolínea no puede ser solo números o de un solo caracter")
            else:
                aerolinea_valida = True

    centro_operaciones_valido = False
    datos_aerolinea = contenido_anterior[indice_ingresado-1].strip().split(";")
    centro_operaciones_actual = datos_aerolinea[1]
    while not centro_operaciones_valido:
        centro_operaciones_ingresado = input("Ingrese el nuevo nombre del centro de operaciones (s para regresar o enter para mantener el nombre del centro de operaciones actual): ")
        if centro_operaciones_ingresado == "":
            centro_operaciones_ingresado = centro_operaciones_actual
            centro_operaciones_valido = True
        else:
            if aerolinea_ingresada == "s":
                return 
            elif not validar_nombre_centro_operaciones(centro_operaciones_ingresado):
                print("Error: el centro de operaciones ingresado no puede ser vacio")
            else:
                centro_operaciones_valido = True

    datos_aerolinea[0] = aerolinea_ingresada
    datos_aerolinea[1] = centro_operaciones_ingresado
    contenido_anterior[indice_ingresado-1] = f"{datos_aerolinea[0]};{datos_aerolinea[1]}"
    reescribir_aerolineas(contenido_anterior)
    print(f"Aerolinea actualizada exitosamente")
    return



