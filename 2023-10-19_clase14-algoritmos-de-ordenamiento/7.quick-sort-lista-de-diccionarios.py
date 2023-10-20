import json
import random as rd
from time import time 

def limpiar_consola():
    import os
    if os.name in ["ce", "nt", "dos"]: # windows
        os.system("cls")
    else: # linux o mac
        os.system("clear")
limpiar_consola()

def cargar_json(path:str)->list:
    with open(path,"r") as file:
        buffer_dict = json.load(file)
    return buffer_dict["heroes"]

def quick_sort_heroes(lista: list[dict], key):
    if len(lista) < 2:
        return lista
    else:
        lista_copia = lista.copy()
        heroe_pivot = lista_copia.pop()
        mas_grandes = []
        mas_chicos = []
        for heroe in lista_copia:
            if heroe[key] > heroe_pivot[key]:
                mas_grandes.append(heroe)
            elif heroe[key] <= heroe_pivot[key]:
                mas_chicos.append(heroe)
        return quick_sort_heroes(mas_chicos, key) + [heroe_pivot] + quick_sort_heroes(mas_grandes, key)

def unir_listas(lista):
    return lista

if __name__ == '__main__':

    lista1 = ["lionel", "luis", "rodri"]
    lista2 = ["tomy", "rafa", "leo"]
    lista3 = ["marian", "alex"]
    print(type(unir_listas(lista1 + lista2 + lista3)))
    print(unir_listas(lista1 + lista2 + lista3))

    lista_diccionarios = cargar_json('data_stark.json')
    
    key = 'peso'
    
    lista_ordenada_por_clave = quick_sort_heroes(lista_diccionarios, key)

    print("\n")    
    
    for heroe in lista_ordenada_por_clave:
        print(f'{key.capitalize()}: {heroe[key]} | Nombre: {heroe["nombre"]}')
    
    print("\n")    
