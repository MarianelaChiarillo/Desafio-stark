import os 
from data_stark import *
from Final2 import *


def stark_normalizar_data(lista_personajes:list[dict]) -> list[dict]:

    if len(lista_personajes) == 0: # Verifico que no estén vacíos los diccionarios de héroes.
        return "-1"
    else:
        normalizar = False   #Si hay datos se inicializa con un booleano, se crea una lista nueva vacia.
        nueva_lista_personajes = [] 
        for diccionario in lista_personajes:
            for key, value in diccionario.items():
                if isinstance(value, str) and value.isnumeric():  #se verifica si el valor es de tipo string o si contiene solo numeros, sino se convierte en int y se modifica el valor.
                    diccionario[key] = int(value)
                    normalizar = True  #se realizaron cambios.
                elif isinstance(value, str) and value.replace(".", "").isnumeric():  #si es decimal se eliminan los puntos decimales.
                    diccionario[key] = float(value) # Se agrega al nuevo dict modificando la lista previa.
                    normalizar = True
            nueva_lista_personajes.append(diccionario)

        if normalizar:
            print("Datos normalizados")
        return nueva_lista_personajes

# #---------------------------------------------------------------------------------------------------------------------------------------

def obtener_nombre(dict_list: dict, key: str) -> str: 

    nombres = []
    for personaje in dict_list:
        if key in personaje:#Se iteran los (elementos)  y se verifica si la clave especificada existe en el dict personaje actuaL.
            nombre = personaje[key] #Si existe se asigna el valor a nombres sobreescribiendo el anterior.
            nombres.append(f"Nombre: {nombre}")
    return nombres

data = obtener_nombre(lista_personajes, "nombre") # le asigno a data los nombres de los personajes.
 #al iterar el nombre se van separando dejando más legibles los nombres.

# #---------------------------------------------------------------------------------------------------------------------------------------

def imprimir_dato(dato:str, key:str)->None: #La función toma un string como parámetro. No retorna nada solo si es llamada.

    print(dato, key) 
# #----------------------------------------------------------------------------------------------------------------------------------------

def stark_imprimir_nombres_heroes(lista_personajes: list) -> None:
    if not lista_personajes: # Verificar si la lista está vacía
        return -1

    for nombre in nombres: 
        nombre = obtener_nombre(lista_personajes, "nombre")
    imprimir_dato(nombre, "nombre")

# Llamada a la función
# stark_imprimir_nombres_heroes(lista_personajes)

#------------------------------------------------------------------------------------------------------------------------------------------

def obtener_nombre_y_dato(personaje: dict, key: str) -> str:
    
    nombre = personaje.get("nombre") #Se utiliza el método get() para obtener el nombre y el valor correspondiente al dato dentro del diccionario.
    valor = personaje.get(key)
    return f"Nombre: {nombre} | {key}: {valor}"

opciones = ['identidad', 'empresa', 'altura', 'peso', 'genero', 'color_ojos', 'fuerza', 'inteligencia', 'color_pelo']
#El usuario ingresa el dato que desea saber utilizando la función input(). El valor ingresado se guarda en la variable dato.

# for personaje in lista_personajes:
#     for opcion in opciones:
#         resultado = obtener_nombre_y_dato(personaje, opciones)
    # imprimir_dato("->",resultado)

# #------------------------------------------------------------------------------------------------------------------------------------------

def stark_imprimir_nombres_alturas(lista_personajes: list) -> None:
    if not lista_personajes: # Verificar si la lista está vacía
        print("La lista de personajes está vacía.")
        return -1

    opciones = ['altura'] #unica opcion altura
    for personaje in lista_personajes:
        for opcion in opciones:
            resultado = obtener_nombre_y_dato(personaje, opcion)
            imprimir_dato("->", resultado)

# #------------------------------------------------------------------------------------------------------------------------------------------

def calcular_max(lista:list[dict], key:str)->str or float:
    stark_normalizar_data(lista)   #Se normalizan los datos, se inicializa con la variable dato_max con el primer dict de la lista.
  
    dato_max = lista[0]
    for personaje in lista:  #Se itera cada diccionario y se compara el valor de la con el valor del dato max, si el valor es mayor se actualizan los datos.
        if personaje[key] > dato_max[key]:
            dato_max = personaje
    return dato_max   #Terminada la iteracion se retorna el dato maximo con el diccionario del mismo.

# #-------------------------------------------------------------------------------------------------------------------------------------------

def calcular_min(lista:list[dict], key:str)->str or float:
    stark_normalizar_data(lista) #Mismo funcionar que el maximo solo con cambio de signo.

    dato_min = lista[0]
    for personaje in lista:
        if personaje[key] < dato_min[key]:
            dato_min = personaje
    return dato_min

