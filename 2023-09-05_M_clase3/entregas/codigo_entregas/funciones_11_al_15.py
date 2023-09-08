nro_ejercicio = input("\nNro. de ejercicio a ejecutar (11 - 15): ")
while not nro_ejercicio.isdigit() or not (int(nro_ejercicio) >= 11 and int(nro_ejercicio) <= 15):  
    nro_ejercicio = input("\nNro. de ejercicio a ejecutar (11 - 15): ")

match nro_ejercicio: 

    case "11":

        # Crea una función que reciba como parámetro una cadena de texto y devuelva la cantidad de vocales que tiene.

        def cantidad_vocales(cadena: str) -> int:
            cadena = cadena.lower()
            cantidad_vocales = 0
            for caracter in cadena:
                if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
                    cantidad_vocales += 1
            return cantidad_vocales

        print(f"\nEjercicio #11:\n")
        print("Crea una función que reciba como parámetro una cadena de texto\n y devuelva la cantidad de vocales que tiene.\n")

        cadena = input("Ingrese in string: ")
        while not cadena:
            cadena = input("Ingrese in string: ")
        
        resultado = cantidad_vocales(cadena)
        print(f"\n{cadena} tiene {resultado} vocales\n")

    case "12":

        # Crea una función que reciba dos listas de nombres, y devuelva una lista con los nombres que aparecen en ambas listas

        def nombres_duplicados(lista_1: list, lista_2: list) -> list:
            
            lista_duplicados = []

            for nombre in lista_1: 
                if any(nombre == i for i in lista_2):
                    lista_duplicados.append(nombre)

            return lista_duplicados 

        lista_nombres_1 = ["pablo", "lautaro", "daniel", "carolina", "valeria"]
        lista_nombres_2 = ["daniel", "valeria", "santiago", "lautaro", "fernanda"]

        resultado = nombres_duplicados(lista_nombres_1, lista_nombres_2)

        print(f"\nEjercicio #12:\n")
        print("Crea una función que reciba dos listas de nombres,\n y devuelva una lista con los nombres que aparecen en ambas listas\n")

        print("Lista A:")
        print(f"{lista_nombres_1}\n")
        print("Lista B:")
        print(f"{lista_nombres_2}\n")
        print("Lista de nombres duplicados:")
        print(f"{resultado}\n")
            

    case "13":
        
        # Crear una función que recibe una lista de palabras y devuelve un diccionario con las palabras como llaves y su longitud como valores.

        print(f"\nEjercicio #13:\n")
        print("Crear una función que recibe una lista de palabras\n y devuelve un diccionario con las palabras como llaves\n y su longitud como valores.\n")

    case "14":

        # Crear una función que recibe una lista de números y devuelve un diccionario con el valor mínimo, el valor máximo y el promedio de los números en la lista.

        print(f"\nEjercicio #14:\n")
        print("Crear una función que recibe una lista de números\n y devuelve un diccionario con el valor mínimo,\n el valor máximo y el promedio de los números en la lista.\n")

    case _:
        
        # Crear una función que recibe una lista de diccionarios con información de películas (título, género, director) y devuelve un diccionario con la cantidad de películas por género.

        print(f"\nEjercicio #15:\n")
        print("Crear una función que recibe una lista de diccionarios con información de películas (título, género, director)\n y devuelve un diccionario con la cantidad de películas por género.\n")