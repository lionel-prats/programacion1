""" 
13) Crea un diccionario que contenga el nombre y el nivel de dificultad de varios juegos de mesa. Luego, pedirle al usuario un nivel de dificultad, buscar los que coinciden e imprimir sus nombres
"""

info_juegos_de_mesa = {
    "Monopoly": "Intermedio",
    "Truco": "Facil",
    "Canasta": "Facil",
    "Poker": "Dificil"
}

# nivel_de_dificultad = input("Ingrese el nivel de dificultad: ").capitalize()

# print("usando items()")
# for k, v in info_juegos_de_mesa.items():
#     if v == nivel_de_dificultad:
#         print(k)

# print("usando keys()")
# for k in info_juegos_de_mesa.keys():
#     if info_juegos_de_mesa[k] == nivel_de_dificultad:
#         print(k)
    
juego = input("Ingrese el juego: ").capitalize()
nivel_de_dificultad = input("Ingrese el nivel de dificultad: ").capitalize()

info_juegos_de_mesa[juego] = nivel_de_dificultad

print(info_juegos_de_mesa)

# entrega de ejercicios
# grupo alfa
# onlinegdb.com
# elegimos python3 en "Lenguaje"
# en la web hay 2 desafios mas (donde?) (https://www.pybeselegidos.fun/2-native-forest)

""" 
Alumno: Lionel Prats 
División: 1H
Legajo: xxx
"""
pass
pass
pass
pass
pass

""" 
Diccionarios 1 al 10
Diccionarios 10 al 23
Funciones 1 al 10
Funciones 10 al 15
"""