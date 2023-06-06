from data4 import *

def imprimir_menu():
    print("""
    ***Menu de opciones***
    ----------------------------------------------
    0. Bienvenido, ¿comenzamos? Coloque -> 0 <-
    1. Imprimir la lista de nombres junto con sus iniciales <- 
    2. Generar códigos de héroes <-
    3. Normalizar datos <-
    4. Imprimir índice de nombres <-
    5. Navegar fichas <-
    6. Salir  <-
    """)

def stark_menu_principal():
    imprimir_menu()
    opcion = input("Ingrese una opción: ")
    return opcion

