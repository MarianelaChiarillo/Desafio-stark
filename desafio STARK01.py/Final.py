from stark01 import *

def menu():

    print(
    """
    ***Menu de opciones***
    ----------------------------------------------------------------
    Bienvenido, comenzamos? s/n <-
    1. Nombre de todos los superheroes <-
    2. Nombre y altura de todos los superheroes <-
    3. El más alto de los superheroes <-
    4. El más bajo de los superheroes <-
    5. Promedio de alturas de los superheroes <-
    6. El más pesado de los superheroes <-
    7. El más liviano de los superheroes <-
    8. Nombre de todos los superheroes masculinos <-
    9. Nombre de todos los superheroes femeninos <-
    10. Nombre y altura del más alto de los superheroes masculinos <-
    11. Nombre y altura del más alto de los superheroes femeninos <-
    12. Nombre y altura del más bajo de los superheroes masculinos <-
    13. Nombre y altura del más bajo de los superheroes femeninos <-
    14. Promedio de alturas de los superheroes masculinos <-
    15. Promedio de alturas de los superheroes femeninos <-
    16. Cantidad de superheroes según su color de ojos <-
    17. Cantidad de superheroes según su color y tipo de pelo <-
    18. Cantidad de superheroes según su tipo de inteligencia <-
    19. Nombre de todos los superheroes según su tipo de: ojos <-
    20. Nombre de todos los superheroes según su tipo de: pelo <-
    21. Nombre de todos los superheroes según su tipo de: inteligencia <-
    22. Salir
    """)
    opcion = input("Ingrese una opción ---> ")
    return opcion
