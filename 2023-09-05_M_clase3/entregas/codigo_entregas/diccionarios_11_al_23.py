"""
11) Crea un diccionario que represente una lista de tareas por hacer. Cada clave del diccionario debe ser el nombre de una tarea y cada valor debe ser su estado (los estados son:  pendiente, en proceso, completada). Imprimir todas las tareas seguido de su estado
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





"""
13) Crea un diccionario que contenga el nombre y el nivel de dificultad de varios juegos de mesa. Luego, pedirle al usuario un nivel de dificultad, buscar los que coinciden e imprimir sus nombres
"""






"""
14) Crea un diccionario que contenga el nombre como clave y el puntaje como valor de varios jugadores en un juego. Luego, pedirle al usuario el nombre del jugador y nuevo puntaje y actualizar el valor correspondiente en el diccionario.
"""






"""
15) Crea un diccionario que contenga el nombre y el sueldo de varios empleados. Luego, permite al usuario aumentar el sueldo de un empleado y actualizar el valor correspondiente en el diccionario.
"""






"""
16) Crea un diccionario que represente una lista de tareas pendientes, donde las claves son las tareas y los valores son "True" si están completadas y "False" si no lo están. Solicita al usuario el nombre de una tarea y modifica el valor para marcarla como completada. Imprimir el listado de tareas pendientes
"""






"""
17) Crea un diccionario que represente las películas de un cine, donde las claves son los nombres de las películas y los valores son los horarios correspondientes. Modifica el horario de la película "Avengers: Endgame" a las 19:30.
"""









"""
18) Crea un diccionario que represente los juegos de una consola, donde las claves son los nombres de los juegos y los valores son las puntuaciones correspondientes. Solicita al usuario el nombre de un juego y luego su puntuación, si el juego no existe agregarlo y si existe actualizar su puntuación 
"""









"""
19) Crea un diccionario que represente las temperaturas de una ciudad durante una semana, donde las claves son los días de la semana y los valores son las temperaturas correspondientes. Calcula la temperatura promedio de la semana.
"""







"""
20) Crea un diccionario que represente los asientos de un avión, donde las claves son los números de asientos y los valores son "True" si están ocupados y "False" si no lo están. Solicita al usuario un número de asiento y modifica su valor para marcarlo como ocupado. Luego imprimí la lista de asientos libres
"""






"""
21) Crea un diccionario que represente los gastos de una persona en diferentes categorías, donde las claves son los nombres de las categorías y los valores son los gastos correspondientes. Calcula el total de gastos de la persona.
"""







"""
22) Crea un diccionario que represente los gastos de una persona en diferentes categorías, donde las claves son los nombres de las categorías y los valores son los gastos correspondientes. Calcula el total de gastos de la persona en el mes.
"""







"""
23) Crea un diccionario que represente los contactos de un teléfono, donde las claves son los nombres de las personas y los valores son los números de teléfono correspondientes. Solicitar al usuario el nombre de un contacto: agregarlo al diccionario en caso de que no exista. En caso de que exista modificar el número de teléfono del contacto.
"""