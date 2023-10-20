import json
import random as rd
from time import time

ITERACIONES = 30000
lista_random_numeros = [
    rd.randint(0, 100000) for _ in range(ITERACIONES)
]

def ordenar_burbujeo(lista_numeros: list[int]):
    if not lista_numeros:
        print('La lista esta vacia')
    else:
        lista_copia = lista_numeros.copy()
        # Arranca nuestro algoritmo
        for indice_1 in range(len(lista_copia) - 1):
            for indice_2 in range(indice_1 + 1, len(lista_copia)):
                if lista_copia[indice_1] > lista_copia[indice_2]:
                    lista_copia[indice_1], lista_copia[indice_2] =\
                    lista_copia[indice_2], lista_copia[indice_1]
        return lista_copia


# el indice del elemento mas chiquito
def buscar_min(lista: list[int]):
    minimo = 0
    for indice in range(len(lista)):
        if lista[minimo] > lista[indice]:
            minimo = indice
    return minimo

def selection_sort_v1(lista: list[int]):
    if lista:
        lista_a_ordenar = lista.copy()
        lista_ordenada = []
        while len(lista_a_ordenar) > 0:
            indice_del_minimo = buscar_min(lista_a_ordenar)
            elemento_min = lista_a_ordenar.pop(indice_del_minimo)
            lista_ordenada.append(elemento_min)
        return lista_ordenada

def selection_sort_v2(lista: list[int]):
    if lista:
        lista_a_ordenar = lista.copy()
        for indice in range(len(lista_a_ordenar)):
            indice_del_minimo = buscar_min(lista_a_ordenar[indice:]) + indice
            lista_a_ordenar[indice], lista_a_ordenar[indice_del_minimo] =\
            lista_a_ordenar[indice_del_minimo], lista_a_ordenar[indice]
        return lista_a_ordenar


def quick_sort(lista: list[dict], key):

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
        return quick_sort(mas_chicos, key) + [heroe_pivot] + quick_sort(mas_grandes, key)

def cargar_json(path:str)->list:
    with open(path,"r") as file:
        buffer_dict = json.load(file)
    return buffer_dict["heroes"]

if __name__ == '__main__':
    
    lista_original = cargar_json('data_stark.json')
    key = 'fuerza'
    start = time()
    # Ordenamiento
    lista = quick_sort(lista_original, key)
    end = time()
    tiempo_total = end - start
    print(f'QuickSort Tardo: {tiempo_total}')
    
    for heroe in lista:
        print(f'{key.capitalize()}: {heroe[key]} | Nombre: {heroe["nombre"]}')

    # start = time()
    # # Ordenamiento
    # lista_original.sort()
    # end = time()
    # tiempo_total = end - start
    # print(f'Sort Lista Tardo: {tiempo_total}')