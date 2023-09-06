nro_ejercicio = input("Nro. de ejercicio a ejecutar (11 - 23): ")
while not nro_ejercicio.isdigit() or not (int(nro_ejercicio) >=11 and int(nro_ejercicio) <= 23):  
    nro_ejercicio= input("Nro. de ejercicio a ejecutar (11 - 23): ")

match nro_ejercicio: 

    case "11":
        """
        Crea un diccionario que represente una lista de tareas por hacer. Cada clave del diccionario debe ser el nombre de una tarea y cada valor debe ser su estado (los estados son:  pendiente, en proceso, completada). Imprimir todas las tareas seguido de su estado
        """
        tareas = {
            "lavar la ropa": "en proceso",
            "hacer las compras": "completada",
            "pasear al perro": "completada",
            "preparar la cena": "pendiente",
            "limpiar el cuarto": "en proceso"
        }

        print(f"\nEjercicio #11:")
        print(f"NOMBRE TAREA | ESTADO")
        for k, v in tareas.items():
            print(f"{k} | {v}")

    case "12":
        
        """
        12) Crea un diccionario que represente una lista de las compras. Cada clave del diccionario debe ser el nombre de un producto y cada valor debe ser su cantidad. Pedir al usuario que ingrese el nombre del producto e imprimir la cantidad
        """
        lista_de_compras = {
            "galletitas": 4,
            "jabon": 2,
            "leche": 5,
            "pan": 2,
            "pure instantaneo": 5
        }

        print(f"\nEjercicio #12:")
        producto= input("Ingrese el nombre de un producto: ").lower()

        cantidad = lista_de_compras.get(producto, "El producto ingresado no no está en el listado")
        mensaje = f"Producto ingresado: {producto}\nCantidad: {cantidad}" 

        print(mensaje)
    
    case "13":
        
        """
        13) Crea un diccionario que contenga el nombre y el nivel de dificultad de varios juegos de mesa. Luego, pedirle al usuario un nivel de dificultad, buscar los que coinciden e imprimir sus nombres
        """
        juegos = {
            "backgamon": "difícil",
            "juego de la oca": "fácil",
            "ajedrez": "difícil",
            "teg": "moderado",
            "monopoly": "fácil"
        }

        print(f"\nEjercicio #13:")
        dificultad= input("Ingrese el nivel de dificultad: ").lower()

        existe_juego = False
        posicion = 1
        print(f"Listado de juegos de dificultad \"{dificultad}\"")
        for k, v in juegos.items():
            if v == dificultad:
                existe_juego = True
                print(f"{posicion}- {k}")
                posicion += 1

        if not existe_juego:
            print("No hay juegos que coincidan con la dificultad ingresada")
    
    case "14":
        
        """
        14) Crea un diccionario que contenga el nombre como clave y el puntaje como valor de varios jugadores en un juego. Luego, pedirle al usuario el nombre del jugador y nuevo puntaje y actualizar el valor correspondiente en el diccionario.
        """
        jugadores = {
            "alex": 30,
            "carolina": 28,
            "luis": 32,
            "mariela": 40,
            "rafael": 23,
            "rocio": 26
        }
        jugadores_original = dict(jugadores)

        print(f"\nEjercicio #14:")
        jugador_ingresado= input("Ingrese el nombre del jugador: ").lower()

        while not len(jugador_ingresado): 
            jugador_ingresado= input("Ingrese el nombre del jugador: ").lower()

        nuevo_puntaje= input("Ingrese el nuevo puntaje: ")

        while not nuevo_puntaje.isdigit(): 
            nuevo_puntaje= input("Ingrese el nuevo puntaje: ")

        existe_jugador = False
        puntaje_anterior = None
        for k in jugadores.keys():
            if k == jugador_ingresado:
                existe_jugador = True
                puntaje_anterior = jugadores[jugador_ingresado]
                jugadores[jugador_ingresado] = nuevo_puntaje

        if existe_jugador:
            print(f"El puntaje de {jugador_ingresado} se actualizó correctamente.")
            print(f"Puntaje anterior {puntaje_anterior}.")
            print(jugadores_original)
            print(f"Puntaje actual {nuevo_puntaje}.")
            print(jugadores)
        else:
            print(f"El jugador ingresado no existe.")
    
    case "15":
        print("Ejercicio 15")
    
    case "16":
        print("Ejercicio 16")
    
    case "17":
        print("Ejercicio 17")
    
    case "18":
        print("Ejercicio 18")
    
    case "19":
        print("Ejercicio 19")
    
    case "20":
        print("Ejercicio 20")
    
    case "21":
        print("Ejercicio 21")
    
    case "22":
        print("Ejercicio 22")
    
    case _:
        print("Ejercicio 23")


















    






