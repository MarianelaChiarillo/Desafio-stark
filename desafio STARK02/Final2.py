from stark2 import *


def imprimir_menu():
    print("""
    ***Menu de opciones***
    ----------------------------------------------
    0. Bienvenido, ¿comenzamos? Coloque -> 0 <-
    1. Nombre de todos los superhéroes <- 
    2. Nombre y altura de todos los superhéroes <-
    3. Calcular el máximo o mínimo <-
    4. Promedio de alturas de los superhéroes <-
    5. Salir  <-
    """)
    opcion = input("Ingrese una opcion: --> ") 
    return opcion


def validar_entero(opcion: int) -> bool:
    if opcion.isdigit():
        return True
    else:
        return False
    
def stark_menu_principal():
    imprimir_menu()

    while True:
        opcion = input("Seleccione una opción: ")

        if validar_entero(opcion):
            opcion_entero = int(opcion)

            if opcion_entero >= 0 and opcion_entero <= 5:
                return opcion_entero
            else:
                imprimir_dato("Opción inválida, ingrese nuevamente.")


