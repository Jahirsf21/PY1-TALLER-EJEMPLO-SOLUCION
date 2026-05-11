from validadores import *
from acceso_datos import *
from vistas import *

def menu_principal():
    while True:
        print("\nSistema de reservacion de vuelos")
        print("Opciones disponibles")
        print("--------------------")
        print("1) Opciones administrativas")
        print("2) Opciones de usuario")
        print("3) Salir")
        opcion_ingresada = input("Ingrese una opcion: ")
        if opcion_ingresada != "":
            try:
                opcion_ingresada = int(opcion_ingresada)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if opcion_ingresada == 1:
                if control_acceso() == 1:
                    menu_administrador()
            elif opcion_ingresada == 2:
                "menu_usuario()"
            elif opcion_ingresada == 3:
                exit()
            else:
                print("Error: la opcion ingresada no existe.")
        else:
            print("Error: la opcion no puede estar vacia.")

def menu_administrador():
    while True:
        print("\nPanel de administrador")
        print("Opciones disponibles")
        print("--------------------")
        print("1) Gestion de marcas de aviones")
        print("2) Gestion de modelos de aviones")
        print("3) Gestion de aerolineas")
        print("4) Gestion de aviones por aerolinea")
        print("5) Gestion de vuelos")
        print("6) Estadisticas de vuelo")
        print("7) Consultar historial de reservaciones")
        print("8) Regresar al menu principal")
        opcion_ingresada = input("Ingrese una opcion: ")
        if opcion_ingresada != "":
            try:
                opcion_ingresada = int(opcion_ingresada)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if opcion_ingresada == 1:
                menu_gestion_marcas()
            elif opcion_ingresada == 2:
                menu_gestion_modelos()
            elif opcion_ingresada == 3:
                menu_gestion_aerolineas()
            elif opcion_ingresada == 4:
                menu_gestion_aviones_aerolineas()
            elif opcion_ingresada == 5:
                menu_gestion_vuelos()
            elif opcion_ingresada == 6:
                ""
            elif opcion_ingresada == 7:
                "hola"
            elif opcion_ingresada == 8: 
                break
            else:
                print("Error: la opcion ingresada no existe.")
        else:
            print("Error: la opcion no puede estar vacia.")

def menu_gestion_marcas():
    while True:
        print("\nAdministrador - Gestion de marcas")
        print("Opciones disponibles")
        print("--------------------")
        print("1) Incluir marca")
        print("2) Eliminar marca")
        print("3) Modificar marca")
        print("4) Mostrar marcas")
        print("5) Regresar al menu principal")
        marcas = cargar_marcas()
        opcion_ingresada = input("Ingrese una opcion: ")
        if opcion_ingresada != "":
            try:
                opcion_ingresada = int(opcion_ingresada)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if opcion_ingresada == 1:
                incluir_marca()
            elif opcion_ingresada == 2:
                if not marcas:
                    print("Error: no hay marcas registradas para eliminar.")
                else:
                    eliminar_marca(marcas)
            elif opcion_ingresada == 3:
                if not marcas:
                    print("Error: no hay marcas registradas para modificar.")
                else:
                    modificar_marca(marcas)
            elif opcion_ingresada == 4:
                if not marcas:
                    print("Error: no hay marcas registradas para mostrar.")
                else:
                    mostrar_marcas()
            elif opcion_ingresada == 5: 
                break
            else:
                print("Error: la opcion ingresada no existe.")
        else:
            print("Error: la opcion no puede estar vacia.")

def incluir_marca():
    marca_valida = False
    while not marca_valida:
        marca_ingresada = input("Ingrese el nombre de la marca (s para regresar): ")
        if marca_ingresada != "":
            if existe_marca(marca_ingresada):
                print("Error: la marca ya existe.")
            elif marca_ingresada == "s":
                return 
            elif not validar_nombre_marca(marca_ingresada):
                print("Error: el nombre de la marca no puede ser solo numeros ni de un solo caracter.")
            else:
                marca_valida = True
        else:
            print("Error: la marca no puede estar vacia.")

    guardar_marca(marca_ingresada)
    print(f"Marca {marca_ingresada} agregada exitosamente")
    mostrar_marcas()
    return 

def eliminar_marca(contenido_anterior):
    mostrar_marcas()
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el numero de opcion de la marca que desea eliminar (0 para regresar): ")
        if indice_ingresado != "":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(contenido_anterior):
                print("Error: la opcion ingresada no existe.")
            elif indice_ingresado == 0:
                return 
            elif existe_marca_asociada(contenido_anterior[indice_ingresado-1]):
                print("Error: no se puede eliminar; esta asociada a un modelo.")
            else:
                indice_valido = True
        else:
            print("Error: la opcion no puede estar vacia.")

    contenido_nuevo = contenido_anterior[:indice_ingresado-1] + contenido_anterior[indice_ingresado:]
    reescribir_marcas(contenido_nuevo)
    print("Marca eliminada exitosamente")
    mostrar_marcas()
    return 
        
def modificar_marca(contenido_anterior):
    mostrar_marcas()
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el numero de opcion de la marca que desea editar (0 para regresar): ")
        if indice_ingresado !="":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(contenido_anterior):
                print("Error: la opcion ingresada no existe.")
            elif indice_ingresado == 0:
                return 
            else:
                indice_valido = True
        else:
            print("Error: la opcion no puede estar vacia.")
    
    marca_valida = False
    marca_actual = contenido_anterior[indice_ingresado-1]
    while not marca_valida:
        marca_ingresada = input("Ingrese el nuevo nombre de la marca (s para regresar, enter para mantener el nombre actual): ")
        if marca_ingresada == "":
            marca_ingresada = marca_actual
            marca_valida = True
        else:
            if existe_marca(marca_ingresada) and marca_ingresada != marca_actual:
                print("Error: la marca ya existe.")
            elif marca_ingresada == "s":
                return 
            elif not validar_nombre_marca(marca_ingresada):
                print("Error: el nombre de la marca no puede ser solo numeros ni de un solo caracter.")
            else:
                marca_valida = True

    contenido_anterior[indice_ingresado-1] = marca_ingresada.strip()
    reescribir_marcas(contenido_anterior)
    print("Marca modificada exitosamente")
    mostrar_marcas()
    return

def menu_gestion_modelos():
    while True:
        print("\nAdministrador - Gestion de modelos")
        print("Opciones disponibles")
        print("--------------------")
        print("1) Incluir modelo")
        print("2) Eliminar modelo")
        print("3) Modificar modelo")
        print("4) Mostrar modelos")
        print("5) Regresar al menu principal")
        marcas = cargar_marcas()
        modelos = cargar_modelos()
        opcion_ingresada = input("Ingrese una opcion: ")
        if opcion_ingresada != "":
            try:
                opcion_ingresada = int(opcion_ingresada)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if opcion_ingresada == 1:
                if not marcas:
                    print("Error: no hay marcas registradas para crear modelos.")
                else:
                    incluir_modelo(marcas)
            elif opcion_ingresada == 2:
                if not modelos:
                    print("Error: no hay modelos registrados.")
                else:
                    eliminar_modelo(modelos)
            elif opcion_ingresada == 3:
                if not modelos:
                    print("Error: no hay modelos registrados.")
                elif not marcas:
                    print("Error: no hay marcas registradas.")
                else:
                    modificar_modelo(modelos)
            elif opcion_ingresada == 4:
                if not modelos:
                    print("Error: no hay modelos registrados para mostrar.")
                else:
                    mostrar_modelos()
            elif opcion_ingresada == 5: 
                break
            else:
                print("Error: la opcion ingresada no existe.")
        else:
            print("Error: la opcion no puede estar vacia.")

