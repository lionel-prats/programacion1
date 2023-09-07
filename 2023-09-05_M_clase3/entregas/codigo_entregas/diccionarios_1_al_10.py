""" 
Alumno: Lionel Prats 
DNI: 31367577
División: 1H
Nro. legajo: 115678
"""

nro_ejercicio = input("\nNro. de ejercicio a ejecutar (1 - 10): ")
while not nro_ejercicio.isdigit() or not (int(nro_ejercicio) >= 1 and int(nro_ejercicio) <= 10):  
    nro_ejercicio= input("Nro. de ejercicio a ejecutar (1 - 10): ")

match nro_ejercicio: 
    case "1":

        """  
        1) Crea un diccionario que represente los días de la semana, donde las claves son los nombres de los días y los valores son los números correspondientes (por ejemplo, {"lunes": 1, "martes": 2, ...}). Imprime el valor correspondiente al día "miércoles".
        """
        dias_semana = {
            "lunes": 1,
            "martes": 2,
            "miercoles": 3,
            "jueves": 4,
            "viernes": 5
        }

        print(f"\nEjercicio #1:\n")
        print("""Crea un diccionario que represente los días de la semana, \ndonde las claves son los nombres de los días y los valores son los números correspondientes\n (por ejemplo, {"lunes": 1, "martes": 2, ...}).\n Imprime el valor correspondiente al día "miércoles".\n""")

        print(f"Clave: miercoles\nValor: {dias_semana['miercoles']}")
    
    case "2":
        
        """
        2) Crea un diccionario que represente los meses del año, donde las claves son los nombres de los meses y los valores son sus números correspondientes (por ejemplo, {"enero": 1, "febrero": 2, ...}). Imprime el número correspondiente al mes "julio".
        """
        meses_anio = {
            "enero": 1,
            "febrero": 2,
            "marzo": 3,
            "abril": 4,
            "mayo": 5,
            "junio": 6,
            "julio": 7,
            "agosto": 8,
            "septiembre": 9,
            "octubre": 10,
            "noviembre": 11,
            "diciembre": 12
        }

        print(f"\nEjercicio #2:\n")

        print("""Crea un diccionario que represente los meses del año, donde las claves son los nombres de los meses\n y los valores son sus números correspondientes (por ejemplo, {"enero": 1, "febrero": 2, ...}).\n Imprime el número correspondiente al mes "julio".\n""")

        print(f"Clave: julio\nValor: {meses_anio['julio']}")

    case "3":
        
        """
        3) Crea un diccionario que contenga la información de una película, como título, director y año de estreno. Luego, imprime el título de la película.
        """
        pelicula = {
            "titulo": "Gladiador",
            "director": "Ridley Scott",
            "anio_estreno": 2000
        }

        print(f"\nEjercicio #3:\n")
        print("""Crea un diccionario que contenga la información de una película, como título, director y año de estreno. Luego, imprime el título de la película.\n""")

        print(f"Título de la película: {pelicula['titulo']}")

    case "4":
        
        """
        4) Crea un diccionario que contenga la información de una dirección: nombre de la calle, altura, localidad, código postal, partido y provincia. Luego, imprime el nombre de la calle, seguido de su altura.
        """
        direccion = {
            "nombre_calle": "Montes de Oca",
            "altura": "1414",
            "localidad": "Ciudadela",
            "codigo_postal": "1154",
            "partido": "Tres de Febrero",
            "provincia": "Buenos Aires"
        }

        print(f"\nEjercicio #4:\n")
        print("""Crea un diccionario que contenga la información de una dirección:\n nombre de la calle, altura, localidad, código postal, partido y provincia.\n Luego, imprime el nombre de la calle, seguido de su altura.\n""")

        print(f"Nombre de la calle: {direccion['nombre_calle']}\nAltura: {direccion['altura']}")

    case "5":
        
        """
        5) Crea un diccionario que represente los continentes, donde las claves son los nombres de los continentes y los valores son los números correspondientes (por ejemplo, {"América": 1, "Europa": 2, ...}). Imprime el valor correspondiente al continente "África".
        """
        continentes = {
            "África": 1,
            "América": 2,
            "Asia": 3,
            "Europa": 4,
            "Oceanía": 5
        }

        print(f"\nEjercicio #5:\n")
        print("""Crea un diccionario que represente los continentes,\n donde las claves son los nombres de los continentes y los valores son los números correspondientes\n (por ejemplo, {"América": 1, "Europa": 2, ...}). \nImprime el valor correspondiente al continente "África".\n""")

        print(f"Clave: África\nValor: {continentes['África']}")

    case "6":
    
        """
        6) Crea un diccionario que represente las estaciones del año, donde las claves son los nombres de las estaciones y los valores son los números correspondientes (por ejemplo, {"primavera": 1, "verano": 2, ...}). Imprime el valor correspondiente a la estación "invierno".
        """
        estaciones = {
            "invierno": 1,
            "otono": 2,
            "primavera": 3,
            "verano": 4
        }

        print(f"\nEjercicio #6:\n")
        print("""Crea un diccionario que represente las estaciones del año,\n donde las claves son los nombres de las estaciones y los valores son los números correspondientes\n (por ejemplo, {"primavera": 1, "verano": 2, ...}).\n Imprime el valor correspondiente a la estación "invierno".\n""")

        print(f"Clave: Invierno\nValor: {estaciones['invierno']}")

    case "7":

        """
        7) Crea un diccionario que contenga la información de una canción: título, artista y duración. Luego, imprime la duración de la canción.
        """
        cancion = {
            "titulo": "El Riesgo",
            "artista": "El plan de la mariposa",
            "duracion": "3'30\""
        }

        print(f"\nEjercicio #7:\n")
        print("""Crea un diccionario que contenga la información de una canción: título, artista y duración.\n Luego, imprime la duración de la canción.\n""")

        print(f"La canción dura {cancion['duracion']}")

    case "8":
        
        """
        8) Crea un diccionario que represente las edades de varias personas, donde las claves son los nombres de las personas y los valores son sus edades. Imprime la edad de la persona más joven.
        """
        personas = {
            "alex": 30,
            "carolina": 28,
            "luis": 32,
            "mariela": 40,
            "rafael": 23,
            "rocio": 26
        }

        edad_persona_mas_joven = 1
        primera_clave = True

        for k, v in personas.items():
            if primera_clave:
                edad_persona_mas_joven = v
                primera_clave = False
            elif v < edad_persona_mas_joven:
                edad_persona_mas_joven = v

        print(f"\nEjercicio #8:\n")
        print("""Crea un diccionario que represente las edades de varias personas,\n donde las claves son los nombres de las personas y los valores son sus edades.\n Imprime la edad de la persona más joven.\n""")

        print(f"La persona más joven del diccionario tiene {edad_persona_mas_joven} años")

    case "9":
        
        """
        9) Crea un diccionario que contenga las capitales de los países de América del Sur. Luego, pide al usuario que ingrese el nombre de un país y muestra su capital correspondiente.
        """
        capitales_america_del_sur = {
            "Argentina": "Buenos Aires",
            "Bolivia": "La Paz",
            "Brasil": "Brasilia",
            "Chile": "Santiago de Chile",
            "Colombia": "Bogotá",
            "Ecuador": "Quito",
            "Guayana Francesa": "Cayena",
            "Guyana": "Georgetown",
            "Paraguay": "Asunción",
            "Peru": "Lima",
            "Surinam": "Paramaribo",
            "Uruguay": "Montevideo",
            "Venezuela": "Caracas"
        }

        print(f"\nEjercicio #9:\n")
        print("""Crea un diccionario que contenga las capitales de los países de América del Sur.\n Luego, pide al usuario que ingrese el nombre de un país y muestra su capital correspondiente.\n""")

        nombre_pais= input("Ingrese el nombre de un pais de América del Sur: ").capitalize()

        capital = capitales_america_del_sur.get(nombre_pais, "El pais ingresado no corresponde a América del Sur")
        mensaje = f"Pais ingresado: {nombre_pais}\nCapital: {capital}" 

        print(mensaje)

    case _:
        
        """
        10) Crea un diccionario que represente las notas de un examen de varios estudiantes, donde las claves son los nombres de los estudiantes y los valores son sus notas. Imprime el promedio de las notas.
        """
        alumnos_notas = {
            "alex": 86,
            "carolina": 67,
            "luis": 80,
            "mariela": 76,
            "rafael": 65,
            "rocio": 81
        }

        total_suma_notas = 0
        total_alumnos = 0

        for v in alumnos_notas.values():
            total_suma_notas += v
            total_alumnos += 1

        promedio_notas = total_suma_notas / total_alumnos 

        print(f"\nEjercicio #10:\n")
        print("""Crea un diccionario que represente las notas de un examen de varios estudiantes,\n donde las claves son los nombres de los estudiantes y los valores son sus notas.\n Imprime el promedio de las notas.\n""")

        print(f"El promedio de notas obtenidas entre los alumnos del diccionario es {promedio_notas:.2f}")