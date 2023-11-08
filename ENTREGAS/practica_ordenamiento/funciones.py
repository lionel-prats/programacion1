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

""" 
Alumno: Lionel Prats 
DNI: 31367577
División: 1H
Nro. legajo: 115678
Practica Ordenamiento
"""

import os
import json
import re
import time
import uuid

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

def get_diccionaros_segun_clave(lista: list[dict], key: str, value: str):
    lista_comprimida = [diccionario for diccionario in lista if diccionario.get(key) == value]
    return lista_comprimida

def obtener_inteligencia_ingresada(dato: str):
    diccionario_equivalencias = {
        "a": "average",
        "g": "good",
        "h": "high"
    }
    return diccionario_equivalencias.get(dato) if dato in diccionario_equivalencias else False

def obtener_claves_validas():
    return ("altura", "fuerza", "identidad", "inteligencia", "nombre", "peso")

def guardar_csv(lista: list[dict], nombre_archivo: str):
    nombre_archivo = generar_nombre_unico_archivo(nombre_archivo)
    contenido = formatear_a_csv_contenido_lista_diccionarios(lista)
    try:
        with open(f"{nombre_archivo}", "w", encoding="utf-8") as nuevo_archivo:
            nuevo_archivo.write(f"{contenido}")
        return f"el archivo \"{nombre_archivo}\" ha sido creado correctamente"
    except:  
        return False
    
def generar_nombre_unico_archivo(nombre_generico, es_json=False):
    """ 
    genera un nombre unico para nombrar un archivo
    recibe un string que sera parte del nombre del archivo\n
    recibe un parametro opcional, un boolean, para definir si la extension sera .csv o .json
    retorna una cadena compuesta por dicho string + la fecha unix del momento de la ejecucion de la funcion + un hash aleatorio + la extension que corresponda\n
    """
    nombre_generico = nombre_generico.replace(" ","_").lower()
    timestamp = int(time.time() * 1000) # timestamp en milisegundos

    # uuid -> modulo de Python
    # uuid4() -> metodo de uuid que genera un identificador único universal (UUID-Universally Unique Identifier) de forma aleatoria
    # genera un id del tipo 550e8400-e29b-41d4-a716-446655440000, por lo que reemplazo los "-" por ""
    unique_id = str(uuid.uuid4()).replace("-", "")

    # nombre_archivo = f"{nombre_generico}__{timestamp}_{unique_id}.csv"
    nombre_archivo = f"{nombre_generico}__{timestamp}_{unique_id}"
    if es_json:
        nombre_archivo += ".json"
    else:
        nombre_archivo += ".csv"
    return nombre_archivo

def formatear_a_csv_contenido_lista_diccionarios(lista: list[dict]):
    nombres_campos = lista[0].keys()
    contenido = f"{';'.join(nombres_campos)}\n"
    for diccionario in lista:
        for v in diccionario.values():
            contenido += f"{str(v)};"
        contenido = contenido[:-1]
        contenido += "\n"
    contenido = contenido[:-1]
    
    return contenido