def incluir_modelo(contenido_marcas):
    modelo_valido = False
    while not modelo_valido:
        modelo_ingresado = input("Ingrese el nombre del modelo (s para regresar): ")
        if modelo_ingresado != "":
            if existe_modelo(modelo_ingresado):
                print("Error: el nombre del modelo ya existe.")
            elif modelo_ingresado == "s":
                return 
            elif not validar_nombre_modelo(modelo_ingresado):
                print("Error: el nombre del modelo no puede ser solo numeros ni de un solo caracter.")
            else:
                modelo_valido = True
        else:
            print("Error: el nombre del modelo no puede estar vacio.")
            
    mostrar_marcas()
    indice_valido = False

    while not indice_valido:
        indice_ingresado = input("Ingrese el numero de opcion de la marca que desea usar (0 para regresar): ")
        if indice_ingresado !="":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(contenido_marcas):
                print("Error: la opcion ingresada no existe.")
            elif indice_ingresado == 0:
                return 
            else:
                indice_valido = True
                marca_seleccionada = contenido_marcas[indice_ingresado-1]
        else:
            print("Error: la opcion no puede estar vacia.")

    asiento_valido = False
    while not asiento_valido:
        cantidad_ingresada = input("Ingrese la cantidad de asientos para la clase ejecutiva (-1 para regresar): ")
        if cantidad_ingresada != "":
            try:
                cantidad_ingresada = int(cantidad_ingresada)
            except:
                print("Error: la cantidad de asientos debe ser un numero.")
                continue
            if cantidad_ingresada == -1:
                return 
            elif cantidad_ingresada <= 0:
                print("Error: la cantidad de asientos no puede ser menor que 0.")
            else:
                asiento_valido = True
        else:
            print("Error: la cantidad de asientos no puede estar vacia.")
    asientos_clase_ejecutiva = cantidad_ingresada

    asiento_valido = False
    while not asiento_valido:
        cantidad_ingresada = input("Ingrese la cantidad de asientos para la clase turista (-1 para regresar): ")
        if cantidad_ingresada != "":
            try:
                cantidad_ingresada = int(cantidad_ingresada)
            except:
                print("Error: la cantidad de asientos debe ser un numero.")
                continue
            if cantidad_ingresada == -1:
                return 
            elif cantidad_ingresada <= 0:
                print("Error: la cantidad de asientos no puede ser menor que 0.")
            else:
                asiento_valido = True
        else:
            print("Error: la cantidad de asientos no puede estar vacia.")
    asientos_clase_turista = cantidad_ingresada

    asiento_valido = False
    while not asiento_valido:
        cantidad_ingresada = input("Ingrese la cantidad de asientos para la clase economica (-1 para regresar): ")
        if cantidad_ingresada != "":
            try:
                cantidad_ingresada = int(cantidad_ingresada)
            except:
                print("Error: la cantidad de asientos debe ser un numero.")
                continue
            if cantidad_ingresada == -1:
                return 
            elif cantidad_ingresada <= 0:
                print("Error: la cantidad de asientos no puede ser menor que 0.")
            else:
                asiento_valido = True
        else:
            print("Error: la cantidad de asientos no puede estar vacia.")

    asientos_clase_economica = cantidad_ingresada
    guardar_modelo(modelo_ingresado.strip(),marca_seleccionada,asientos_clase_ejecutiva,asientos_clase_turista,asientos_clase_economica)
    print(f"\nNombre del modelo: {modelo_ingresado.strip()}\nNombre de la marca: {marca_seleccionada}\nCantidad asientos clase ejecutiva: {asientos_clase_ejecutiva}\nCantidad asientos clase turista: {asientos_clase_turista}\nCantidad asientos clase economica: {asientos_clase_economica}\nNuevo modelo agregado exitosamente")
    modelo_valido = True
    mostrar_modelos()
    return 

def eliminar_modelo(contenido_anterior):
    mostrar_modelos()       
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el numero de opcion del modelo que desea eliminar (0 para regresar): ")
        if indice_ingresado != "":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(contenido_anterior):
                print("Error: la opcion ingresada no existe.")
            elif indice_ingresado == 0:
                return 
            elif existe_modelo_asociado((contenido_anterior[indice_ingresado-1]).split(";")[0]):
                print("Error: no se puede eliminar; esta asociado a un avion.")
            else:
                indice_valido = True
        else:
            print("Error: la opcion no puede estar vacia.")

    contenido_nuevo = contenido_anterior[:indice_ingresado-1] + contenido_anterior[indice_ingresado:]
    reescribir_modelos(contenido_nuevo)
    print(f"Modelo {contenido_anterior[indice_ingresado-1]} eliminado con exito")
    mostrar_modelos()
    return 

def modificar_modelo(contenido_anterior):
    mostrar_modelos()
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el numero de opcion del modelo que desea modificar (0 para regresar): ")
        if indice_ingresado != "":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(contenido_anterior):
                print("Error: la opcion ingresada no existe.")
            elif indice_ingresado == 0:
                return 
            else:
                indice_valido = True
        else:
            print("Error: la opcion no puede estar vacia.")

    modelo_seleccionado = contenido_anterior[indice_ingresado-1].split(";")
    return modificar_modelo_aux(modelo_seleccionado, contenido_anterior, indice_ingresado-1)

