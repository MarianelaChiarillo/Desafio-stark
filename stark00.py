import os
from data_stark import lista_personajes
from Final import *


lista_personas = []

#------------------------------------------------------------------------------------------------------
#Saco todos los nombres de los personajes que aparecen en el set.
def mostrar_nombres(lista_personajes):
    for personaje in lista_personajes:
        print(personaje["nombre"])

#----------------------------------------------------------------------------------------------------
#Saco el nombre y  altura de todos los personajes.
def mostrar_nombres_altura(lista_personajes):
    for personaje in lista_personajes:
        print(personaje["nombre"], personaje["altura"])
#----------------------------------------------------------------------------------------------------
#Saco la altura del más alto de todos los personajes del set.
def mostrar_personaje_alto(lista_personajes):
    personaje_alto = lista_personajes[0]
    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        if personaje["altura"] > personaje_alto["altura"]:
            personaje_alto = personaje
    return personaje_alto

#----------------------------------------------------------------------------------------------------
#Saco el más bajo de todo el set de datos.
def mostrar_personaje_bajo(lista_personajes):  
    personaje_bajo = lista_personajes[0]
    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        if personaje["altura"] < personaje_bajo["altura"]:
            personaje_bajo = personaje
    return personaje_bajo

#---------------------------------------------------------------------------------------------------------
#Saco el promedio de alturas de todos los personajes del set.
def mostrar_promedio(lista_personajes):
    acumulador = 0
    for personaje in lista_personajes:
        altura = float(personaje['altura']) #cambio de string a float.
        acumulador += altura
    promedio = acumulador / len(lista_personajes) 
    return promedio
#---------------------------------------------------------------------------------------------------------
#saco el más pesado del set.
def mostrar_personaje_pesado(lista_personajes):  
    personaje_pesado = lista_personajes[0]
    for personaje in lista_personajes:
        personaje["peso"] = float(personaje["peso"])  #asi se valida un string a float.
        if personaje["peso"] > personaje_pesado["peso"]:
            personaje_pesado = personaje
    return personaje_pesado
#--------------------------------------------------------------------------------------------------------
#saco el más liviano del set.
def mostrar_personaje_liviano(lista_personajes):
    personaje_liviano = lista_personajes[0]
    for personaje in lista_personajes:
        personaje["peso"] = float(personaje["peso"])
        if personaje["peso"] < personaje_liviano["peso"]:
            personaje_liviano = personaje
    return personaje_liviano

#---------------------------------------------------------------------------------------------------------   

flag_bienvenida = False
while True:
    os.system("cls")

    match(menu()):
            case "s":
                print("Entendido, comencemos.")
                flag_bienvenida = True

            case "1":
                if flag_bienvenida:
                    mostrar_nombres(lista_personajes)
                else:
                    print("Debe poner confirmar para saber más información.")

            case "2":
                if flag_bienvenida:
                    mostrar_nombres_altura(lista_personajes)
                else:
                    print("Debe poner confirmar para saber más información.")

            
            case "3":
                if flag_bienvenida:
                    personaje_alto = mostrar_personaje_alto(lista_personajes)
                    print(f"Personaje:", personaje_alto["nombre"], " Altura: ", personaje_alto["altura"])
                else:
                    print("Debe poner confirmar para saber más información.")

            case "4":
                if flag_bienvenida:
                    personaje_bajo= mostrar_personaje_bajo(lista_personajes)
                    print(f"Personaje:", personaje_bajo["nombre"], " Altura: ", personaje_bajo["altura"])
                else:
                    print("Debe poner confirmar para saber más información.")

            case "5":
                if flag_bienvenida:
                    promedio = mostrar_promedio(lista_personajes)
                    print(f"Promedio alturas:", promedio)
                else:
                    print("Debe poner confirmar para saber más información.")

            case "6":
                if flag_bienvenida:
                    personaje_pesado = mostrar_personaje_pesado(lista_personajes)
                    print(f"Personaje:", personaje_pesado["nombre"], " Peso: ", personaje_pesado["peso"])
                else:
                    print("Debe poner confirmar para saber más información.")

            case "7":
                if flag_bienvenida:
                    personaje_liviano = mostrar_personaje_liviano(lista_personajes)
                    print(f"Personaje:", personaje_liviano["nombre"], " Peso: ", personaje_liviano["peso"])
                else:
                    print("Debe poner confirmar para saber más información.")

            case "8":
                salir = input("confirma salida? s/n: ")
                if(salir == "s"):
                    break
    input("Presione enter para continuar")


