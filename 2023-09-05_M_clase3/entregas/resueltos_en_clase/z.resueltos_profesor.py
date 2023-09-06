
"""
1 - Crea un diccionario que represente los días de la semana, 
donde las claves son los nombres de los días y los valores 
son los números correspondientes (por ejemplo, {"lunes": 1, "martes": 2, ...}). 
Imprime el valor correspondiente al día "miércoles".

"""

dias_de_la_semana = {
    "lunes": 1, "martes": 2, "miercoles": 3, "jueves": 4, "viernes": 5, "sabado": 6, "domingo": 7
}

clave_a_buscar = 'miercoles'
print(dias_de_la_semana.get(clave_a_buscar, f'La clave {clave_a_buscar} no existe'))


"""
2 - Crea un diccionario que represente los meses del año, donde las claves son los nombres de los meses y los valores son sus números correspondientes (por ejemplo, {"enero": 1, "febrero": 2, ...}). Imprime el número correspondiente al mes "julio".
"""

meses_del_anho = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6, "julio": 7
}

numero_de_junio = meses_del_anho.get("junio", "Error 404")
print(numero_de_junio)

"""
3 - Crea un diccionario que contenga la información de una película, como título, director y año de estreno. Luego, imprime el título de la película.
"""

info_pelicula = {
    "titulo": "Reliquias de la muerte I",
    "director": "UTN Pirata",
    "año": "2023"
}

titulo_de_pelicula = info_pelicula.get("titulo", "La clave titulo no existe prro.")
print(titulo_de_pelicula)

"""
4 - Crea un diccionario que contenga la información de una dirección: nombre de la calle, altura, localidad, código postal, partido y provincia. Luego, imprime el nombre de la calle, seguido de su altura.
"""

direccion = {
    "nombre_calle": "calle falsa",
    "altura": "123",
    "localidad": "Springfield",
    "partido": "Springfield",
    "codigo_postal": "2525",
    "provincia": "Simpsoniana"
}

nombre_de_calle = direccion.get("nombre_calle", "El nombre de calle no fue definido")
altura_direccion = direccion.get("altura", "La altura de la direccion no fue definida")

dato_direccion = f'calle: {nombre_de_calle}\naltura: {altura_direccion}'
print(dato_direccion)

"""
9 - Crea un diccionario que contenga las capitales de los países de América del Sur. Luego, pide al usuario que ingrese el nombre de un país y muestra su capital correspondiente.

"""

capitales_america_del_sur = {
    "Argentina": "Buenos aires",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo",
    "Paraguay": "Asuncion",
    "Bolivia": "La Paz"
}

nombre_de_pais = input('Ingrese el nombre de un pais de ADS: ').capitalize()

capital_seleccionada = capitales_america_del_sur.get(nombre_de_pais)
mensaje = f'La capital de {nombre_de_pais} es {capital_seleccionada}!'
print(mensaje)

"""
13 - Crea un diccionario que contenga el nombre y el nivel de dificultad de varios juegos de mesa. Luego, pedirle al usuario un nivel de dificultad, buscar los que coinciden e imprimir sus nombres
"""

info_juegos_de_mesa = {
    "Monopoly": "Intermedio",
    "Truco": "Facil",
    "Canasta": "Facil",
    "Poker": "Dificil"
}

nivel_de_dificultad = input('Ingrese el nivel de dificultad: ').capitalize()

print('Usando items()')
for clave, valor in info_juegos_de_mesa.items():
    if valor == nivel_de_dificultad:
        print(clave)

