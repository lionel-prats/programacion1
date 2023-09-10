""" 
Alumno: Lionel Prats 
DNI: 31367577
División: 1H
Nro. legajo: 115678
Funciones - Ejercicio 11 al 15
"""

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

        cadena = input("Ingrese un string: ")
        while not cadena:
            cadena = input("Ingrese un string: ")
        
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
        
        def diccionario_palabras(lista_de_palabras: list) -> dict:
            diccionario_palabras = {}
            for palabra in lista_de_palabras:
                diccionario_palabras[palabra] = len(palabra)
            return diccionario_palabras

        lista_de_palabras = ["murcielago", "ornitorrinco", "auto", "pepsi"]
        resultado = diccionario_palabras(lista_de_palabras)

        print(f"Lista de palabras: {lista_de_palabras}")
        
        print(f"\nDiccionario largo palabras:\n")

        for k, v in resultado.items():
            print(f"La palabra {k} tiene {v} caracteres.")

        print("\n")

    case "14":

        # Crear una función que recibe una lista de números y devuelve un diccionario con el valor mínimo, el valor máximo y el promedio de los números en la lista.

        print(f"\nEjercicio #14:\n")
        print("Crear una función que recibe una lista de números\n y devuelve un diccionario con el valor mínimo,\n el valor máximo y el promedio de los números en la lista.\n")

        def diccionario_numeros(lista_de_numeros: list) -> dict:
            minimo = None
            maximo = None
            suma_total = 0
            for numero in lista_de_numeros:
                if not minimo:
                    minimo = numero
                    maximo = numero
                elif numero < minimo:
                    minimo = numero
                elif numero > maximo:
                    maximo = numero

                suma_total += numero

            promedio = suma_total / len(lista_de_numeros)

            return {
                "minimo": minimo,
                "maximo": maximo,
                "promedio": round(promedio, 2)
            }

        lista_de_numeros = [5, 32, 8, 71, 3, 6]
        resultado = diccionario_numeros(lista_de_numeros)

        print(f"Lista de números: {lista_de_numeros}")
        print(f"\nDiccionario con datos de la lista:\n")
        print(f"minimo: {resultado['minimo']}")
        print(f"maximo: {resultado['maximo']}")
        print(f"promedio: {resultado['promedio']}\n")

    case _:
        
        # Crear una función que recibe una lista de diccionarios con información de películas (título, género, director) y devuelve un diccionario con la cantidad de películas por género.

        print(f"\nEjercicio #15:\n")
        print("Crear una función que recibe una lista de diccionarios con información de películas (título, género, director)\n y devuelve un diccionario con la cantidad de películas por género.\n")

        """
        def inventario_peliculas(lista_de_peliculas: list[dict]) ->dict:
            diccionario_generos = {}
            for pelicula in lista_de_peliculas:
                if "genero" in pelicula and pelicula['genero'] != "":
                    diccionario_generos[pelicula['genero']] = 0
                else: 
                    diccionario_generos['Sin Género'] = 0
            
            for pelicula in lista_de_peliculas:
                if not "genero" in pelicula or pelicula['genero'] == "":
                    diccionario_generos['Sin Género'] += 1
                else:
                    diccionario_generos[pelicula['genero']] += 1

            return diccionario_generos
        """

        def inventario_peliculas_2(lista_de_peliculas: list[dict]) ->dict:
            inventario_peliculas = {}
            for pelicula in lista_de_peliculas:
                
                # retorna el valor de la clave indicada en el 1er par. Si no existe tal clave en el dict, retorna el lo que hayamos definido en el 2do. par.
                genero = pelicula.get("genero", "Sin Género") 

                # si la clave "genero" en el diccionario pelicula es un string vacio, reescribo genero para que funcione correctamente
                if not genero:
                    genero = "Sin Género"
                
                # voy creando claves o pisandolas segun corresponda, y actualizando el value en el diccionario a retornar
                inventario_peliculas[genero] = inventario_peliculas.get(genero, 0) + 1

            return inventario_peliculas
            
        lista_de_peliculas = [
            {
                "titulo": "Transformers 1",
                "genero": "Ciencia Ficción",
                "director": "Michael Bay"
            },
            {
                "titulo": "300",
                "genero": "",
                "director": "Zack Snyder"
            },
            {
                "titulo": "Jurasic Park",
                "genero": "Aventura",
                "director": " Steven Spielberg"
            },
            {
                "titulo": "Matrix",
                "genero": "Ciencia Ficción",
                "director": "Lilly Wachowski"
            },
            {
                "titulo": "Gladiador",
                # "genero": "Acción",
                "director": "Ridley Scott"
            },
            {
                "titulo": "Forest Gump",
                "genero": "Drama",
                "director": "Robert Zemeckis"
            },
            {
                "titulo": "Jobs",
                "genero": "",
                "director": "Joshua Michael Stern"
            },
            {
                "titulo": "El código Da Vinci",
                "genero": "Misterio",
                "director": "Ron Howard"
            },  
            {
                "titulo": "Zoolander",
                "genero": "Comedia",
                "director": "Ben Stiller"
            },
            {
                "titulo": "El señor de los anillos",
                "genero": "Comedia",
                "director": "Peter Jackson"
            },
            {
                "titulo": "El juego del miedo",
                # "genero": "Terror",
                "director": "James Wan"
            },
            {
                "titulo": "Oppenheimer",
                "genero": "Comedia",
                "director": "Christopher Nolan"
            },
            {
                "titulo": "El código enigma",
                "genero": "Drama",
                "director": "Morten Tyldum"
            }
        ]

        if lista_de_peliculas:
            resultado = inventario_peliculas_2(lista_de_peliculas)
            print("Listado de películas de la lista con sus respectivos géneros:\n")        
            for i in range(len(lista_de_peliculas)):
                if not "genero" in lista_de_peliculas[i]:
                    print(f"{i + 1}) {lista_de_peliculas[i]['titulo']} (NO TIENE CLAVE \"genero\")")
                elif not lista_de_peliculas[i]["genero"]:
                    print(f"{i + 1}) {lista_de_peliculas[i]['titulo']} (\"genero\" ES UN STRING VACÍO)")
                else:
                    print(f"{i + 1}) {lista_de_peliculas[i]['titulo']} ({lista_de_peliculas[i]['genero']})")
            print("\nCantidad de películas por género en el listado de películas:\n")        
            for k, v in resultado.items():
                print(f"{k}: {v}")
            print("\n")
        else:
            print("La lista de películas está vacía.\n")