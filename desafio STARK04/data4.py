from data_stark import *
from final4 import *
import re
import os


def extraer_iniciales(nombre_heroe: str) -> str:

    if not nombre_heroe:
        return 'N/A'
    else:
        nombre_heroe = nombre_heroe.replace('-', ' ') #reemplazo el guion por un espacio en blanco.

        nombre_heroe = re.sub(r'\bthe\b', '', nombre_heroe) #saco la palabra "the" asi no toma su inicial.

        iniciales = re.findall(r'\b\w', nombre_heroe.upper()) #busco todas las coincidencias que tienen mayusculas.
        iniciales_f = '.'.join(iniciales) + '.' #las agrego en una cadena que separa cada inicial.

        return iniciales_f
        
for personaje in lista_personajes: #recorro toda la lista.
    nombre = personaje["nombre"] #en la clave nombre.
    iniciales = extraer_iniciales(nombre) #busco las iniciales de la lista.
    #print(iniciales)

#........................................................................................................................................

def definir_iniciales_nombre(heroe:dict) -> bool: #defino la funcion con  un dict de heroe como parametro.

    if type(heroe) != dict and 'nombre' not in heroe.keys(): #verifico si heroe es de tipo dict y si se encuentra la key nombre.
        return False #si no es cierto retorno false.
    else:      
        nombre_heroe = heroe['nombre'] #sino continuo obtengo el nombre.
        iniciales = extraer_iniciales(nombre_heroe) #sus iniciales.
        heroe['iniciales'] = iniciales
        return True #retorno True.

#........................................................................................................................................

def agregar_iniciales_nombre(lista_personajes:list[dict]) -> bool:
    
    if type(lista_personajes) != list and len(lista_personajes) == 0: #verifico si lista de personajes de tipo list y si la lista contiene elementos.
        return False #si no es cierto retorno false.
    else:  
        for heroe in lista_personajes: #itero en la lista pasandole a la lista funcion de definir.
            if not definir_iniciales_nombre(heroe):
                print("El origen de datos no contiene el formato correcto") #si la funcion retorna false se muestra un mensaje por pantalla
                return False
        return True #si no hubo incovenientes la iteracion retorno true.
 #........................................................................................................................................
   
def stark_imprimir_nombres_con_iniciales(lista_personajes:list[dict]):
    if type(lista_personajes) != list and len(lista_personajes) == 0: #verifico si lista de personajes de tipo list y si la lista contiene elementos.
        return False #si no es cierto retorno false.
    else:
        if agregar_iniciales_nombre(lista_personajes): #llamo a la funcion agregar iniciales.
            for heroe in lista_personajes: #itero sobre la lista.
                nombre = heroe['nombre'] #obtengo el nombre del personaje.
                iniciales = heroe['iniciales'] #obtengo las iniciales.
                print(f'* {nombre} ({iniciales})') #lo organizo con formato donde tenga asterisco y parentesis.

#........................................................................................................................................

def generar_codigo_heroe(id_heroe:int, genero_heroe:str) -> str:

    if not isinstance(id_heroe, int) or genero_heroe not in ["F", "M", "NB"]: #verifico que el id sea un entero y el genero sea alguno de esos tres.
        return 'N/A' #si no cumple retorno N/A
    else:
        codigo_g = genero_heroe + '-' #genero el codigo genero con el genero y le agrego el guion para formato.
        codigo_id = str(id_heroe) #geneor el id
        codigo_id = '0' * (8 - len(codigo_id)) + codigo_id  # Genero un formato  con ceros a la izquierda y al final el codigo del id.
        codigo_heroe = codigo_g + codigo_id #concateno los dos datos, str y int.

        return codigo_heroe #retorno el codigo.
#.........................................................................................................................................

def agregar_codigo_heroe(heroe:dict, id_heroe:int) -> bool:
    if not heroe or len(heroe) == 0: #verifico si heroe es el dict o si no se encuentra vacio.
        return False #retorno falso en caso de serlo
    else:
        codigo = generar_codigo_heroe(id_heroe, heroe['genero']) #genero el codigo con la funcion generar codigo, junto al id y el genero.
        if codigo == 'N/A' or len(codigo) != 10: #recorro el codigo para que cumpla con los 10 caracteres.
            return False #retorno falso si no cumple
        heroe['codigo_heroe'] = codigo #sino agrego el codigo al diccionario.
        return True
