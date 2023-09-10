def mostrar_menu():
    """  
    Ejecuta todo nuestro programa
    """
    menu = \
    """
    11) Crea una función que reciba como parámetro una cadena de texto\n y devuelva la cantidad de vocales que tiene.

    12) Crea una función que reciba dos listas de nombres, y devuelva\n una lista con los nombres que aparecen en ambas listas

    13) Crear una función que recibe una lista de palabras y devuelve\n un diccionario con las palabras como llaves y su longitud como valores.

    14) Crear una función que recibe una lista de números y devuelve un\n diccionario con el valor mínimo, el valor máximo y el promedio de los números en la lista.

    15) Crear una función que recibe una lista de diccionarios con información de películas (título, género, director)\n y devuelve un diccionario con la cantidad de películas por género.
    
    0) Salir del programa.
    """

    inicio = True

    while True:

        if inicio:
            print(menu)
            opcion_elegida = input("""Ingrese una opción entre 11 y 15, o \"0\" para salir del programa: """)
            inicio = False 

        match opcion_elegida:
            case "0":
                break
            case "11":
                imprimir_nombres_de_heroes()
            case "22":
                imprimir_nombres_altura_de_heroes()
            case "13":
                heroe_mas_alto = determina_heroe_mas_alto()
                print(f"El heroe mas alto es {heroe_mas_alto}")
            case "14":
                pass
            case "15":
                pass
            case _:
                print("\n-----------------------------------------\n")
                print(menu)
                opcion_elegida = input("""Reingrese una opción entre 11 y 15, o \"0\" para salir del programa: """)
    return True


def imprimir_nombres_de_heroes():
    pass
def imprimir_nombres_altura_de_heroes():
    pass
def determina_heroe_mas_alto():
    pass

mostrar_menu()