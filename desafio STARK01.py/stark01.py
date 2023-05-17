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
#Saco el nombre de todos los personajes de genero masculino.
def mostrar_heroes_masculinos(lista_personajes): #funciones.
    personajes_masculinos = []
    for personaje in lista_personajes:
        if personaje["genero"] == "M":
            personajes_masculinos.append(personaje["nombre"])
    return personajes_masculinos

#------------------------------------------------------------------------------------------------------
#Saco nombre de todos los personajes de genero femenino.
def mostrar_heroes_femeninos(lista_personajes):
    personajes_femeninos = []
    for personaje in lista_personajes:
        if personaje["genero"] == "F":
            personajes_femeninos.append(personaje["nombre"])
    return personajes_femeninos
#-------------------------------------------------------------------------------------------------------

#Saco la altura del más alto del genero masculino.
def mostrar_nombre_altura_masculino(lista_personajes):
    personaje_alto_masculino = lista_personajes[0]
    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        if personaje["genero"] == "M":
            if personaje["altura"] > personaje_alto_masculino["altura"]:
                personaje_alto_masculino = personaje
    return personaje_alto_masculino

#------------------------------------------------------------------------------------------------------
#Saco la altura del más alto del genero femenino.
def mostrar_nombre_altura_femenino(lista_personajes):
    personaje_alto_femenino = lista_personajes[0]
    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        if personaje["genero"] == "F":
            if personaje["altura"] > personaje_alto_femenino["altura"]:
                personaje_alto_femenino = personaje
    return personaje_alto_femenino

#-------------------------------------------------------------------------------------------------------
#Saco el más bajo de los personajes masculinos.
def mostrar_personaje_bajo_masculino(lista_personajes):  
    personaje_bajo_m = lista_personajes[0]
    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        if personaje["genero"] == "M":
            if personaje["altura"] < personaje_bajo_m["altura"]:
                personaje_bajo_m = personaje
    return personaje_bajo_m
#------------------------------------------------------------------------------------------------------
#Saco el más bajo de los femeninos.
def mostrar_nombre_bajo_femenino(lista_personajes):
    personaje_bajo_femenino = lista_personajes[0]
    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        if personaje["genero"] == "F":
            if personaje["altura"] < personaje_bajo_femenino["altura"]:
                personaje_bajo_femenino = personaje
    return personaje_bajo_femenino

#---------------------------------------------------------------------------------------------------------
#Saco el promedio de alturas de los personajes masculinos.
def mostrar_promedio_masculino(lista_personajes:list):
    acumulador = 0
    for personaje in lista_personajes:
        altura_m = float(personaje['altura']) #cambio de string a float.
        if personaje["genero"] == "M": 
            acumulador += altura_m
        promedio_m = acumulador / len(lista_personajes) 
    return promedio_m

#---------------------------------------------------------------------------------------------------------
#Saco el promedio de alturas de los personajes femeninos.
def mostrar_promedio_femenino(lista_personajes):
    acumulador = 0
    for personaje in lista_personajes:
        altura_f = float(personaje['altura'])#cambio de string a float.
        if personaje["genero"] == "F": 
            acumulador += altura_f
        promedio_f = acumulador / len(lista_personajes) 
    return promedio_f
# #---------------------------------------------------------------------------------------------------------
#Funcion reutilizable para mostrar lo que se desee y el titulo de ello.(Tiene doble parametro.)
def mostrar_lista(lista:list, title:str):
    print(f"        ***{title}***        ")
    for item in lista:
        print(item)
#-----------------------------------------------------------------------------------------------------------
#Funcion para establecer si ya hay un elemento en la lista muestra T or F.(Tiene doble parametro.)
def disponible_lista(lista:list, item:str)->bool:
    esta = False
    for elemento in lista:
        if(elemento == item):
            esta = True
            break
    return esta
#-----------------------------------------------------------------------------------------------------------
#Funcion que filtra elementos dependiendo su key(tiene triple parametro). Recibe un elemento y lo appendea a la lista.
def filtrar_valores(lista:list, key:str, value:str)-> list:
    lista_filtradora = []

    for personaje in lista:
        if (personaje[key] == value):
            lista_filtradora.append(personaje)
    return lista_filtradora
#-----------------------------------------------------------------------------------------------------------
#Funcion que muestra el personaje. Desde la filtracion de personajes, se establece si ya existe, si no se agrega a la lista aux.(Triple parametro.)
def mostrar_superheroe(lista: list, key: str, repetido: bool = False) -> list:
    lista_filtradora = []

    for personaje in lista:
        lista_filtradora.append(personaje[key])

        if (not repetido):
            lista_aux = []
            for item in lista_filtradora:
                if not disponible_lista(lista_aux, item):
                    lista_aux.append(item)
            lista_filtradora = lista_aux
    
    return lista_filtradora
#-----------------------------------------------------------------------------------------------------------
#Funcion que se encarga de verficar si esta repetido o no. Si esta los agrega a la lista de no repetidos(1 parametro)
def sacar_superheroes_repetidos(lista:list)-> list:
    lista_no_repetidos = []
    for item in lista:
        if (not disponible_lista(lista_no_repetidos, item)):
            lista_no_repetidos.append(item)
    return lista_no_repetidos

#-----------------------------------------------------------------------------------------------------------
#Funcion que se encarga de contar valores o juntarlos dependiendo de su valor. Deuelve un int.(es contador)(triple parametro.)
def contar_valores(lista: list, key: str, value: str) -> int:
    contador = 0
    for valor in lista:
        if valor[key] == value:
            contador += 1
    return contador


