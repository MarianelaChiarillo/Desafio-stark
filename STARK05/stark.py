import json
import re
import os
from menu import *

def leer_json(nombre_archivo: str) -> list[dict]: #defino el leer json con el nombre del archivo como parametro.
    with open(nombre_archivo, 'r') as file: #lo abro en  modo lectura.
        diccionario = json.load(file)
    return diccionario #devuelve el diccionario con los datos.

data_stark_json = "data_stark.json"  
diccionario = leer_json(data_stark_json)
lista_heroes = diccionario["heroes"] #se leen los datos de lor archivos atraves de las variables definidas previamente.

#---------------------------------------------------------------------------------------------------------------------------------------

def imprimir_dato(dato:str, key:str) -> None: #funcion que sirve como print.
    imprimir_dato(dato, key)

#---------------------------------------------------------------------------------------------------------------------------------------

def leer_archivo(nombre_archivo): #funcion para leer archivos.
    lista_diccionarios = [] #establezco una lista vacia.

    patron = r"\.json$" #verifico que el archivo sea de .json con regex.

    # Verificar si la extensión del archivo coincide con el patrón
    if re.search(patron, nombre_archivo, re.IGNORECASE):#verifica que haya coincidencia y lo abre modo lectura.
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            data = json.load(archivo) #cargo la informacion en data.
            lista_diccionarios = data['heroes']

    else:  # Si no es un archivo JSON, leer como antes
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines() #lee las lineas del archivo.
            encabezados = lineas[0].strip().split(';') #obtiene los encabezados, se eliminan espacios en blanco al principio y al final de la línea y se dividen los valores.

            for linea in lineas[1:]: #itera en las lineas quitando la primer linea
                valores = linea.strip().split(';')
                diccionario = {encabezados[i]: valores[i] if i < len(valores) else '' for i in range(len(encabezados))}#Se crea un diccionario 
                lista_diccionarios.append(diccionario) #se agrega el diccionario a la lista.

    return lista_diccionarios

#---------------------------------------------------------------------------------------------------------------------------------------

def guardar_archivo(nombre_archivo: str, contenido: str) -> bool:
    try:#crea un archivo, primero verifica si la condicion es la misma y si es asi se escribe.
        with open(nombre_archivo, 'w+', encoding='utf-8') as archivo:
            archivo.write(contenido)
        print(f"Se creó el archivo: {nombre_archivo}")
        return True
    except Exception as e: #si no se cumple se muesta un mensaje de error sobre el archivo.
        print(f"Error al crear el archivo: {nombre_archivo}")
        print(f"Detalles del error: {str(e)}")
        return False
    
#---------------------------------------------------------------------------------------------------------------------------------------

def capitalizar_palabras(palabras: str) -> str: #funcion que capitaliza palabras.
    lista_palabras = palabras.split() 
    for i in range(len(lista_palabras)):
        lista_palabras[i] = lista_palabras[i].capitalize() #al iterar la priemra letra pasa a ser mayuscula.
    return ' '.join(lista_palabras)

#---------------------------------------------------------------------------------------------------------------------------------------

def obtener_nombre_capitalizado(diccionario: dict) -> str: #funcion que capitaliza las palabras.
    nombre = diccionario.get("nombre", "")
    nombre_capitalizado = capitalizar_palabras(nombre)
    return nombre_capitalizado

#---------------------------------------------------------------------------------------------------------------------------------------

def obtener_nombre_y_dato(diccionario: dict, key: str) -> str: #busca el valor asociado a una clave en el diccionario.
    nombre = diccionario.get("nombre", "")

    if key in diccionario:
        dato = diccionario[key]
        return f"Nombre: {nombre} | {key.capitalize()}: {dato}" #retorna una cadena formateada con el nombre, la clave capitalizada y el valor.
    else:
        return f"La clave '{key}' no existe en el diccionario."

#---------------------------------------------------------------------------------------------------------------------------------------

