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

def burbujeo_sin_swap(lista_numeros):
    if not lista_numeros:
        print("La lista esta vacia")
    else:
        lista_copia = lista_numeros.copy() 
        numero_aux = None
        for indice1 in range(len(lista_copia) - 1):
            for indice2 in range(indice1 + 1, len(lista_copia)):
                if lista_copia[indice1] > lista_copia[indice2]:
                    numero_aux = lista_copia[indice2]                    
                    lista_copia[indice2] = lista_copia[indice1]                    
                    lista_copia[indice1] = numero_aux   
    return lista_copia

def burbujeo_con_swap(lista_numeros):
    if not lista_numeros:
        print("La lista esta vacia")
    else:
        lista_copia = lista_numeros.copy() 
        for indice1 in range(len(lista_copia) - 1):
            for indice2 in range(indice1 + 1, len(lista_copia)):
                if lista_copia[indice1] > lista_copia[indice2]:
                    lista_copia[indice1], lista_copia[indice2] = lista_copia[indice2], lista_copia[indice1]   
    return lista_copia

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
            lista_a_ordenar[indice], lista_a_ordenar[indice_del_minimo] = lista_a_ordenar[indice_del_minimo], lista_a_ordenar[indice]
        return lista_a_ordenar 

def quick_sort(lista: list[int]):
    if len(lista) < 2:
        return lista
    else:
        lista_copia = lista.copy()
        pivot = lista_copia.pop()
        mas_grandes = []
        mas_chicos = []
        for numero in lista_copia:
            if(numero > pivot):
                mas_grandes.append(numero)
            else:
                mas_chicos.append(numero)
        return quick_sort(mas_chicos) + [pivot] + quick_sort(mas_grandes) 

if __name__ == "__main__":
    print("\ndemostracion con lista de 10000 elementos:")
    ITERACIONES = 10000
    lista_random_numeros = [
        rd.randint(0, 10000) for _ in range(ITERACIONES)
    ]

    # quick_sort()
    start = time()
    lista = quick_sort(lista_random_numeros)
    end = time()
    tiempo_total = end - start
    print("\nquick_sort():")
    print(f"Tardó {tiempo_total} segundos\n")

    # selection_sort_v1()
    start = time()
    lista = selection_sort_v1(lista_random_numeros)
    end = time()
    tiempo_total = end - start
    print("\nselection_sort_v1():")
    print(f"Tardó {tiempo_total} segundos\n")
 
    # selection_sort_v2()
    start = time()
    lista = selection_sort_v2(lista_random_numeros)
    end = time()
    tiempo_total = end - start
    print("\nselection_sort_v2():")
    print(f"Tardó {tiempo_total} segundos\n")

    # burbujeo_con_swap()
    start = time()
    lista = burbujeo_con_swap(lista_random_numeros)
    end = time()
    tiempo_total = end - start
    print("\nburbujeo_con_swap():")
    print(f"Tardó {tiempo_total} segundos\n")
    
    # burbujeo_sin_swap()
    start = time()
    lista = burbujeo_sin_swap(lista_random_numeros)
    end = time()
    tiempo_total = end - start
    print("\nburbujeo_sin_swap():")
    print(f"Tardó {tiempo_total} segundos\n")