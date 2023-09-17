# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1
# python pruebas.py

import os
if os.name in ["ce", "nt", "dos"]: # windows
    os.system("cls")
else: # linux o mac
    os.system("clear")

"""
estoy trabajando en python
tengo que hacer algo como esto
el problema es que las opciones validas son entre la a y la o (valen mayusculas o minusculas), y es demasiado engorroso validar por cada posibilidad
cual es la forma mas eficiente y profesional de hacerlo?
"""


def validar(input_usuario, lista_opciones_validas):
    if input_usuario == "Q":
        return False 
    input_usuario = input_usuario.lower() 
    return input_usuario in lista_opciones_validas

opciones_validas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "q"]

input_usuario = "M"

print(validar(input_usuario, opciones_validas))