def es_genero(diccionario: dict, genero: str) -> bool:

    if "genero" in diccionario:
        return diccionario.get("genero") == genero.upper() #verifica que el genero este dentro de las opciones del archivo.
    else:
        return False
#---------------------------------------------------------------------------------------------------------------------------------------

def stark_guardar_heroe_genero(heroes: list[dict], genero: str) -> bool:
    nombres_heroes = []
    for heroe in heroes:
        if es_genero(heroe, genero):
            nombre_heroe = obtener_nombre_capitalizado(heroe)
            nombres_heroes.append(nombre_heroe) #se agregan los nombres en base al genero solicitado.
    
    if nombres_heroes: #se crea un archivo csv.
        nombres_csv = ",".join(nombres_heroes)
        nombre_archivo = f"heroes_{genero}.csv"
        resultado = guardar_archivo(nombre_archivo, nombres_csv) #se llama a la funcion guardar archivo.

        if resultado:
            print(f"Se guardaron los héroes en el archivo: {nombre_archivo}")
        else:
            print(f"Error al guardar el archivo: {nombre_archivo}")
        
        return resultado
    else:
        print(f"No se encontraron héroes del género {genero}")
        return False
    
#---------------------------------------------------------------------------------------------------------------------------------------

def calcular_min_genero(lista: list[dict], genero: str, dato: str) -> dict or None:
    primer_personaje_genero = None
    
    for personaje in lista:
        if personaje["genero"] == genero:  #si el valor de genero en el diccionario coincide con el especificado, se asigna ese diccionario a primer_personaje_genero.
            primer_personaje_genero = personaje
            break #termina el bucle
    
    if primer_personaje_genero:
        if isinstance(primer_personaje_genero[dato], str):
            try:
                primer_personaje_genero[dato] = float(primer_personaje_genero[dato]) #inicializa con un  primer personaje.
            except ValueError:
                primer_personaje_genero[dato] = 0
        
        dato_min = primer_personaje_genero
        
        for personaje in lista: #filtra los personajes por genero.
            if personaje["genero"] == genero:
                if isinstance(personaje[dato], str):
                    try:
                        personaje[dato] = float(personaje[dato])
                    except ValueError:
                        continue  # Ignorar personaje si el valor no es numérico
                
                if personaje[dato] < dato_min[dato]:
                    dato_min = personaje
        
        return dato_min
    
    return None
#---------------------------------------------------------------------------------------------------------------------------------------

def calcular_max_genero(lista: list[dict], genero: str, dato: str) -> dict or None: #mismo funcionar que el min pero en este caso es maximo.
    primer_personaje_genero = None
    
    for personaje in lista:
        if personaje["genero"] == genero:
            primer_personaje_genero = personaje
            break
    
    if primer_personaje_genero:
        if isinstance(primer_personaje_genero[dato], str):
            try:
                primer_personaje_genero[dato] = float(primer_personaje_genero[dato])
            except ValueError:
                primer_personaje_genero[dato] = 0
        
        dato_min = primer_personaje_genero
        
        for personaje in lista:
            if personaje["genero"] == genero:
                if isinstance(personaje[dato], str):
                    try:
                        personaje[dato] = float(personaje[dato])
                    except ValueError:
                        continue  # Ignorar personaje si el valor no es numérico
                
                if personaje[dato] > dato_min[dato]:
                    dato_min = personaje
        
        return dato_min
    
    return None

#---------------------------------------------------------------------------------------------------------------------------------------
def calcular_max_min_dato_genero(lista: list[dict], genero: str, key:str, tipo: str) -> dict or None: #calcula el maximo o minimo de un dato retornando un diccionario o nada.
    if tipo == 'minimo':
        return calcular_min_genero(lista, genero, key)
    elif tipo == 'maximo':
        return calcular_max_genero(lista, genero, key)
    else:
        return None