"""
15) Crea un diccionario que contenga el nombre y el sueldo de varios empleados. Luego, permite al usuario aumentar el sueldo de un empleado y actualizar el valor correspondiente en el diccionario.
"""
# empleados = {
#     "marcelo": 26800,
#     "fabiola": 25000,
#     "dante": 30000,
#     "sofia": 27000,
#     "valeria": 25500,
#     "tatiana": 29200
# }
# empleados_original = dict(empleados)

# print(f"\nEjercicio #15:")
# empleado_ingresado= input("Ingrese el nombre del empleado: ").lower()

# if not empleados.get(empleado_ingresado):
#     print("El nombre ingresado no existe en el diccionario")
# else:
#     salario_actualizado= input("Ingrese el nuevo salario: ")
#     while not salario_actualizado.isdigit(): 
#         salario_actualizado= input("Ingrese un monto válido: ")

#     salario_anterior = empleados[empleado_ingresado]
#     empleados[empleado_ingresado] = salario_actualizado
#     print(f"El salario de {empleado_ingresado} se actualizó correctamente.")
#     print(f"Salario anterior {salario_anterior}.")
#     print(empleados_original)
#     print(f"Salario actual {salario_actualizado}.")
#     print(empleados)





"""
16) Crea un diccionario que represente una lista de tareas pendientes, donde las claves son las tareas y los valores son "True" si están completadas y "False" si no lo están. Solicita al usuario el nombre de una tarea y modifica el valor para marcarla como completada. Imprimir el listado de tareas pendientes
"""
# tareas = {
#     "lavar la ropa": "False",
#     "hacer las compras": "False",
#     "pasear al perro": "False",
#     "preparar la cena": "False",
#     "limpiar el cuarto": "False"
# }
# tareas_original = dict(tareas)

# print(f"\nEjercicio #16:")
# tarea_ingresada= input("Ingrese la tarea a modificar: ").lower()

# if not tareas.get(tarea_ingresada):
#     print(f"La tarea \"{tarea_ingresada}\" no existe en el diccionario.")
# else:
#     tareas[tarea_ingresada] = "True"
#     print(f"\nLa tarea \"{tarea_ingresada}\" está completada! \n")

# print("Listado de tareas pendientes:")
# posicion = 1
# for k, v in tareas.items():
#     if v == "False":
#         print(f"{posicion}- {k}")
#         posicion += 1





"""
17) Crea un diccionario que represente las películas de un cine, donde las claves son los nombres de las películas y los valores son los horarios correspondientes. Modifica el horario de la película "Avengers: Endgame" a las 19:30.
"""
# peliculas = {
#     "Spiderman": "13:30",
#     "El Señor de los Anillos": "15:30",
#     "Harry Potter": "17:30",
#     "Avengers: Endgame": "19:00",
#     "Batman": "21:30"
# }
# peliculas_original = dict(peliculas)

# horario_anterior = peliculas["Avengers: Endgame"] 
# peliculas["Avengers: Endgame"] = "19:30"

# print("\nEjercicio #17:")
# print("El horario de Avengers: Endgame se actualizó correctamente")
# print(f"Horario anterior: {horario_anterior}")
# print(peliculas)
# print(f"Horario actualizado: {peliculas['Avengers: Endgame']}")
# print(peliculas)





"""
18) Crea un diccionario que represente los juegos de una consola, donde las claves son los nombres de los juegos y los valores son las puntuaciones correspondientes. Solicita al usuario el nombre de un juego y luego su puntuación, si el juego no existe agregarlo y si existe actualizar su puntuación 
"""
# juegos = {
#     "street fighter": 6,
#     "mortal kombat": 9,
#     "mario bross": 3,
#     "counter strike": 7,
#     "age of empires": 10,
#     "fifa 2021": 8
# }
# juegos_original = dict(juegos)

# print(f"\nEjercicio #18:")
# juego_ingresado = input("Ingrese un juego: ").lower()
# while not len(juego_ingresado): 
#     juego_ingresado = input("Ingrese un juego: ").lower()

# puntuacion_ingresada = input("Ingrese la puntuación del juego: ")
# while not puntuacion_ingresada.isdigit():  
#     puntuacion_ingresada= input("Ingrese la puntuación del juego: ")

# juegos[juego_ingresado] = puntuacion_ingresada

# print("Diccionario original:")
# print(juegos_original)
# print("Diccionario actualizado:")
# print(juegos)