def modificar_modelo_aux(modelo_seleccionado, contenido_anterior, indice_seleccionado):
    print(f"\nModelo seleccionado para editar:\nNombre modelo: {modelo_seleccionado[0]}\nNombre de la marca: {modelo_seleccionado[1]}\nCantidad asientos clase ejecutiva: {modelo_seleccionado[2]}\nCantidad asientos clase turista: {modelo_seleccionado[3]}\nCantidad asientos clase economica: {modelo_seleccionado[4]}\n")
    while True:
        print("Opciones disponibles")
        print("--------------------")
        print("1) Editar nombre")
        print("2) Editar marca")
        print("3) Editar cantidad asientos")
        print("4) Regresar al menu de gestion de modelos")
        marcas = cargar_marcas()
        opcion_ingresada = input("Ingrese una opcion: ")
        if opcion_ingresada != "":
            try:
                opcion_ingresada = int(opcion_ingresada)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if opcion_ingresada == 1:
                return modificar_modelo_nombre(modelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif opcion_ingresada == 2:
                return modificar_modelo_marca(modelo_seleccionado, contenido_anterior, indice_seleccionado, marcas)
            elif opcion_ingresada == 3:
                return modificar_modelo_asientos(modelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif opcion_ingresada == 4:
                return 
        else:
            print("Error: la opcion no puede estar vacia.")

def modificar_modelo_nombre(modelo_seleccionado, contenido_anterior, indice_seleccionado):
    modelo_valido = False
    while not modelo_valido:
        modelo_ingresado = input("\nIngrese el nuevo nombre del modelo (s para regresar, enter para mantener el nombre actual): ")
        if modelo_ingresado == "":
            modelo_ingresado = modelo_seleccionado[0]
            modelo_valido = True
        else:
            if existe_modelo(modelo_ingresado) and modelo_ingresado != modelo_seleccionado[0]:
                print("Error: el nombre del modelo ya existe.")
            elif modelo_ingresado == "s":
                return modificar_modelo_aux(modelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif not validar_nombre_modelo(modelo_ingresado):
                print("Error: el nombre del modelo no puede ser solo numeros ni de un solo caracter.")
            else:
                modelo_valido = True

    datos_modelo = contenido_anterior[indice_seleccionado].split(";")
    datos_modelo[0] = modelo_ingresado.strip()
    contenido_anterior[indice_seleccionado] = f"{datos_modelo[0]};{datos_modelo[1]};{datos_modelo[2]};{datos_modelo[3]};{datos_modelo[4]}"
    print("\nNombre del modelo modificado exitosamente")
    reescribir_modelos(contenido_anterior)
    return modificar_modelo_aux(contenido_anterior[indice_seleccionado].split(";"), contenido_anterior, indice_seleccionado)

def modificar_modelo_marca(modelo_seleccionado, contenido_anterior, indice_seleccionado, contenido_marcas):
    mostrar_marcas()
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el numero de opcion de la marca que desea usar (0 para regresar, enter para mantener): ")
        if indice_ingresado == "":
            marca_seleccionada = modelo_seleccionado[1]
            indice_valido = True
        else:
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(contenido_marcas):
                print("Error: la opcion ingresada no existe.")
            elif indice_ingresado == 0:
                return modificar_modelo_aux(modelo_seleccionado, contenido_anterior, indice_seleccionado)
            else:
                marca_seleccionada = contenido_marcas[indice_ingresado-1]
                if marca_seleccionada == modelo_seleccionado[1]:
                    print("Error: esa marca ya esta asociada a este modelo.")
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
        cantidad_ingresada = input("Ingrese la nueva cantidad de asientos para la clase ejecutiva (-1 para regresar, enter para mantener la cantidad actual): ")
        if cantidad_ingresada == "":
            asientos_clase_ejecutiva = modelo_seleccionado[2]
            asiento_valido = True
        else:
            try:
                cantidad_ingresada = int(cantidad_ingresada)
            except:
                print("Error: la cantidad de asientos debe ser un numero.")
                continue
            if cantidad_ingresada == -1:
                return modificar_modelo_aux(modelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif cantidad_ingresada <= 0:
                print("Error: la cantidad de asientos no puede ser menor que 0.")
            else:
                asientos_clase_ejecutiva = cantidad_ingresada
                asiento_valido = True

    asiento_valido = False
    while not asiento_valido:
        cantidad_ingresada = input("Ingrese la nueva cantidad de asientos para la clase turista (-1 para regresar, enter para mantener la cantidad actual): ")
        if cantidad_ingresada == "":
            asientos_clase_turista = modelo_seleccionado[3]
            asiento_valido = True
        else:
            try:
                cantidad_ingresada = int(cantidad_ingresada)
            except:
                print("Error: la cantidad de asientos debe ser un numero.")
                continue
            if cantidad_ingresada == -1:
                return modificar_modelo_aux(modelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif cantidad_ingresada <= 0:
                print("Error: la cantidad de asientos no puede ser menor que 0.")
            else:
                asientos_clase_turista = cantidad_ingresada
                asiento_valido = True
        
    asiento_valido = False
    while not asiento_valido:
        cantidad_ingresada = input("Ingrese la nueva cantidad de asientos para la clase economica (-1 para regresar, enter para mantener la cantidad actual): ")
        if cantidad_ingresada == "":
            asientos_clase_economica = modelo_seleccionado[4]
            asiento_valido = True
        else:
            try:
                cantidad_ingresada = int(cantidad_ingresada)
            except:
                print("Error: la cantidad de asientos debe ser un numero.")
                continue
            if cantidad_ingresada == -1:
                return modificar_modelo_aux(modelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif cantidad_ingresada <= 0:
                print("Error: la cantidad de asientos no puede ser menor que 0.")
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
        print("\nAdministrador - Gestion de aerolineas")
        print("Opciones disponibles")
        print("--------------------")
        print("1) Incluir aerolinea")
        print("2) Eliminar aerolinea")
        print("3) Modificar aerolinea")
        print("4) Mostrar aerolineas")
        print("5) Regresar al menu principal")
        opcion_ingresada = input("Ingrese una opcion: ")
        aerolineas = cargar_aerolineas()
        if opcion_ingresada != "":
            try:
                opcion_ingresada = int(opcion_ingresada)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if opcion_ingresada == 1:
                incluir_aerolinea()
            elif opcion_ingresada == 2:
                if not aerolineas:
                    print("Error: no hay aerolineas registradas.")
                else:
                    eliminar_aerolinea(aerolineas)
            elif opcion_ingresada == 3:
                if not aerolineas:
                    print("Error: no hay aerolineas registradas.")
                else:
                    modificar_aerolinea(aerolineas)
            elif opcion_ingresada == 4:
                if not aerolineas:
                    print("Error: no hay aerolineas registradas para mostrar.")
                else:
                    mostrar_aerolineas()
            elif opcion_ingresada == 5: 
                break
            else:
                print("Error: la opcion ingresada no existe.")
        else:
            print("Error: la opcion no puede estar vacia.")


def incluir_aerolinea():
    aerolinea_valida = False
    while not aerolinea_valida:
        aerolinea_ingresada = input("\nIngrese el nombre de la aerolinea (s para regresar): ")
        if aerolinea_ingresada != "":
            if existe_aerolinea(aerolinea_ingresada):
                print("Error: la aerolinea ya existe.")
            elif aerolinea_ingresada == "s":
                return
            elif not validar_nombre_aerolinea(aerolinea_ingresada):
                print("Error: el nombre de la aerolinea no puede ser solo numeros ni de un solo caracter.")
            else:
                aerolinea_valida = True
        else:
            print("Error: la aerolinea no puede estar vacia.")

    centro_operaciones_valido = False
    while not centro_operaciones_valido:
        centro_operaciones_ingresado = input("Ingrese el nombre del centro de operaciones (s para regresar): ")
        if centro_operaciones_ingresado != "":
            if centro_operaciones_ingresado == "s":
                return
            elif not validar_nombre_centro_operaciones(centro_operaciones_ingresado):
                print("Error: el centro de operaciones no puede ser solo numeros ni de un solo caracter.")
            else:
                centro_operaciones_valido = True
        else:
            print("Error: el centro de operaciones no puede estar vacio.")

    guardar_aerolinea(aerolinea_ingresada,centro_operaciones_ingresado)
    print(f"Aerolínea {aerolinea_ingresada} agregada exitosamente")
    return 

def eliminar_aerolinea(contenido_anterior):
    mostrar_aerolineas()
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el numero de opcion de la aerolinea que desea eliminar (0 para regresar): ")
        if indice_ingresado != "":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(contenido_anterior):
                print("Error: la opcion ingresada no existe.")
            elif indice_ingresado == 0:
                return
            elif existe_aerolinea_asociada(contenido_anterior[indice_ingresado-1].split(";")[0]):
                print("Error: no se puede eliminar; esta asociada a un avion.")
            else:
                indice_valido = True
        else: 
            print("Error: la opcion no puede estar vacia.")
            
    
    contenido_nuevo = contenido_anterior[:indice_ingresado-1] + contenido_anterior[indice_ingresado:]
    reescribir_aerolineas(contenido_nuevo)
    print(f"\nAerolínea:\nnombre aerolínea: {contenido_anterior[indice_ingresado-1].strip().split(";")[0]}\ncentro de operaciones en: {contenido_anterior[indice_ingresado-1].strip().split(";")[1]}\neliminada exitosamente")
    mostrar_aerolineas()
    return


def modificar_aerolinea(contenido_anterior):
    mostrar_aerolineas()

    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el numero de opcion de la aerolinea que desea editar (0 para regresar): ")
        if indice_ingresado !="":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(contenido_anterior):
                print("Error: la opcion ingresada no existe.")
            elif indice_ingresado == 0:
                return 
            else:
                indice_valido = True
        else:
            print("Error: la opcion no puede estar vacia.")
    
    aerolinea_valida = False
    datos_aerolinea = contenido_anterior[indice_ingresado-1].strip().split(";")
    aerolinea_actual = datos_aerolinea[0]

    while not aerolinea_valida:
        aerolinea_ingresada = input("Ingrese el nuevo nombre de la aerolinea (s para regresar, enter para mantener el nombre actual): ")
        if aerolinea_ingresada == "":
            aerolinea_ingresada = aerolinea_actual
            aerolinea_valida = True
        else:
            if existe_aerolinea(aerolinea_ingresada) and aerolinea_ingresada != aerolinea_actual:
                print("Error: la aerolinea ya existe.")
            elif aerolinea_ingresada == "s":
                return 
            elif not validar_nombre_aerolinea(aerolinea_ingresada):
                print("Error: el nombre de la aerolinea no puede ser solo numeros ni de un solo caracter.")
            else:
                aerolinea_valida = True

    centro_operaciones_valido = False
    centro_operaciones_actual = datos_aerolinea[1]

    while not centro_operaciones_valido:
        centro_operaciones_ingresado = input("Ingrese el nuevo nombre del centro de operaciones (s para regresar, enter para mantener el nombre actual): ")
        if centro_operaciones_ingresado == "":
            centro_operaciones_ingresado = centro_operaciones_actual
            centro_operaciones_valido = True
        else:
            if centro_operaciones_ingresado == "s":
                return 
            elif not validar_nombre_centro_operaciones(centro_operaciones_ingresado):
                print("Error: el centro de operaciones no es valido.")
            else:
                centro_operaciones_valido = True

    datos_aerolinea[0] = aerolinea_ingresada
    datos_aerolinea[1] = centro_operaciones_ingresado
    contenido_anterior[indice_ingresado-1] = f"{datos_aerolinea[0]};{datos_aerolinea[1]}"
    reescribir_aerolineas(contenido_anterior)
    print(f"Aerolinea actualizada exitosamente")
    return


def menu_gestion_aviones_aerolineas():
    while True:
        print("\nAdministrador - Gestion de aviones por aerolinea")
        print("Opciones disponibles")
        print("--------------------")
        print("1) Incluir avion")
        print("2) Eliminar avion")
        print("3) Modificar avion")
        print("4) Mostrar aviones")
        print("5) Regresar al menu principal")
        marcas = cargar_marcas()
        modelos = cargar_modelos()
        aerolineas = cargar_aerolineas()
        aviones = cargar_aviones()
        opcion_ingresada = input("Ingrese una opcion: ")
        if opcion_ingresada != "":
            try:
                opcion_ingresada = int(opcion_ingresada)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if opcion_ingresada == 1:
                if not marcas:
                    print("Error: no hay marcas registradas.")
                elif not modelos:
                    print("Error: no hay modelos registrados.")
                elif not aerolineas:
                    print("Error: no hay aerolineas registradas.")
                else:
                    incluir_avion(marcas, aerolineas)
            elif opcion_ingresada == 2:
                if not aviones:
                    print("Error: no hay aviones registrados para eliminar.")
                else:
                    eliminar_avion(aviones)
            elif opcion_ingresada == 3:
                if not aviones:
                    print("Error: no hay aviones registrados para modificar.")
                elif not marcas:
                    print("Error: no hay marcas registradas.")
                elif not modelos:
                    print("Error: no hay modelos registrados.")
                elif not aerolineas:
                    print("Error: no hay aerolineas registradas.")
                else:
                    modificar_avion(aviones)
            elif opcion_ingresada == 4:
                if not aviones:
                    print("Error: no hay aviones registrados para mostrar.")
                else:
                    mostrar_aviones()
            elif opcion_ingresada == 5: 
                break
            else:
                print("Error: la opcion ingresada no existe.")
        else:
            print("Error: la opcion no puede estar vacia.")

def incluir_avion(marcas, aerolineas):
    matricula_valida = False
    while not matricula_valida:
        matricula_ingresada = input("\nIngrese el numero de matricula (s para regresar): ")
        if matricula_ingresada != "":
            if existe_avion(matricula_ingresada):
                print("Error: la matricula ya existe.")
            elif matricula_ingresada == "s":
                return
            elif not validar_matricula(matricula_ingresada):
                print("Error: la matricula no puede ser de un solo caracter ni contener caracteres especiales.")
            else:
                matricula_valida = True
        else:
            print("Error: la matricula no puede estar vacia.")

    mostrar_marcas()

    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el numero de opcion de la marca que desea usar (0 para regresar): ")
        if indice_ingresado != "":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(marcas):
                print("Error: la opcion ingresada no existe.")
            elif indice_ingresado == 0:
                return
            elif not existe_marca_asociada(marcas[indice_ingresado-1]):
                print("Error: no se puede usar esta marca; no esta asociada a ningun modelo.")
            else:
                indice_valido = True

    marca_seleccionada = marcas[indice_ingresado-1]
    modelos_disponibles = mostrar_modelos_marcas(marca_seleccionada)

    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("\nIngrese el numero de opcion del modelo que desea usar (0 para regresar): ")
        if indice_ingresado != "":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(modelos_disponibles):
                print("Error: la opcion ingresada no existe.")
            elif indice_ingresado == 0:
                return
            else:
                indice_valido = True

    modelo_seleccionado = modelos_disponibles[indice_ingresado-1].strip().split(";")[0]

    año_valido = False
    while not año_valido:
        año_ingresado = input("\nIngrese el Año del avion (0 para regresar): ")
        if año_ingresado != "":
            try:
                año_ingresado = int(año_ingresado)
            except:
                print("Error: el Año ingresado debe ser un valor numerico.")
                continue
            if año_ingresado == 0:
                return
            elif año_ingresado < 1950 or año_ingresado > 2026:
                print("Error: el Año del avion debe estar entre 1950 y 2026.")
            else:
                año_valido = True
        else:
            print("Error: el Año no puede estar vacio.")

    mostrar_aerolineas()

    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("\nIngrese el numero de opcion de la aerolinea que desea usar (0 para regresar): ")
        if indice_ingresado != "":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(aerolineas):
                print("Error: la opcion ingresada no existe.")
            elif indice_ingresado == 0:
                return
            else:
                indice_valido = True

    aerolinea_seleccionada = aerolineas[indice_ingresado-1].strip().split(";")[0]
    datos = f"matricula: {matricula_ingresada} marca: {marca_seleccionada} modelo: {modelo_seleccionado} año {año_ingresado} aerolínea: {aerolinea_seleccionada}"
    guardar_avion(matricula_ingresada,marca_seleccionada,modelo_seleccionado,año_ingresado,aerolinea_seleccionada)
    print(f"\nInformación avion:\n{datos}\nAgregado exitosamente")
    return

def eliminar_avion(contenido_anterior):
    mostrar_aviones()

    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("\nIngrese el numero de opcion del avion que desea eliminar (0 para regresar): ")
        if indice_ingresado != "":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(contenido_anterior):
                print("Error: la opcion ingresada no existe.")
            elif indice_ingresado == 0:
                return
            elif existe_avion_asociado(contenido_anterior[indice_ingresado-1].split(";")[0]):
                print("Error: no se puede eliminar; esta asociado a un vuelo.")
            else:
                indice_valido = True
        else:
            print("Error: la opcion no puede estar vacia.")


    contenido_nuevo = contenido_anterior[:indice_ingresado-1] + contenido_anterior[indice_ingresado:]
    reescribir_aviones(contenido_nuevo)
    print(f"\nInformación avion:\nMatricula: {contenido_anterior[indice_ingresado-1].strip().split(";")[0]}\nMarca: {contenido_anterior[indice_ingresado-1].strip().split(";")[1]}\nModelo: {contenido_anterior[indice_ingresado-1].strip().split(";")[2]}\nAño: {contenido_anterior[indice_ingresado-1].strip().split(";")[3]}\nNombre aerolínea: {contenido_anterior[indice_ingresado-1].strip().split(";")[4]}\nEliminado exitosamente")
    mostrar_aviones()
    return

def modificar_avion(contenido_anterior):
    mostrar_aviones()
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el numero de opcion del avion que desea modificar (0 para regresar): ")
        if indice_ingresado != "":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(contenido_anterior):
                print("Error: la opcion ingresada no existe.")
            elif indice_ingresado == 0:
                return 
            else:
                indice_valido = True
        else:
            print("Error: la opcion no puede estar vacia.")

    avion_seleccionado = contenido_anterior[indice_ingresado-1].split(";")
    return modificar_avion_aux(avion_seleccionado, contenido_anterior, indice_ingresado-1)


def modificar_avion_aux(avion_seleccionado, contenido_anterior, indice_seleccionado):
    print(f"\nAvion seleccionado para editar:\nMatricula: {avion_seleccionado[0]}\nNombre de la marca: {avion_seleccionado[1]}\nNombre del modelo: {avion_seleccionado[2]}\nAño del avion: {avion_seleccionado[3]}\nNombre de la aerolínea a la que pertenece: {avion_seleccionado[4]}")
    while True:
        print("Opciones disponibles")
        print("--------------------")
        print("1) Editar matricula")
        print("2) Editar marca")
        print("3) Editar modelo")
        print("4) Editar Año")
        print("5) Editar aerolinea")
        print("6) Regresar al menu de gestion de aviones")
        marcas = cargar_marcas()
        aerolineas = cargar_aerolineas()
        opcion_ingresada = input("Ingrese una opcion: ")
        if opcion_ingresada != "":
            try:
                opcion_ingresada = int(opcion_ingresada)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if opcion_ingresada == 1:
                return modificar_avion_matricula(avion_seleccionado, contenido_anterior, indice_seleccionado)
            elif opcion_ingresada == 2:
                return modificar_avion_marca(avion_seleccionado,contenido_anterior,indice_seleccionado, marcas)
            elif opcion_ingresada == 3:
                return modificar_avion_modelo(avion_seleccionado, contenido_anterior, indice_seleccionado)
            elif opcion_ingresada == 4:
                return modificar_avion_año(avion_seleccionado, contenido_anterior, indice_seleccionado)
            elif opcion_ingresada == 5:
                return modificar_avion_aerolinea(avion_seleccionado, contenido_anterior, indice_seleccionado, aerolineas)
            elif opcion_ingresada == 6:
                return
        else:
            print("Error: la opcion no puede estar vacia.")

def modificar_avion_matricula(avion_seleccionado, contenido_anterior, indice_seleccionado):
    matricula_valida = False
    while not matricula_valida:
        matricula_ingresada = input("\nIngrese el nuevo numero de matricula (s para regresar, enter para mantener): ")
        if matricula_ingresada == "":
            matricula_ingresada = avion_seleccionado[0]
            matricula_valida = True
        else:
            if existe_avion(matricula_ingresada) and matricula_ingresada != avion_seleccionado[0]:
                print("Error: el numero de matricula ya existe.")
            elif matricula_ingresada == "s":
                return modificar_avion_aux(avion_seleccionado, contenido_anterior, indice_seleccionado)
            elif not validar_matricula(matricula_ingresada):
                print("Error: la matricula no puede ser de un solo caracter ni contener caracteres especiales.")
            else:
                matricula_valida = True
        
    datos_avion = contenido_anterior[indice_seleccionado].split(";")
    datos_avion[0] = matricula_ingresada.strip()
    contenido_anterior[indice_seleccionado] = f"{datos_avion[0]};{datos_avion[1]};{datos_avion[2]};{datos_avion[3]};{datos_avion[4]}"
    reescribir_aviones(contenido_anterior)
    print("\nMatricula del avion modificada exitosamente")
    return modificar_avion_aux(contenido_anterior[indice_seleccionado].split(";"), contenido_anterior, indice_seleccionado)

def modificar_avion_marca(avion_seleccionado, contenido_anterior, indice_seleccionado, marcas):
    mostrar_marcas()
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el numero de opcion de la nueva marca (0 para regresar, enter para mantener): ")
        if indice_ingresado == "":
            marca_seleccionada = avion_seleccionado[1]
            indice_valido = True
        else:
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(marcas):
                print("Error: la opcion ingresada no existe.")
            elif indice_ingresado == 0:
                return
            elif not existe_marca_asociada(marcas[indice_ingresado-1]):
                print("Error: no se puede usar esta marca; no esta asociada a ningun modelo.")
            else:
                marca_seleccionada = marcas[indice_ingresado-1]
                indice_valido = True

    datos_avion = contenido_anterior[indice_seleccionado].split(";")
    datos_avion[1] = marca_seleccionada
    contenido_anterior[indice_seleccionado] = f"{datos_avion[0]};{datos_avion[1]};{datos_avion[2]};{datos_avion[3]};{datos_avion[4]}"
    reescribir_aviones(contenido_anterior)
    print("\nMarca del avion modificada exitosamente")
    return modificar_avion_aux(contenido_anterior[indice_seleccionado].split(";"), contenido_anterior, indice_seleccionado)

def modificar_avion_modelo(avion_seleccionado, contenido_anterior, indice_seleccionado):
    modelos_disponibles = mostrar_modelos_marcas(avion_seleccionado[1])
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el numero de opcion del modelo (0 para regresar, enter para mantener): ")
        if indice_ingresado == "":
            modelo_seleccionado = avion_seleccionado[2]
            indice_valido = True
        else:
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(modelos_disponibles):
                print("Error: la opcion ingresada no existe.")
            elif indice_ingresado == 0:
                return modificar_avion_aux(avion_seleccionado, contenido_anterior, indice_seleccionado)
            else:
                modelo_seleccionado = modelos_disponibles[indice_ingresado-1].strip().split(";")[0]
                indice_valido = True

    datos_avion = contenido_anterior[indice_seleccionado].split(";")
    datos_avion[2] = modelo_seleccionado
    contenido_anterior[indice_seleccionado] = f"{datos_avion[0]};{datos_avion[1]};{datos_avion[2]};{datos_avion[3]};{datos_avion[4]}"
    reescribir_aviones(contenido_anterior)
    print("\nModelo del avion modificado exitosamente")
    return modificar_avion_aux(contenido_anterior[indice_seleccionado].split(";"), contenido_anterior, indice_seleccionado)

def modificar_avion_año(avion_seleccionado, contenido_anterior, indice_seleccionado):
    año_valido = False
    while not año_valido:
        año_ingresado = input("Ingrese el nuevo año del avion (0 para regresar, enter para mantener): ")
        if año_ingresado == "":
            año_ingresado = avion_seleccionado[3]
            año_valido = True
        else:
            try:
                año_ingresado = int(año_ingresado)
            except:
                print("Error: el año ingresado debe ser un valor numerico.")
                continue
            if año_ingresado == 0:
                return modificar_avion_aux(avion_seleccionado, contenido_anterior, indice_seleccionado)
            elif año_ingresado < 1950 or año_ingresado > 2026:
                print("Error: el año del avion debe estar entre 1950 y 2026.")
            else:
                año_valido = True

    datos_avion = contenido_anterior[indice_seleccionado].split(";")
    datos_avion[3] = año_ingresado
    contenido_anterior[indice_seleccionado] = f"{datos_avion[0]};{datos_avion[1]};{datos_avion[2]};{datos_avion[3]};{datos_avion[4]}"
    reescribir_aviones(contenido_anterior)
    print("\nAño del avion modificado exitosamente")
    return modificar_avion_aux(contenido_anterior[indice_seleccionado].split(";"), contenido_anterior, indice_seleccionado)

def modificar_avion_aerolinea(avion_seleccionado, contenido_anterior, indice_seleccionado, aerolineas):
    mostrar_aerolineas()
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el numero de opcion de la nueva aerolinea (0 para regresar, enter para mantener): ")
        if indice_ingresado == "":
            aerolinea_seleccionada = avion_seleccionado[4]
            indice_valido = True
        else:
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(aerolineas):
                print("Error: la opcion ingresada no existe.")
            elif indice_ingresado == 0:
                return modificar_avion_aux(avion_seleccionado, contenido_anterior, indice_seleccionado)
            else:
                aerolinea_seleccionada = aerolineas[indice_ingresado-1].strip().split(";")[0]
                indice_valido = True

    datos_avion = contenido_anterior[indice_seleccionado].split(";")
    datos_avion[4] = aerolinea_seleccionada
    contenido_anterior[indice_seleccionado] = f"{datos_avion[0]};{datos_avion[1]};{datos_avion[2]};{datos_avion[3]};{datos_avion[4]}"
    reescribir_aviones(contenido_anterior)
    print("\nAerolinea del avion modificada exitosamente")
    return modificar_avion_aux(contenido_anterior[indice_seleccionado].split(";"), contenido_anterior, indice_seleccionado)

def menu_gestion_vuelos():
    while True:
        print("\nAdministrador - Gestion de vuelos")
        print("Opciones disponibles")
        print("--------------------")
        print("1) Incluir vuelo")
        print("2) Eliminar vuelo")
        print("3) Modificar vuelo")
        print("4) Estadisticas vuelos")
        print("5) Regresar al menu principal")
        vuelos = cargar_vuelos()
        aviones = cargar_aviones()
        opcion_ingresada = input("Ingrese una opcion: ")
        if opcion_ingresada != "":
            try:
                opcion_ingresada = int(opcion_ingresada)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if opcion_ingresada == 1:
                if not aviones:
                    print("Error: no hay aviones registrados para incluirlos en un vuelo")
                else:
                    incluir_vuelo(vuelos)
            elif opcion_ingresada == 2:
                if not vuelos:
                    print("Error: no hay vuelos registrados para eliminar.")
                else:
                    eliminar_vuelo(vuelos)
            elif opcion_ingresada == 3:
                if not vuelos:
                    print("Error: no hay vuelos registrados para modificar.")
                elif not aviones:
                    print("Error: no hay aviones registrados para incluirlos en un vuelo")
                else:
                    modificar_vuelo(vuelos)
            elif opcion_ingresada == 4:
                if not vuelos:
                    print("Error: no hay vuelos registrados.")
                else:
                    ""
            elif opcion_ingresada == 5:
                break
            else:
                print("Error: la opcion ingresada no existe.")
        else:
            print("Error: la opcion no puede estar vacia.")

def generar_numero_vuelo(contenido_vuelos):
    cantidad_vuelos = 0
    if contenido_vuelos:
        for vuelo in contenido_vuelos:
            numero_vuelo = vuelo.strip().split(";")[0]
            if numero_vuelo.startswith("AV"):
                numero = numero_vuelo[2:]
                numero = int(numero)
                if numero > cantidad_vuelos:
                    cantidad_vuelos = numero
    numero_nuevo = cantidad_vuelos + 1
    return f"AV{numero_nuevo}"

def incluir_vuelo(contenido_vuelos):
    numero_vuelo = generar_numero_vuelo(contenido_vuelos)

    codigo_salida_valido = False
    while not codigo_salida_valido:
        codigo_ingresado = input("Ingrese el codigo de aeropuerto de salida (s para regresar): ")
        if codigo_ingresado == "s":
            return
        elif codigo_ingresado == "":
            print("Error: el codigo de aeropuerto no puede estar vacio.")
        elif not validar_codigo_aeropuerto(codigo_ingresado):
            print("Error: el codigo de aeropuerto no es valido.")
        else:
            codigo_salida = codigo_ingresado.upper().strip()
            codigo_salida_valido = True

    fecha_salida_valida = False
    while not fecha_salida_valida:
        fecha_ingresada = input("Ingrese la fecha de salida (DD/MM/AAAA) (s para regresar): ")
        if fecha_ingresada == "s":
            return
        elif fecha_ingresada == "":
            print("Error: la fecha de salida no puede estar vacia.")
        elif not validar_fecha(fecha_ingresada):
            print("Error: la fecha de salida no es valida.")
        else:
            fecha_salida = fecha_ingresada
            fecha_salida_valida = True

    hora_salida_valida = False
    while not hora_salida_valida:
        hora_ingresada = input("Ingrese la hora de salida (HH:MM) (s para regresar): ")
        if hora_ingresada == "s":
            return
        elif hora_ingresada == "":
            print("Error: la hora de salida no puede estar vacia.")
        elif not validar_hora(hora_ingresada):
            print("Error: la hora de salida no es valida.")
        else:
            hora_salida = hora_ingresada
            hora_salida_valida = True

    codigo_arribo_valido = False
    while not codigo_arribo_valido:
        codigo_ingresado = input("Ingrese el codigo de aeropuerto de arribo (s para regresar): ")
        if codigo_ingresado == "s":
            return
        elif codigo_ingresado == "":
            print("Error: el codigo de aeropuerto no puede estar vacio.")
        elif not validar_codigo_aeropuerto(codigo_ingresado):
            print("Error: el codigo de aeropuerto no es valido.")
        else:
            codigo_arribo = codigo_ingresado.upper().strip()
            codigo_arribo_valido = True

    fecha_arribo_valida = False
    while not fecha_arribo_valida:
        fecha_ingresada = input("Ingrese la fecha de arribo (DD/MM/AAAA) (s para regresar): ")
        if fecha_ingresada == "s":
            return
        elif fecha_ingresada == "":
            print("Error: la fecha de arribo no puede estar vacia.")
        elif not validar_fecha(fecha_ingresada):
            print("Error: la fecha de arribo no es valida.")
        else:
            fecha_arribo = fecha_ingresada
            fecha_arribo_valida = True

    hora_arribo_valida = False
    while not hora_arribo_valida:
        hora_ingresada = input("Ingrese la hora de arribo (HH:MM) (s para regresar): ")
        if hora_ingresada == "s":
            return
        elif hora_ingresada == "":
            print("Error: la hora de arribo no puede estar vacia.")
        elif not validar_hora(hora_ingresada):
            print("Error: la hora de arribo no es valida.")
        else:
            hora_arribo = hora_ingresada
            hora_arribo_valida = True

    aerolinea_valida = False
    while not aerolinea_valida:
        aerolineas = cargar_aerolineas()
        if not aerolineas:
            print("Error: no hay aerolineas registradas.")
            return
        mostrar_aerolineas()
        indice_ingresado = input("Ingrese el numero de opcion de la aerolinea (0 para regresar): ")
        if indice_ingresado != "":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(aerolineas):
                print("Error: la opcion ingresada no existe.")
            elif indice_ingresado == 0:
                return
            else:
                aerolinea_seleccionada = aerolineas[indice_ingresado-1].strip().split(";")[0]
                aviones_disponibles = mostrar_aviones_aerolinea(aerolinea_seleccionada)
                if not aviones_disponibles:
                    print("Error: no hay aviones registrados para esta aerolinea.")
                else:
                    aerolinea_valida = True
        else:
            print("Error: la opcion no puede estar vacia.")

    matricula_valida = False

    while not matricula_valida:
        indice_ingresado = input("Ingrese el numero de opcion de la matricula (0 para regresar): ")
        if indice_ingresado != "":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(aviones_disponibles):
                print("Error: la opcion ingresada no existe.")
            elif indice_ingresado == 0:
                return
            else:
                matricula_seleccionada = aviones_disponibles[indice_ingresado-1].strip().split(";")[0]
                matricula_valida = True
        else:
            print("Error: la opcion no puede estar vacia.")

    monto_ejecutiva_valido = False
    while not monto_ejecutiva_valido:
        monto_ingresado = input("Ingrese el monto para la clase ejecutiva (0 para regresar): ")
        if monto_ingresado == "0":
            return
        elif monto_ingresado == "":
            print("Error: el monto no puede estar vacio.")
        elif not validar_monto(monto_ingresado):
            print("Error: el monto debe ser un numero mayor que 0.")
        else:
            monto_ejecutiva = monto_ingresado
            monto_ejecutiva_valido = True

    monto_turista_valido = False
    while not monto_turista_valido:
        monto_ingresado = input("Ingrese el monto para la clase turista (0 para regresar): ")
        if monto_ingresado == "0":
            return
        elif monto_ingresado == "":
            print("Error: el monto no puede estar vacio.")
        elif not validar_monto(monto_ingresado):
            print("Error: el monto debe ser un numero mayor que 0.")
        else:
            monto_turista = monto_ingresado
            monto_turista_valido = True

    monto_economica_valido = False
    while not monto_economica_valido:
        monto_ingresado = input("Ingrese el monto para la clase economica (0 para regresar): ")
        if monto_ingresado == "0":
            return
        elif monto_ingresado == "":
            print("Error: el monto no puede estar vacio.")
        elif not validar_monto(monto_ingresado):
            print("Error: el monto debe ser un numero mayor que 0.")
        else:
            monto_economica = monto_ingresado
            monto_economica_valido = True

    guardar_vuelo(numero_vuelo,codigo_salida,fecha_salida,hora_salida,codigo_arribo,fecha_arribo,hora_arribo,aerolinea_seleccionada,matricula_seleccionada,monto_ejecutiva,monto_turista,monto_economica)
    print(f"\nInformacion del vuelo:\nNumero vuelo: {numero_vuelo}\nSalida: {codigo_salida} {fecha_salida} {hora_salida}\nArribo: {codigo_arribo} {fecha_arribo} {hora_arribo}\nAerolinea: {aerolinea_seleccionada} Matricula: {matricula_seleccionada}\nMontos: ejecutiva {monto_ejecutiva}, turista {monto_turista}, economica {monto_economica}\nVuelo agregado exitosamente")
    return

def eliminar_vuelo(contenido_anterior):
    mostrar_vuelos()
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el numero de opcion del vuelo que desea eliminar (0 para regresar): ")
        if indice_ingresado != "":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(contenido_anterior):
                print("Error: la opcion ingresada no existe.")
            elif indice_ingresado == 0:
                return
            else:
                indice_valido = True
        else:
            print("Error: la opcion no puede estar vacia.")

    vuelo_seleccionado = contenido_anterior[indice_ingresado-1].strip().split(";")
    contenido_nuevo = contenido_anterior[:indice_ingresado-1] + contenido_anterior[indice_ingresado:]
    reescribir_vuelos(contenido_nuevo)
    print(f"\nInformacion del vuelo:\nNumero vuelo: {vuelo_seleccionado[0]}\nSalida: {vuelo_seleccionado[1]} {vuelo_seleccionado[2]} {vuelo_seleccionado[3]}\nArribo: {vuelo_seleccionado[4]} {vuelo_seleccionado[5]} {vuelo_seleccionado[6]}\nAerolinea: {vuelo_seleccionado[7]} Matricula: {vuelo_seleccionado[8]}\nEliminado exitosamente")
    mostrar_vuelos()
    return

def modificar_vuelo(contenido_anterior):
    mostrar_vuelos()
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el numero de opcion del vuelo que desea modificar (0 para regresar): ")
        if indice_ingresado != "":
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(contenido_anterior):
                print("Error: la opcion ingresada no existe.")
            elif indice_ingresado == 0:
                return
            else:
                indice_valido = True
        else:
            print("Error: la opcion no puede estar vacia.")

    vuelo_seleccionado = contenido_anterior[indice_ingresado-1].split(";")
    return modificar_vuelo_aux(vuelo_seleccionado, contenido_anterior, indice_ingresado-1)

def modificar_vuelo_aux(vuelo_seleccionado, contenido_anterior, indice_seleccionado):
    print(f"\nVuelo seleccionado para editar:\nNumero vuelo: {vuelo_seleccionado[0]}\nSalida: {vuelo_seleccionado[1]} {vuelo_seleccionado[2]} {vuelo_seleccionado[3]}\nArribo: {vuelo_seleccionado[4]} {vuelo_seleccionado[5]} {vuelo_seleccionado[6]}\nAerolinea: {vuelo_seleccionado[7]} Matricula: {vuelo_seleccionado[8]}\nMontos: ejecutiva {vuelo_seleccionado[9]}, turista {vuelo_seleccionado[10]}, economica {vuelo_seleccionado[11]}\n")
    while True:
        print("Opciones disponibles")
        print("--------------------")
        print("1) Editar codigo de salida")
        print("2) Editar fecha de salida")
        print("3) Editar hora de salida")
        print("4) Editar codigo de arribo")
        print("5) Editar fecha de arribo")
        print("6) Editar hora de arribo")
        print("7) Editar aerolinea")
        print("8) Editar matricula")
        print("9) Editar monto clase ejecutiva")
        print("10) Editar monto clase turista")
        print("11) Editar monto clase economica")
        print("12) Regresar al menu de gestion de vuelos")
        opcion_ingresada = input("Ingrese una opcion: ")
        if opcion_ingresada != "":
            try:
                opcion_ingresada = int(opcion_ingresada)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if opcion_ingresada == 1:
                return modificar_vuelo_codigo_salida(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif opcion_ingresada == 2:
                return modificar_vuelo_fecha_salida(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif opcion_ingresada == 3:
                return modificar_vuelo_hora_salida(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif opcion_ingresada == 4:
                return modificar_vuelo_codigo_arribo(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif opcion_ingresada == 5:
                return modificar_vuelo_fecha_arribo(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif opcion_ingresada == 6:
                return modificar_vuelo_hora_arribo(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif opcion_ingresada == 7:
                return modificar_vuelo_aerolinea(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif opcion_ingresada == 8:
                return modificar_vuelo_matricula(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif opcion_ingresada == 9:
                return modificar_vuelo_monto_ejecutiva(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif opcion_ingresada == 10:
                return modificar_vuelo_monto_turista(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif opcion_ingresada == 11:
                return modificar_vuelo_monto_economica(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif opcion_ingresada == 12:
                return
        else:
            print("Error: la opcion no puede estar vacia.")

def modificar_vuelo_codigo_salida(vuelo_seleccionado, contenido_anterior, indice_seleccionado):
    codigo_valido = False
    while not codigo_valido:
        codigo_ingresado = input("\nIngrese el nuevo codigo de aeropuerto de salida (s para regresar, enter para mantener): ")
        if codigo_ingresado == "":
            codigo_ingresado = vuelo_seleccionado[1]
            codigo_valido = True
        else:
            if codigo_ingresado == "s":
                return modificar_vuelo_aux(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif not validar_codigo_aeropuerto(codigo_ingresado):
                print("Error: el codigo de aeropuerto no es valido.")
            else:
                codigo_ingresado = codigo_ingresado.upper().strip()
                codigo_valido = True

    datos_vuelo = contenido_anterior[indice_seleccionado].split(";")
    datos_vuelo[1] = codigo_ingresado
    contenido_anterior[indice_seleccionado] = f"{datos_vuelo[0]};{datos_vuelo[1]};{datos_vuelo[2]};{datos_vuelo[3]};{datos_vuelo[4]};{datos_vuelo[5]};{datos_vuelo[6]};{datos_vuelo[7]};{datos_vuelo[8]};{datos_vuelo[9]};{datos_vuelo[10]};{datos_vuelo[11]}"
    reescribir_vuelos(contenido_anterior)
    print("\nCodigo de salida modificado exitosamente")
    return modificar_vuelo_aux(contenido_anterior[indice_seleccionado].split(";"), contenido_anterior, indice_seleccionado)

def modificar_vuelo_fecha_salida(vuelo_seleccionado, contenido_anterior, indice_seleccionado):
    fecha_valida = False
    while not fecha_valida:
        fecha_ingresada = input("\nIngrese la nueva fecha de salida (DD/MM/AAAA) (s para regresar, enter para mantener): ")
        if fecha_ingresada == "":
            fecha_ingresada = vuelo_seleccionado[2]
            fecha_valida = True
        else:
            if fecha_ingresada == "s":
                return modificar_vuelo_aux(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif not validar_fecha(fecha_ingresada):
                print("Error: la fecha de salida no es valida.")
            else:
                fecha_valida = True

    datos_vuelo = contenido_anterior[indice_seleccionado].split(";")
    datos_vuelo[2] = fecha_ingresada
    contenido_anterior[indice_seleccionado] = f"{datos_vuelo[0]};{datos_vuelo[1]};{datos_vuelo[2]};{datos_vuelo[3]};{datos_vuelo[4]};{datos_vuelo[5]};{datos_vuelo[6]};{datos_vuelo[7]};{datos_vuelo[8]};{datos_vuelo[9]};{datos_vuelo[10]};{datos_vuelo[11]}"
    reescribir_vuelos(contenido_anterior)
    print("\nFecha de salida modificada exitosamente")
    return modificar_vuelo_aux(contenido_anterior[indice_seleccionado].split(";"), contenido_anterior, indice_seleccionado)

def modificar_vuelo_hora_salida(vuelo_seleccionado, contenido_anterior, indice_seleccionado):
    hora_valida = False
    while not hora_valida:
        hora_ingresada = input("\nIngrese la nueva hora de salida (HH:MM) (s para regresar, enter para mantener): ")
        if hora_ingresada == "":
            hora_ingresada = vuelo_seleccionado[3]
            hora_valida = True
        else:
            if hora_ingresada == "s":
                return modificar_vuelo_aux(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif not validar_hora(hora_ingresada):
                print("Error: la hora de salida no es valida.")
            else:
                hora_valida = True

    datos_vuelo = contenido_anterior[indice_seleccionado].split(";")
    datos_vuelo[3] = hora_ingresada
    contenido_anterior[indice_seleccionado] = f"{datos_vuelo[0]};{datos_vuelo[1]};{datos_vuelo[2]};{datos_vuelo[3]};{datos_vuelo[4]};{datos_vuelo[5]};{datos_vuelo[6]};{datos_vuelo[7]};{datos_vuelo[8]};{datos_vuelo[9]};{datos_vuelo[10]};{datos_vuelo[11]}"
    reescribir_vuelos(contenido_anterior)
    print("\nHora de salida modificada exitosamente")
    return modificar_vuelo_aux(contenido_anterior[indice_seleccionado].split(";"), contenido_anterior, indice_seleccionado)

def modificar_vuelo_codigo_arribo(vuelo_seleccionado, contenido_anterior, indice_seleccionado):
    codigo_valido = False
    while not codigo_valido:
        codigo_ingresado = input("\nIngrese el nuevo codigo de aeropuerto de arribo (s para regresar, enter para mantener): ")
        if codigo_ingresado == "":
            codigo_ingresado = vuelo_seleccionado[4]
            codigo_valido = True
        else:
            if codigo_ingresado == "s":
                return modificar_vuelo_aux(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif not validar_codigo_aeropuerto(codigo_ingresado):
                print("Error: el codigo de aeropuerto no es valido.")
            else:
                codigo_ingresado = codigo_ingresado.upper().strip()
                codigo_valido = True

    datos_vuelo = contenido_anterior[indice_seleccionado].split(";")
    datos_vuelo[4] = codigo_ingresado
    contenido_anterior[indice_seleccionado] = f"{datos_vuelo[0]};{datos_vuelo[1]};{datos_vuelo[2]};{datos_vuelo[3]};{datos_vuelo[4]};{datos_vuelo[5]};{datos_vuelo[6]};{datos_vuelo[7]};{datos_vuelo[8]};{datos_vuelo[9]};{datos_vuelo[10]};{datos_vuelo[11]}"
    reescribir_vuelos(contenido_anterior)
    print("\nCodigo de arribo modificado exitosamente")
    return modificar_vuelo_aux(contenido_anterior[indice_seleccionado].split(";"), contenido_anterior, indice_seleccionado)

def modificar_vuelo_fecha_arribo(vuelo_seleccionado, contenido_anterior, indice_seleccionado):
    fecha_valida = False
    while not fecha_valida:
        fecha_ingresada = input("\nIngrese la nueva fecha de arribo (DD/MM/AAAA) (s para regresar, enter para mantener): ")
        if fecha_ingresada == "":
            fecha_ingresada = vuelo_seleccionado[5]
            fecha_valida = True
        else:
            if fecha_ingresada == "s":
                return modificar_vuelo_aux(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif not validar_fecha(fecha_ingresada):
                print("Error: la fecha de arribo no es valida.")
            else:
                fecha_valida = True

    datos_vuelo = contenido_anterior[indice_seleccionado].split(";")
    datos_vuelo[5] = fecha_ingresada
    contenido_anterior[indice_seleccionado] = f"{datos_vuelo[0]};{datos_vuelo[1]};{datos_vuelo[2]};{datos_vuelo[3]};{datos_vuelo[4]};{datos_vuelo[5]};{datos_vuelo[6]};{datos_vuelo[7]};{datos_vuelo[8]};{datos_vuelo[9]};{datos_vuelo[10]};{datos_vuelo[11]}"
    reescribir_vuelos(contenido_anterior)
    print("\nFecha de arribo modificada exitosamente")
    return modificar_vuelo_aux(contenido_anterior[indice_seleccionado].split(";"), contenido_anterior, indice_seleccionado)

def modificar_vuelo_hora_arribo(vuelo_seleccionado, contenido_anterior, indice_seleccionado):
    hora_valida = False
    while not hora_valida:
        hora_ingresada = input("\nIngrese la nueva hora de arribo (HH:MM) (s para regresar, enter para mantener): ")
        if hora_ingresada == "":
            hora_ingresada = vuelo_seleccionado[6]
            hora_valida = True
        else:
            if hora_ingresada == "s":
                return modificar_vuelo_aux(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
            elif not validar_hora(hora_ingresada):
                print("Error: la hora de arribo no es valida.")
            else:
                hora_valida = True

    datos_vuelo = contenido_anterior[indice_seleccionado].split(";")
    datos_vuelo[6] = hora_ingresada
    contenido_anterior[indice_seleccionado] = f"{datos_vuelo[0]};{datos_vuelo[1]};{datos_vuelo[2]};{datos_vuelo[3]};{datos_vuelo[4]};{datos_vuelo[5]};{datos_vuelo[6]};{datos_vuelo[7]};{datos_vuelo[8]};{datos_vuelo[9]};{datos_vuelo[10]};{datos_vuelo[11]}"
    reescribir_vuelos(contenido_anterior)
    print("\nHora de arribo modificada exitosamente")
    return modificar_vuelo_aux(contenido_anterior[indice_seleccionado].split(";"), contenido_anterior, indice_seleccionado)

def modificar_vuelo_aerolinea(vuelo_seleccionado, contenido_anterior, indice_seleccionado):
    aerolineas = cargar_aerolineas()
    if not aerolineas:
        print("Error: no hay aerolineas registradas.")
        return modificar_vuelo_aux(vuelo_seleccionado, contenido_anterior, indice_seleccionado)

    mostrar_aerolineas()
    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el numero de opcion de la nueva aerolinea (0 para regresar, enter para mantener): ")
        if indice_ingresado == "":
            aerolinea_seleccionada = vuelo_seleccionado[7]
            matricula_seleccionada = vuelo_seleccionado[8]
            indice_valido = True
        else:
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(aerolineas):
                print("Error: la opcion ingresada no existe.")
            elif indice_ingresado == 0:
                return modificar_vuelo_aux(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
            else:
                aerolinea_seleccionada = aerolineas[indice_ingresado-1].strip().split(";")[0]
                aviones_disponibles = mostrar_aviones_aerolinea(aerolinea_seleccionada)
                if not aviones_disponibles:
                    print("Error: no hay aviones registrados para esta aerolinea.")
                else:
                    indice_matricula_valido = False
                    while not indice_matricula_valido:
                        indice_matricula = input("Ingrese el numero de opcion de la matricula (0 para regresar): ")
                        if indice_matricula != "":
                            try:
                                indice_matricula = int(indice_matricula)
                            except:
                                print("Error: la opcion debe ser un numero.")
                                continue
                            if indice_matricula < 0 or indice_matricula > len(aviones_disponibles):
                                print("Error: la opcion ingresada no existe.")
                            elif indice_matricula == 0:
                                return modificar_vuelo_aux(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
                            else:
                                matricula_seleccionada = aviones_disponibles[indice_matricula-1].strip().split(";")[0]
                                indice_matricula_valido = True
                                indice_valido = True
                        else:
                            print("Error: la opcion no puede estar vacia.")

    datos_vuelo = contenido_anterior[indice_seleccionado].split(";")
    datos_vuelo[7] = aerolinea_seleccionada
    datos_vuelo[8] = matricula_seleccionada
    contenido_anterior[indice_seleccionado] = f"{datos_vuelo[0]};{datos_vuelo[1]};{datos_vuelo[2]};{datos_vuelo[3]};{datos_vuelo[4]};{datos_vuelo[5]};{datos_vuelo[6]};{datos_vuelo[7]};{datos_vuelo[8]};{datos_vuelo[9]};{datos_vuelo[10]};{datos_vuelo[11]}"
    reescribir_vuelos(contenido_anterior)
    print("\nAerolinea del vuelo modificada exitosamente")
    return modificar_vuelo_aux(contenido_anterior[indice_seleccionado].split(";"), contenido_anterior, indice_seleccionado)

def modificar_vuelo_matricula(vuelo_seleccionado, contenido_anterior, indice_seleccionado):
    aviones_disponibles = mostrar_aviones_aerolinea(vuelo_seleccionado[7])
    if not aviones_disponibles:
        print("Error: no hay aviones registrados para esta aerolinea.")
        return modificar_vuelo_aux(vuelo_seleccionado, contenido_anterior, indice_seleccionado)

    indice_valido = False
    while not indice_valido:
        indice_ingresado = input("Ingrese el numero de opcion de la matricula (0 para regresar, enter para mantener): ")
        if indice_ingresado == "":
            matricula_seleccionada = vuelo_seleccionado[8]
            indice_valido = True
        else:
            try:
                indice_ingresado = int(indice_ingresado)
            except:
                print("Error: la opcion debe ser un numero.")
                continue
            if indice_ingresado < 0 or indice_ingresado > len(aviones_disponibles):
                print("Error: la opcion ingresada no existe.")
            elif indice_ingresado == 0:
                return modificar_vuelo_aux(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
            else:
                matricula_seleccionada = aviones_disponibles[indice_ingresado-1].strip().split(";")[0]
                indice_valido = True

    datos_vuelo = contenido_anterior[indice_seleccionado].split(";")
    datos_vuelo[8] = matricula_seleccionada
    contenido_anterior[indice_seleccionado] = f"{datos_vuelo[0]};{datos_vuelo[1]};{datos_vuelo[2]};{datos_vuelo[3]};{datos_vuelo[4]};{datos_vuelo[5]};{datos_vuelo[6]};{datos_vuelo[7]};{datos_vuelo[8]};{datos_vuelo[9]};{datos_vuelo[10]};{datos_vuelo[11]}"
    reescribir_vuelos(contenido_anterior)
    print("\nMatricula del vuelo modificada exitosamente")
    return modificar_vuelo_aux(contenido_anterior[indice_seleccionado].split(";"), contenido_anterior, indice_seleccionado)

def modificar_vuelo_monto_ejecutiva(vuelo_seleccionado, contenido_anterior, indice_seleccionado):
    monto_valido = False
    while not monto_valido:
        monto_ingresado = input("Ingrese el nuevo monto de clase ejecutiva (0 para regresar, enter para mantener): ")
        if monto_ingresado == "":
            monto_ingresado = vuelo_seleccionado[9]
            monto_valido = True
        elif monto_ingresado == "0":
            return modificar_vuelo_aux(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
        elif not validar_monto(monto_ingresado):
            print("Error: el monto debe ser un numero mayor que 0.")
        else:
            monto_valido = True

    datos_vuelo = contenido_anterior[indice_seleccionado].split(";")
    datos_vuelo[9] = monto_ingresado
    contenido_anterior[indice_seleccionado] = f"{datos_vuelo[0]};{datos_vuelo[1]};{datos_vuelo[2]};{datos_vuelo[3]};{datos_vuelo[4]};{datos_vuelo[5]};{datos_vuelo[6]};{datos_vuelo[7]};{datos_vuelo[8]};{datos_vuelo[9]};{datos_vuelo[10]};{datos_vuelo[11]}"
    reescribir_vuelos(contenido_anterior)
    print("\nMonto clase ejecutiva modificado exitosamente")
    return modificar_vuelo_aux(contenido_anterior[indice_seleccionado].split(";"), contenido_anterior, indice_seleccionado)

def modificar_vuelo_monto_turista(vuelo_seleccionado, contenido_anterior, indice_seleccionado):
    monto_valido = False
    while not monto_valido:
        monto_ingresado = input("Ingrese el nuevo monto de clase turista (0 para regresar, enter para mantener): ")
        if monto_ingresado == "":
            monto_ingresado = vuelo_seleccionado[10]
            monto_valido = True
        elif monto_ingresado == "0":
            return modificar_vuelo_aux(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
        elif not validar_monto(monto_ingresado):
            print("Error: el monto debe ser un numero mayor que 0.")
        else:
            monto_valido = True

    datos_vuelo = contenido_anterior[indice_seleccionado].split(";")
    datos_vuelo[10] = monto_ingresado
    contenido_anterior[indice_seleccionado] = f"{datos_vuelo[0]};{datos_vuelo[1]};{datos_vuelo[2]};{datos_vuelo[3]};{datos_vuelo[4]};{datos_vuelo[5]};{datos_vuelo[6]};{datos_vuelo[7]};{datos_vuelo[8]};{datos_vuelo[9]};{datos_vuelo[10]};{datos_vuelo[11]}"
    reescribir_vuelos(contenido_anterior)
    print("\nMonto clase turista modificado exitosamente")
    return modificar_vuelo_aux(contenido_anterior[indice_seleccionado].split(";"), contenido_anterior, indice_seleccionado)

def modificar_vuelo_monto_economica(vuelo_seleccionado, contenido_anterior, indice_seleccionado):
    monto_valido = False
    while not monto_valido:
        monto_ingresado = input("Ingrese el nuevo monto de clase economica (0 para regresar, enter para mantener): ")
        if monto_ingresado == "":
            monto_ingresado = vuelo_seleccionado[11]
            monto_valido = True
        elif monto_ingresado == "0":
            return modificar_vuelo_aux(vuelo_seleccionado, contenido_anterior, indice_seleccionado)
        elif not validar_monto(monto_ingresado):
            print("Error: el monto debe ser un numero mayor que 0.")
        else:
            monto_valido = True

    datos_vuelo = contenido_anterior[indice_seleccionado].split(";")
    datos_vuelo[11] = monto_ingresado
    contenido_anterior[indice_seleccionado] = f"{datos_vuelo[0]};{datos_vuelo[1]};{datos_vuelo[2]};{datos_vuelo[3]};{datos_vuelo[4]};{datos_vuelo[5]};{datos_vuelo[6]};{datos_vuelo[7]};{datos_vuelo[8]};{datos_vuelo[9]};{datos_vuelo[10]};{datos_vuelo[11]}"
    reescribir_vuelos(contenido_anterior)
    print("\nMonto clase economica modificado exitosamente")
    return modificar_vuelo_aux(contenido_anterior[indice_seleccionado].split(";"), contenido_anterior, indice_seleccionado)

menu_principal()