#---------------------------------------------------------------------------------------------------------------------------------------
def stark_calcular_imprimir_guardar_heroe_genero(heroes: list[dict]) -> bool: #funcion que le pide al usuario los valores que desea calcular y los retorna.
    genero = input("Ingrese el género a evaluar: ").upper()
    key = input("Ingrese la clave sobre la cual calcular (altura, peso, etc.): ").lower()
    tipo = input("Ingrese el tipo de cálculo (maximo o minimo): ").lower()

    # Calcular máximo o mínimo
    resultado = calcular_max_min_dato_genero(heroes, genero, key, tipo)

    if resultado: # si hay resultado retorna los nombres.
        nombre_heroe = obtener_nombre_capitalizado(resultado)
        dato = resultado[key]
        print(nombre_heroe, dato)

        archivo = f"heroes_{tipo}_{key}_{genero}.csv" #se crea un csv.
        contenido = f"Nombre: {nombre_heroe}, {key.capitalize()}: {dato}"
        exito = guardar_archivo(archivo, contenido)

        return exito
    else:
        print(f"No se encontraron héroes del género {genero}")
        return False

# Ejemplo de uso
data_stark_json = "data_stark.json"
diccionario = leer_json(data_stark_json)
lista_heroes = diccionario["heroes"]

#---------------------------------------------------------------------------------------------------------------------------------------

def sumar_dato_heroe_genero(lista_heroes: list[dict], dato: str, genero: str) -> float:
    suma = 0 #la suma la inicializo en 0.

    for heroe in lista_heroes: #verifica la condicion 
        if isinstance(heroe, dict) and heroe.get("genero") == genero: #controla si es del diccionario y lo especificado.
            valor = heroe.get(dato)
            if isinstance(valor, (int, float)): #aclaro que es un  digito.
                suma += valor
            elif isinstance(valor, str) and valor.replace(".", "").isdigit():
                suma += float(valor)

    if suma > 0: #verifica si se sumaron valores o no.
        return suma
    else:
        return -1
#---------------------------------------------------------------------------------------------------------------------------------------

def cantidad_heroes_genero(lista_heroes: list[dict], genero: str) -> int: #funcion que contabiliza la cantidad de heroes de cada genero.
    cantidad = 0

    for heroe in lista_heroes:
        if isinstance(heroe, dict) and heroe.get("genero") == genero:
            cantidad += 1  
    return cantidad
#---------------------------------------------------------------------------------------------------------------------------------------

def dividir_datos(dividendo:float, divisor:float)-> float: #como parámetro dos números (dividendo y divisor). 

    if divisor == 0: #si es 0 retorno 0 sino hago la division.
        return 0
    else:
        division = dividendo / divisor
        return division

#---------------------------------------------------------------------------------------------------------------------------------------

def calcular_promedio_genero(lista_heroes: list[dict], genero: str) -> float: #calculo el promedio llamando a la funcion de sumar los datos, obtener la cantidad de heroes en comun y divido.
    suma = sumar_dato_heroe_genero(lista_heroes, "altura", genero)
    cantidad = cantidad_heroes_genero(lista_heroes, genero)
    promedio = dividir_datos(suma, cantidad)
    return promedio #retorno el promedio

#---------------------------------------------------------------------------------------------------------------------------------------

def stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes: list[dict], genero: str) -> str:
    if len(lista_heroes) == 0:
        print("Error: Lista de héroes vacía.")
        return False
    else:
        promedio = calcular_promedio_genero(lista_heroes, genero) #muestro el promedio de genero en base a la altura.
        if promedio != -1:
            print(f"Altura promedio género {genero}: {promedio:.2f}") #guardo el archivo en un csv.
            nombre_archivo = f"heroes_promedio_altura_{genero}.csv"
            contenido_archivo = f"Altura promedio género {genero}: {promedio:.2f}"
            guardar_archivo(nombre_archivo, contenido_archivo)
            return True
        else:
            print(f"No se encontraron héroes {genero}.") #si el genero no es ese retorno un mensaje.
            return False
        