#.........................................................................................................................................

def stark_generar_codigos_heroes(lista_personajes: list) -> str:

    if not lista_personajes or len(lista_personajes) == 0: #verifico que la lista no este vacia.
        print("El origen de datos no contiene el formato correcto") #muestro mensaje si no tiene elementos y finaliza.
        return
            
    for i in range(len(lista_personajes)): #itero en la lista de los personajes.
        heroe = lista_personajes[i]
        if type(heroe) != dict or 'genero' not in heroe: #verifico si los elementos son diccionarios con clave genero. Sino muestra mensaje y finaliza.
            print("El origen de datos no contiene el formato correcto")
            return
        
        id_heroe = i + 1 #itero
        if agregar_codigo_heroe(heroe, id_heroe): #genero el codigo utilizando la funcion agregar.
            print(f"* El código del héroe {id_heroe} es: {heroe['codigo_heroe']}") #muestro el id y el codigo
        else:
            print(f"No se pudo generar el código para el héroe {id_heroe}") #muestro mensaje que no se generaron codigos.
        
    print(f"Se asignaron {len(lista_personajes)} códigos") #saca el total de codigos asignados.

#.........................................................................................................................................

def sanitizar_entero(numero_str: str) -> int:
    if not isinstance(numero_str, str): #verifico que sea un str para poder eliminar los espacios cons strip, si no  es retorno -3.
        return -3
    
    numero_str = numero_str.strip()  #strip para eliminar espacios en blanco al inicio y final.

    if not re.match(r'^\d+$', numero_str):  #verificar si con regex si contiene caracteres no numéricos, si los tiene retorno -1.
        return -1

    numero = int(numero_str) #paso a int para poder compararlo con el 0 y saber si es negativo o no.

    if numero < 0:  #verificar si el número es negativo.
        return -2

    return numero

#.........................................................................................................................................

def sanitizar_flotante(numero_str: str) -> float:
    numero_str = numero_str.strip()  #elimino espacios en blanco al inicio y final
    
    if not re.match(r'^[-+]?[0-9]*\.?[0-9]+$', numero_str):  #verifico con regex si contiene caracteres no numéricos.
        return -1
    
    if float(numero_str) < 0:  #verifico si el número es negativo.
        return -2
    
    try:
        numero_float = float(numero_str)  # Convertir a float y validar si es si no muestra la excepcion.
        return numero_float
    except ValueError:
        return -3
    
#.........................................................................................................................................

def sanitizar_string(valor_str: str, valor_por_defecto: str = '-') -> str:
    valor_str = valor_str.strip()  # Eliminar espacios en blanco al inicio y final
    valor_por_defecto = valor_por_defecto.strip()  # Eliminar espacios en blanco al inicio y final
    
    tiene_num = False
    for caracter in valor_str:
        if caracter.isdigit():
            tiene_num = True
            break
    
    if tiene_num:  # Verificar si contiene números
        return "N/A"
    else:
        valor_str = valor_str.replace('/', ' ')  # Reemplazar la barra '/' por un espacio
        
        if len(valor_str) == 0 and valor_por_defecto != '':
            return valor_por_defecto.lower()
        
        return valor_str.lower()

#.........................................................................................................................................

def sanitizar_dato(heroe: dict, clave: str, tipo_dato: str) -> bool:
    tipo_dato = tipo_dato.lower()  # el tipo de dato lo convierto todo en minuscula.
    
    tipos_validos = ['string', 'entero', 'flotante'] #establezco que datos son validos.
    if tipo_dato not in tipos_validos: #si el dato no pertenece retorno falso.
        return False
    
    if clave not in heroe: #si la clave no esta en el diccionario, muestro mensaje.
        print('La clave especificada no existe en el héroe')
        return False

    valor = heroe[clave] #obtengo el valor de la clave en el diccionario.

    if tipo_dato == 'string': #verifico el dato str.
        if isinstance(valor, str): #analizo si es string.
            heroe[clave] = sanitizar_string(valor) #llamo a la funcion sanitizar str
        else:
            heroe[clave] = str(valor) #sino lo convierto a string.
    elif tipo_dato == 'entero': #verifico el dato entero
        try:
           heroe[clave] = sanitizar_entero(valor)
        except ValueError: #si no cumple retorna falso.
            return False
    elif tipo_dato == 'flotante': #verifico el dato flotante.
        try:
            heroe[clave] = sanitizar_flotante(valor)
        except ValueError:  #si no cumple retorna falso.
            return False

    return True

