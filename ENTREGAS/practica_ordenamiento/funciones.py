# MIT License
#
# Copyright (c) 2022 [UTN FRA](https://fra.utn.edu.ar/) All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import json
import re

def limpiar_consola():
    """  
    limpia la consola
    """
    # os.system('cls' if os.name == 'nt' else 'clear')
    if os.name in ["ce", "nt", "dos"]: # windows
      os.system("cls")
    else: # linux o mac
      os.system("clear")

def leer_json(ruta_archivo):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido_json = json.load(archivo)
        return contenido_json
    except:
       return False

def ordenar_lista_diccionarios_metodo_quick_sort(lista: list[dict], key: str, orden: str = "a"):
   
    if len(lista) < 2:
        return lista
    else:
        lista_copia = lista.copy()
        diccionario_pivot = lista_copia.pop()
        lista_diccionarios_anteriores = []
        lista_diccionarios_posteriores = []
        for diccionario in lista_copia:
            if diccionario[key] > diccionario_pivot[key]:
                if orden.lower() == "a":
                    lista_diccionarios_posteriores.append(diccionario)
                elif orden.lower() == "d":
                    lista_diccionarios_anteriores.append(diccionario)
            elif diccionario[key] <= diccionario_pivot[key]:
                if orden.lower() == "a":
                    lista_diccionarios_anteriores.append(diccionario)
                elif orden.lower() == "d":
                    lista_diccionarios_posteriores.append(diccionario)
        return ordenar_lista_diccionarios_metodo_quick_sort(lista_diccionarios_anteriores, key, orden) + [diccionario_pivot] + ordenar_lista_diccionarios_metodo_quick_sort(lista_diccionarios_posteriores, key, orden)
        
def validar_dato(regex, dato, search = False):
    if search and re.search(regex, dato, re.IGNORECASE):
        return True
    elif re.match(regex, dato):
        return True
    return False 

def separador():
    print("\n---------------\n")

def imprimir_menu():
    menu = '''
1 - Listar los primeros N heroes
2 - Ordenar heroes por altura [Ascendente o Descendente]
3 - Ordenar heroes por fuerza [Ascendente o Descendente]
4 - Buscar heroes por inteligencia [good, average, high] 
5 - Exportar lista Ordenada de heroes ordenada [ASC o DESC] por una clave que decida el usuario a CSV
7 - Salir
'''
    print(menu)