#---------------------------------------------------------------------------------------------------------------------------------------

def calcular_cantidad_tipo(lista_heroes: list[dict], tipo_dato: str) -> dict: #funcion que sirve para contar la cantidad de datos.
    if not lista_heroes:
        return {"Error": "La lista se encuentra vacía"} #verifico que no este vacia.

    cantidad_tipo = {}

    for heroe in lista_heroes: #itero para sacar cuantos tipos tengo de cada dato del diccionario.
        if tipo_dato in heroe:
            valor = heroe[tipo_dato]
            valor = capitalizar_palabras(valor)
            cantidad_tipo[valor] = cantidad_tipo.get(valor, 0) + 1

    return cantidad_tipo

#---------------------------------------------------------------------------------------------------------------------------------------

def guardar_cantidad_heroes_tipo(diccionario: dict, tipo_dato: str) -> str:
    mensaje = [f"Caracteristica: {tipo_dato} {key} - Cantidad de heroes: {value}" for key, value in diccionario.items()] #formateo el mensaje segun el tipo de dato.
    mensaje_final = "\n".join(mensaje)
    nombre_archivo = f"heroes_cantidad_{tipo_dato}.csv" #guardo en csv.
    return guardar_archivo(nombre_archivo, mensaje_final)

#---------------------------------------------------------------------------------------------------------------------------------------

def stark_calcular_cantidad_por_tipo(lista_heroes: list[dict], tipo_dato: str) -> bool:
    claves_permitidas = ["nombre", "identidad", "empresa", "altura", "peso", "genero", "color_ojos", "color_pelo", "fuerza", "inteligencia"] #establezco los datos existentes.

    if tipo_dato not in claves_permitidas:
        print("Error: Tipo de dato no válido")
        return False

    resultado = calcular_cantidad_tipo(lista_heroes, tipo_dato)
    if not resultado:
        print(f"No se encontraron héroes con el tipo de dato {tipo_dato}")
        return False

    exito = guardar_cantidad_heroes_tipo(resultado, tipo_dato) #si encuentro coincidencias entre el dato ingresado los muestros pòr el csv.
    return exito

#---------------------------------------------------------------------------------------------------------------------------------------

def obtener_lista_de_tipos(lista_heroes: list[dict], tipo_dato: str) -> set: #funcion que elimina duplicados
    lista_valores = []

    for heroe in lista_heroes:
        valor = heroe.get(tipo_dato)
        if valor:
            valor = valor.strip().title() #capitalizo los valores
        else:
            valor = "N/A" #si no  hay dato se muestrea N/A
        lista_valores.append(valor)

    lista_valores = list(set(lista_valores))
    return lista_valores

#---------------------------------------------------------------------------------------------------------------------------------------

def normalizar_dato(key: str, valor_default: str) -> str: #realizar  validaciones en la clave para que el formato tenga ciertas condiciones.
    if key.strip() == "":
        return valor_default
    else:
        return key

#---------------------------------------------------------------------------------------------------------------------------------------

def normalizar_heroe(diccionario: dict, key: str) -> dict: #normalizo los datos del diccionario.
    try:
        valor = diccionario[key]
        valor = normalizar_dato(valor, "N/A")
        valor = capitalizar_palabras(valor)
        diccionario[key] = valor

        nombre = diccionario.get("nombre", "")
        nombre = capitalizar_palabras(nombre)
        diccionario["nombre"] = nombre

        return diccionario
    except KeyError:
        print(f"La clave '{key}' no existe en el diccionario.")
        return diccionario

#---------------------------------------------------------------------------------------------------------------------------------------
def obtener_heroes_por_tipo(heroes: list, tipos: set, tipo_dato: str) -> dict:
    diccionario_variedades = {tipo: [] for tipo in tipos} #obtener los nombres de los heroes segun el dato. Se genera una lista de cada grupo.

    for heroe in heroes:
        valor = normalizar_dato(heroe.get(tipo_dato, ""), "N/A")
        if valor in tipos:
            diccionario_variedades[valor].append(heroe.get("nombre", ""))

    return diccionario_variedades