#.........................................................................................................................................
def stark_normalizar_datos(lista_heroes: list[dict]) -> None:
    if len(lista_heroes) == 0: #Verifico disponibilidad de elementos.
        print("Error: la lista de héroes está vacía.")
        return
    
    claves_a_sanitizar = ['altura', 'peso', 'color_ojos', 'color_pelo', 'fuerza', 'inteligencia'] #menciono las claves existentes.
    
    for heroe in lista_heroes: #itero en la lista.
        for clave in claves_a_sanitizar: #verico las claves.
            sanitizar_dato(heroe, clave, 'float') #sanitizo los datos en float.

        for clave, valor in heroe.items(): #itero las claves
            print(f"{clave}: {valor}") #muestro la clave y el valor sanitizado.
        print()

#.........................................................................................................................................

def generar_indice_nombres(lista_heroes: list[dict]) -> list[str]:
    if len(lista_heroes) == 0: #verifico que no este vacio.
        print("El origen de datos no contiene el formato correcto")
        return [] #retorno una lista vacia.

    nombres = [] #genero una lista vacia llamada nombres.

    for heroe in lista_heroes: #itero en la lista de personajes.
        if "nombre" in heroe: #si la clave nombre esta la lista.
            nombre = heroe["nombre"] #si la clave nombre esta obtengo el valor.
            palabras = nombre.split() #separo las palabras de los nombres con split.
            nombres.extend(palabras) #con extend agrego las palabras a la lista general.
        else:
            print("El origen de datos no contiene el formato correcto") #sino muestro mensaje.
            return []

    return nombres

resultado = generar_indice_nombres(lista_personajes)

#.........................................................................................................................................

def stark_imprimir_indice_nombre(lista_heroes:list[dict]):

    if len(lista_heroes) == 0: #verifico la lista si esta vacia.
        return "Lista vacia"
    else:
        nombres = generar_indice_nombres(lista_personajes) #implemento la funcion de generar_indice_nombres.
        resultado = "-".join(nombres) #le agrego el guion entre palabras.
        print(resultado)  # muestro el resultado.

#........................................................................................................................................

def convertir_cm_a_mtrs(valor_cm:float) -> float:
    if valor_cm <= 0:
         return -1  #retorna -1 si el valor recibido es negativo
    
    else:
        metros = valor_cm / 100  #calculo el valor de metros desde los centimetros.
        return metros
    
#........................................................................................................................................

def generar_separador(patron:str, largo:int, imprimir:True) -> str: #defino funcion.

    if len(patron) < 1 or len(patron) > 2 and largo < 1 or largo > 235: #recorro que el patron no se exceda y que la cantida de largo no sea 0 o mayor a 235.
        return "N/A" #retorno N/A
    else:
        separador = patron * largo  #genera el separador multiplicando el patrón por el largo
        if imprimir:
            print(separador)  # Imprime el separador si el parámetro imprimir es True
    return separador #lo retorno

#........................................................................................................................................

def generar_encabezado(titulo: str) -> str:
    titulo_mayus = titulo.upper() #establezco que el titulo este en mayuscula.
    separador = generar_separador('*', 50, False) #pongo cuanto quiero que se repita el caracter.
    encabezado = f"{separador}\n{titulo_mayus}\n{separador}" #realizo el formato.
    return encabezado #retorno el encabezado.

#........................................................................................................................................

