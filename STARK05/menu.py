from stark import *
import re

def imprimir_menu_desafio_5():
    opciones = [
        ".........................................................",

        "A.Bienvenido, comenzamos? s/n",
        "B. Imprimir el nombre de cada superhéroe de género M <-",
        "C. Imprimir el nombre de cada superhéroe de género F  <-",
        "D. Ingrese que dato desea saber del personaje, (alto, bajo) <-",
        "E. Ingrese el genero por el que desea saber el promedio de alturas <-",
        "F. Ingrese el dato que desea saber por cantidad <-",
        "G. Ingrese el dato que desea saber los nombres de los personajes <-",
        "Z. Salir <-"
        
    ]
    print("*** Menú de opciones ***")

    for opcion in opciones:
        print(opcion)
    opcion = input("Ingrese una opción: --> ")
    return opcion

def stark_menu_principal_desafio_5(): 
    opcion = imprimir_menu_desafio_5()
    opcion = opcion.strip().upper() #separo las opciones y las hago mayuscula.

    if re.findall(r'^[a-f,z]$', opcion): #con regex veifico que las letras sea las del menu.
        return opcion
    else:
        return -1