#---------------------------------------------------------------------------------------------------------------------------------------

def guardar_heroes_por_tipo(diccionario: dict, tipo_dato: str) -> bool:
    try:
        archivo = f"heroes_segun_{tipo_dato}.csv" #se guardan los grupos con los nombres en un csv.
        contenido = ""

        for tipo, nombres_heroes in diccionario.items(): #formateo como se muestra.
            contenido += f"{tipo}: "
            contenido += " | ".join(nombres_heroes)
            contenido += "\n"

        guardar_archivo(archivo, contenido)
        return True
    except:
        return False
    
#---------------------------------------------------------------------------------------------------------------------------------------

def stark_listar_heroes_por_dato(heroes: list, tipo_dato: str) -> str: #listo los personajes con sus datos.
    tipos = obtener_lista_de_tipos(heroes, tipo_dato)
    diccionario = obtener_heroes_por_tipo(heroes, tipos, tipo_dato)
    return guardar_heroes_por_tipo(diccionario, tipo_dato)

#---------------------------------------------------------------------------------------------------------------------------------------

def stark_marvel_app_5(): #menu que contiene todas las funciones.
    flag_bienvenida = False
    opcion = ""
    while opcion != "Z":
        os.system("cls")
        opcion = imprimir_menu_desafio_5().strip()

        match opcion:
            case "A":
                print("Entendido, comencemos.")
                flag_bienvenida = True

            case "B":
                if flag_bienvenida:
                    genero = "M"
                    resultado = stark_guardar_heroe_genero(lista_heroes, genero)
                    print(f"Se guardaron los héroes en el archivo: heroes_{genero}.csv") if resultado else print(f"Error al guardar el archivo: heroes_{genero}.csv")
                else:
                    print("Debe poner confirmar para saber más información.")

            case "C":
                if flag_bienvenida:
                    genero = "F"
                    resultado = stark_guardar_heroe_genero(lista_heroes, genero)
                    print(f"Se guardaron los héroes en el archivo: heroes_{genero}.csv") if resultado else print(f"Error al guardar el archivo: heroes_{genero}.csv")
                else:
                    print("Debe poner confirmar para saber más información.")

            case "D":
                if flag_bienvenida:
                    resultado = stark_calcular_imprimir_guardar_heroe_genero(lista_heroes)
                    print(resultado)
                else:
                    print("Debe poner confirmar para saber más información.")

            case "E":
                if flag_bienvenida:
                    genero = input("Ingrese el género (M/F): ").upper()
                    exito = stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes, genero)
                    print(f"Éxito al calcular y guardar el promedio para el género {genero}: {exito}")
                else:
                    print("Debe poner confirmar para saber más información.")

            case "F":
                if flag_bienvenida:
                    tipo_dato = input("Ingrese el tipo de dato a calcular y guardar: ")
                    exito = stark_calcular_cantidad_por_tipo(lista_heroes, tipo_dato)
                    print(f"Éxito al calcular y guardar la cantidad por tipo de dato: {exito}")
                else:
                    print("Debe poner confirmar para saber más información.")

            case "G":
                if flag_bienvenida:
                    tipo_dato = input("Ingrese el tipo de dato a evaluar (color_pelo, color_ojos, etc.): ")
                    resultado = stark_listar_heroes_por_dato(lista_heroes, tipo_dato)
                    print("Archivo guardado exitosamente.") if resultado else imprimir_dato("Hubo un error al guardar el archivo.")
                else:
                    print("Debe poner confirmar para saber más información.")

            case "Z":
                salir = input("¿Confirma la salida? (Z): ")
                if salir == "s":
                    break
        input("Presione enter para continuar")

stark_marvel_app_5()