#-----------------------------------------------------------------------------------------------------------

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
                if flag_bienvenida:
                    personajes_masculinos = mostrar_heroes_masculinos(lista_personajes)
                    print(personajes_masculinos)
                else:
                    print("Debe poner confirmar para saber más información.")

            case "9":
                if flag_bienvenida:
                    personajes_femeninos = mostrar_heroes_femeninos(lista_personajes)
                    print(personajes_femeninos)
                else:
                    print("Debe poner confirmar para saber más información.")
            
            case "10":
                if flag_bienvenida:
                    personajes_alto_masculino = mostrar_nombre_altura_masculino(lista_personajes)
                    print(f"Personaje:", personajes_alto_masculino["nombre"], " Altura: ", personajes_alto_masculino["altura"])
                else:
                    print("Debe poner confirmar para saber más información.")

            case "11":
                if flag_bienvenida:
                    personaje_alto_femenino = mostrar_nombre_altura_femenino(lista_personajes)
                    print(f"Personaje:", personaje_alto_femenino["nombre"], " Altura: ", personaje_alto_femenino["altura"])
                else:
                    print("Debe poner confirmar para saber más información.")
            
            case "12":
                if flag_bienvenida:
                    personaje_bajo_m= mostrar_personaje_bajo_masculino(lista_personajes)
                    print(f"Personaje:", personaje_bajo_m["nombre"], " Altura: ", personaje_bajo_m["altura"])
                else:
                    print("Debe poner confirmar para saber más información.")

            case "13":
                if flag_bienvenida:
                    personaje_bajo_femenino= mostrar_nombre_bajo_femenino(lista_personajes)
                    print(f"Personaje:", personaje_bajo_femenino["nombre"], " Altura: ", personaje_bajo_femenino["altura"])
                else:
                    print("Debe poner confirmar para saber más información.")

            case "14":
                if flag_bienvenida:
                    promedio_m = mostrar_promedio_masculino(lista_personajes)
                    print(f"Promedio alturas:", promedio_m)
                else:
                    print("Debe poner confirmar para saber más información.")

            case "15":
                if flag_bienvenida:
                    promedio_f = mostrar_promedio_femenino(lista_personajes)
                    print(f"Promedio alturas:", promedio_f)
                else:
                    print("Debe poner confirmar para saber más información.")

            case "16":
                if flag_bienvenida:
                    colores_ojos = ["Blue", "Brown", "Yellow", "Hazel", "Yellow (without irises)", "Green", "Silver", "Red"]
                    print("               ***Contador por color de ojos***    ")
                    print("................................................................................................")

                    for color in colores_ojos:
                        contador = contar_valores(lista_personajes, "color_ojos", color)
                        print(f"Contador {color}: {contador}")

                else:
                    print("Debe poner confirmar para saber más información.")

            case "17":
                if flag_bienvenida:
                    tipo_pelo = ["Black", "Brown", "Yellow", "Auburn", "Red / Orange", "White", "No Hair", "Blond", "Green", "Red", "Brown / White"]
                    print("               ***Contador por color o tipo de pelo***    ")
                    print("."*60)

                    for tipo in tipo_pelo:
                        contador = contar_valores(lista_personajes, "color_pelo", tipo)
                        print(f"Contador {tipo}: {contador}") 
                else:
                    print("Debe poner confirmar para saber más información.")

            case "18":
                if flag_bienvenida:
                    tipo_inteligencia = ["None", "good", "average", "high"]
                    print("          ***Contador por tipo de inteligencia***    ")
                    print("."*60)

                    for tipo in tipo_inteligencia:
                        contador = contar_valores(lista_personajes, "inteligencia", tipo)
                        print(f"Contador {tipo}: {contador}")     
                else:
                    print("Debe poner confirmar para saber más información.")
                
            case "19":
                if flag_bienvenida:
                    colores_ojos = ["Blue", "Brown", "Yellow", "Hazel", "Yellow (without irises)", "Green", "Silver", "Red"]
                    print("             ***Lista por color de ojos***    ")
                    print("."*60)
                    
                    for color in colores_ojos:
                        division_por_ojos = filtrar_valores(lista_personajes, "color_ojos", color)
                        nombres_superheroes = mostrar_superheroe(division_por_ojos, "nombre")
                        mostrar_lista(nombres_superheroes, f"Lista por color {color}")
                        print("."*60)

                else:
                    print("Debe poner confirmar para saber más información.")
                    
            case "20":
                if flag_bienvenida:
                    tipo_pelo = ["Black", "Brown", "Yellow", "Auburn", "Red / Orange", "White", "No Hair", "Blond", "Green", "Red", "Brown / White"]
                    print("            ***Lista por color o tipo de pelo***    ")
                    print("."*60)

                    for tipo in tipo_pelo:
                        division_por_pelo = filtrar_valores(lista_personajes, "color_pelo", tipo)
                        nombres_superheroes = mostrar_superheroe(division_por_pelo, "nombre")
                        mostrar_lista(nombres_superheroes, f"Lista por tipo {tipo}")
                        print("."*60)
                else:
                    print("Debe poner confirmar para saber más información.")
                
            case "21":
                if flag_bienvenida:
                    tipo_inteligencia = ["None", "good", "average", "high"]
                    print("            ***Lista por tipo de inteligencia***    ")
                    print("."*60)

                    for tipo in tipo_inteligencia:
                        division_por_inteligencia = filtrar_valores(lista_personajes, "inteligencia", tipo)
                        nombres_superheroes = mostrar_superheroe(division_por_inteligencia, "nombre")
                        mostrar_lista(nombres_superheroes, f"Lista por tipo {tipo}")
                        print("."*60)
                else:
                    print("Debe poner confirmar para saber más información.")

            case "22":
                salir = input("confirma salida? s/n: ")
                if(salir == "s"):
                    break
    input("Presione enter para continuar")