# #-------------------------------------------------------------------------------------------------------------------------------------------

def calcular_max_min_dato(lista:list[dict], value:str, key:str): 
    #recibe una lista de dicts(lista superheroes), el tipo de cálculo 'maximo' o 'minimo' y una key que representa el dato que a calcular.
    
    if value == 'maximo': 
        maximo = calcular_max(lista, key) #Si el valor es 'maximo', se llama a la función calcular_max pasando la lista de héroes y la clave especificada.
        return maximo
    
    elif value == 'minimo': #Si el valor es 'minimo' mismo funcionamiento que el maximo.
        minimo = calcular_min(lista, key)
        return minimo

# #-------------------------------------------------------------------------------------------------------------------------------------------

def stark_calcular_imprimir_heroe(lista: list[dict], calculo: str, dato: str) -> None:
    if not lista:  # Verificar si la lista de héroes está vacía
        return -1
    
    valor = calcular_max_min_dato(lista, calculo, dato)  # Calcular el valor máximo o mínimo según el tipo de cálculo
    
    if valor:
        for personaje in lista:
            resultado = obtener_nombre_y_dato(personaje, dato)  # Obtener el nombre y valor del dato del personaje
        imprimir_dato(valor, resultado)  # Imprimir el valor calculado junto con el nombre del personaje y el dato correspondiente       


#----------------------------------------------------------------------------------------------------------------------------------------------

def sumar_dato_heroe(heroes:list[dict], key:str)-> float: # lista de héroes y un string que representa el dato/key de los héroes.
    stark_normalizar_data(heroes) #normalizo datos.

    if len(heroes) == 0: #valido que el dict no este vacio.
        return "-1"
    else:
        suma = 0 #realizo la suma de las keys.
        for heroe in heroes:
            suma += heroe.get(key)
        return suma
#----------------------------------------------------------------------------------------------------------------------------------------------

def dividir_datos(dividendo:float, divisor:float)-> float: #como parámetro dos números (dividendo y divisor). 

    if divisor == 0: 
        return "0"
    else:
        division = dividendo / divisor
        return division
    
#----------------------------------------------------------------------------------------------------------------------------------------------

def calcular_promedio(heroe:list[dict], key:str)->float:
    stark_normalizar_data(heroe)

    if len(heroe) == 0: #verifico que no este en 0 los dicts de heroes.
        return "Error"
    else:
        suma = sumar_dato_heroe(heroe, key)  # Sumar los valores de la clave.
        cantidad = len(heroe)  # Cantidad de elementos en la heroe de héroes para dividir.
        promedio = dividir_datos(suma, cantidad)  # Saco el promedio
    return promedio

#----------------------------------------------------------------------------------------------------------------------------------------------

def stark_calcular_imprimir_promedio_altura(lista: list[dict]) -> float:
    stark_normalizar_data(lista)

    if len(lista) == 0: # Verifico que no estén vacíos los diccionarios de héroes.
        return "Error"
    else:
        resultado_altura = calcular_promedio(lista, "altura") #llamo a la funcion de promedio
        return resultado_altura

#-----------------------------------------------------------------------------------------------------------------------------------------------

def stark_marvel_app(lista_personajes):
    flag_bienvenida = False
    while True:
        os.system("cls")
        match(imprimir_menu()):
                case "0":
                    print("Entendido, comencemos.")
                    flag_bienvenida = True

                case "1":
                    if flag_bienvenida:
                        data = obtener_nombre(lista_personajes, "nombre")
                        for nombre in data:
                            imprimir_dato("->", nombre)
                    else:
                        print("Debe poner confirmar para saber más información.")

                case "2":
                    if flag_bienvenida:
                        alturas = stark_imprimir_nombres_alturas(lista_personajes)
                        imprimir_dato("->", alturas)
                    else:
                        print("Debe poner confirmar para saber más información.")

                
                case "3":
                    if flag_bienvenida:
                        opciones = input("opciones = ['altura', 'peso', 'fuerza']-> ")
                        dato_deseado = input("¿Qué dato desea conocer? (minimo/maximo) -> ")
                        resultado = stark_calcular_imprimir_heroe(lista_personajes, dato_deseado, opciones)
                        imprimir_dato("->", resultado)
                        

                    else:
                        print("Debe poner confirmar para saber más información.")

                case "4":
                    if flag_bienvenida:
                        resultado = stark_calcular_imprimir_promedio_altura(lista_personajes)
                        imprimir_dato("El promedio es: ", resultado) #imprimo el dato.
                    else:
                        print("Debe poner confirmar para saber más información.")
                        
                case "5":
                    salir = input("confirma salida? s/n: ")
                    if(salir == "s"):
                        break
        input("Presione enter para continuar")

