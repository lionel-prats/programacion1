import random as rd
from time import time 

def limpiar_consola():
    import os
    if os.name in ["ce", "nt", "dos"]: # windows
        os.system("cls")
    else: # linux o mac
        os.system("clear")
limpiar_consola()

def buscar_min(lista: list[int]):
    """  
    retorna el indice del menor elemento de la lista
    """
    retorno = -1
    if lista:
        minimo = 0
        for indice in range(len(lista)):
            if lista[minimo] > lista[indice]:
                minimo = indice
        retorno = minimo
    return retorno

def selection_sort_v1(lista: list[int]):
    if lista:
        lista_a_ordenar = lista.copy()
        lista_ordenada = []
        while len(lista_a_ordenar) > 0:
            indice_del_minimo = buscar_min(lista_a_ordenar)
            elemento_min = lista_a_ordenar.pop(indice_del_minimo)
            lista_ordenada.append(elemento_min)
    return lista_ordenada
 

if __name__ == "__main__":
    print("\nDemostracion con lista de 10 elementos:")
    lista_random_numeros = [5, 0.44, -4, 0, -8, 4, 1, 6, -4, 6]

    print("\nLista original:")
    print(lista_random_numeros)

    start = time()
    lista = selection_sort_v1(lista_random_numeros)
    end = time()
    tiempo_total = end - start
    print("\nCopia ordenada con selection_sort_v1()")
    print(lista)
    print(f"Tardó: {tiempo_total}")

    print("\nLista original:")
    print(lista_random_numeros)

    print("\n----------------------------------------------------------\n")

    print("demostracion con lista de 10000 elementos:")
    ITERACIONES = 10000
    lista_random_numeros = [
        rd.randint(0, 10000) for _ in range(ITERACIONES)
    ]
    start = time()
    lista = selection_sort_v1(lista_random_numeros)
    end = time()
    tiempo_total = end - start
    print("\nCopia ordenada con selection_sort_v1():")
    print(f"Tardó: {tiempo_total} segundos\n")