def imprimir_ficha_heroe(heroe: dict) -> None:
    id_heroe = lista_personajes.index(heroe) + 1 #el id muestra el indice del heroe para poder utilizar la funcion codigo.
                                                                                                                                                                                                                                                                                                                                                                                                                                                               

    encabezados = ["PRINCIPAL", "FISICO", "SEÑAS PARTICULARES"] #formateo encabezados.
    for encabezado in encabezados:
        separador = generar_separador('*', 80, True)
        print(encabezado)
        print(separador)

        if encabezado == "PRINCIPAL": #muestro todos los elementos que pertenecen a principal con sus respectivos valores.
            print("NOMBRE DEL HÉROE:", heroe["nombre"])
            print("IDENTIDAD SECRETA:", heroe["identidad"])
            print("CONSULTORA:", heroe["empresa"])
            if agregar_codigo_heroe(heroe, id_heroe): #verifico lo de la funcion codigo.
                codigo_heroe = heroe['codigo_heroe']
                print(f"CÓDIGO DE HÉROE: {codigo_heroe}")
            else:
                print(f"No se pudo generar el código para el héroe {id_heroe}")
        elif encabezado == "FISICO": #muestro los elementos en fisico.
            if "altura" in heroe: #hago las conversiones de cm a mtrs de la clave altura.
                altura_str = heroe["altura"]
                if sanitizar_dato(heroe, "altura", "flotante"):
                    altura_cm = float(altura_str)
                    altura_mtrs = convertir_cm_a_mtrs(altura_cm)
                    print("ALTURA:", altura_mtrs, "Mtrs.")
            else:
                print("ALTURA: N/A")
            #sanitizo el resto de claves peso y fuerza.
            if "peso" in heroe:
                if sanitizar_dato(heroe, "peso", "flotante"):
                    print("PESO:", heroe["peso"], "Kg.")
            else:
                print("PESO: N/A")

            if "fuerza" in heroe:
                if sanitizar_dato(heroe, "fuerza", "entero"):
                    print("FUERZA:", heroe["fuerza"], "N")

        elif encabezado == "SEÑAS PARTICULARES": #muestro los elementos que pertencen a señas particulares.
            print("COLOR DE OJOS:", heroe["color_ojos"])
            print("COLOR DE PELO:", heroe["color_pelo"])
        print(separador)

#........................................................................................................................................

def stark_navegar_fichas(lista_heroes):
    if len(lista_heroes) == 0: #verifico la lista.
        print("Error: la lista de héroes está vacía.")
        return
    
    index_actual = 0 #inicializo el indice en 0.
    num_personajes = len(lista_heroes) #recorro la cantidad de personajes.
    continuar = True
    
    while continuar:
        heroe_actual = lista_heroes[index_actual] #analizo los indices de los heroes.
        imprimir_ficha_heroe(heroe_actual) #Imprimo la ficha.
        
        opcion = input(""" 
        Ingrese una opción: 
        [1] Ir a la izquierda <-
        [2] Ir a la derecha <-
        [S] Salir <-
        -->: """) #pido al usuario una opcion.
        
        if opcion == "1": #si es 1 retroceden las fichas de los personajes.
            index_actual -= 1
            if index_actual < 0:
                index_actual = num_personajes - 1
        elif opcion == "2": #si es positivo avanzo.
            index_actual += 1
            if index_actual >= num_personajes:
                index_actual = 0
        elif opcion.upper() == "S": #si es s salgo de las condiciones.
            continuar = False
        else:
            print("Opción no válida. Intente nuevamente.")

#........................................................................................................................................

#Hago el menu con las respectivas funciones.

def stark_marvel_app_3(lista_personajes):
    flag_bienvenida = False
    opcion = ""

    while opcion != "6":
        os.system("cls")
        opcion = stark_menu_principal()

        match(opcion):

            case "0":
                print("Entendido, comencemos.")
                flag_bienvenida = True

            case "1":
                if flag_bienvenida:
                    stark_imprimir_nombres_con_iniciales(lista_personajes)  
                else:
                    print("Debe poner confirmar para saber más información.")

            case "2":
                if flag_bienvenida:
                    stark_generar_codigos_heroes(lista_personajes) 
                else:
                    print("Debe poner confirmar para saber más información.")
            
            case "3":
                if flag_bienvenida:
                    stark_normalizar_datos(lista_personajes)
                else:
                    print("Debe poner confirmar para saber más información.")

            case "4":
                if flag_bienvenida:
                    stark_imprimir_indice_nombre(lista_personajes)
                else:
                    print("Debe poner confirmar para saber más información.")
                    
            case "5":
                if flag_bienvenida:
                    stark_navegar_fichas(lista_personajes)
                else:
                    print("Debe poner confirmar para saber más información.")
                    
            case "6":
                salir = input("confirma salida? s/n: ")
                if salir == "s":
                    break
        input("Presione enter para continuar")


stark_marvel_app_3(lista_personajes)