"""
19) Crea un diccionario que represente las temperaturas de una ciudad durante una semana, donde las claves son los días de la semana y los valores son las temperaturas correspondientes. Calcula la temperatura promedio de la semana.
"""
# temperaturas = {
#     "lunes": 25.5,
#     "martes": 24,
#     "miercoles": 28,
#     "jueves": 14,
#     "viernes": 15,
#     "sabado": 30,
#     "domingo": 24
# }

# total_temperaturas = 0

# for v in temperaturas.values():
#     total_temperaturas += v

# promedio_temperaturas = total_temperaturas / 7 

# print(f"\nEjercicio #19:")
# print(f"El promedio semanal de la temperatura fué de: {promedio_temperaturas:.2f}°")





"""
20) Crea un diccionario que represente los asientos de un avión, donde las claves son los números de asientos y los valores son "True" si están ocupados y "False" si no lo están. Solicita al usuario un número de asiento y modifica su valor para marcarlo como ocupado. Luego imprimí la lista de asientos libres
"""
# asientos = {
#     "1": "True",
#     "2": "False",
#     "3": "True",
#     "4": "False",
#     "5": "False"
# }

# asientos_disponibles = False
# for v in asientos.values():
#     if v == "False":
#         asientos_disponibles = True

# print(f"\nEjercicio #20:")
# if not asientos_disponibles:
#     print("Todos los asientos están ocupados.")
# else:
#     asientos_original = dict(asientos)  
#     asiento_ingresado = input("Ingrese el número de asiento deseado (1-5): ")
#     while not asiento_ingresado.isdigit() or not (int(asiento_ingresado) >= 1 and int(asiento_ingresado) <= 5):
#         asiento_ingresado = input("Ingrese el número de asiento deseado (1-5): ")
        
#     if asientos[asiento_ingresado] == "True":
#         print(f"El asiento {asiento_ingresado} no está disponible.")
#     else:
#         asientos[asiento_ingresado] = "True"
#         print(f"Reservaste el asiento nro: {asiento_ingresado}")

#     mensaje = ""
#     for k, v in asientos.items():
#         if v == "False":
#             mensaje += f"{k} | "
#     mensaje = mensaje[:-2]
#     print(f"Listado de asientos libres: {mensaje}")





"""
21) Crea un diccionario que represente los gastos de una persona en diferentes categorías, donde las claves son los nombres de las categorías y los valores son los gastos correspondientes. Calcula el total de gastos de la persona.
"""
# gastos = {
#     "alquiler": 70000,
#     "cuota auto": 24000,
#     "impuestos": 2500,
#     "ocio": 7000,
#     "servicios": 11000,
# }

# total_gastos = 0
# for v in gastos.values():
#     total_gastos += v
# print(f"\nEjercicio #21:")
# print(f"Total gastos: ${total_gastos}")



"""
22) Crea un diccionario que represente los gastos de una persona en diferentes categorías, donde las claves son los nombres de las categorías y los valores son los gastos correspondientes. Calcula el total de gastos de la persona en el mes.
"""
# gastos = {
#     "alquiler": 70000,
#     "cuota auto": 24000,
#     "impuestos": 2500,
#     "ocio": 7000,
#     "servicios": 11000,
# }

# total_gastos = 0
# for v in gastos.values():
#     total_gastos += v
# print(f"\nEjercicio #22:")
# print(f"Total gastos mes: ${total_gastos}")





"""
23) Crea un diccionario que represente los contactos de un teléfono, donde las claves son los nombres de las personas y los valores son los números de teléfono correspondientes. Solicitar al usuario el nombre de un contacto: agregarlo al diccionario en caso de que no exista. En caso de que exista modificar el número de teléfono del contacto.
"""
# agenda = {
#     "gabriel": "4444",
#     "juan": "5555",
#     "mariano": "6666",
#     "emiliano": "7777",
#     "santiago": "8888",
#     "sergio": "9999"
# }
# agenda_original = dict(agenda)

# print(f"\nEjercicio #23:")
# contacto_ingresado = input("Ingrese un nombre: ").lower()
# while not len(contacto_ingresado): 
#     contacto_ingresado = input("Ingrese un nombre: ").lower()

# numero_ingresado = input("Ingrese un número telefónico: ")
# while not numero_ingresado.isdigit():  
#     numero_ingresado= input("Ingrese un número telefónico: ")

# agenda[contacto_ingresado] = numero_ingresado

# print("Agenda original:")
# print(agenda_original)
# print("Agenda actualizada:")
# print(agenda)


    