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
    print("\nAlgoritmo Quick Sort vs. Algoritmo Selection(version 1):\n")

    print("Registros:")
    print("Cantidad elementos | QUICK SORT | SELECTION")
    print("10000 | 0.010201215744018555 | 1.7102885246276855")
    print("15000 | 0.017278194427490234 | 3.8783414363861084")
    print("20000 | 0.02420496940612793  | 6.73885703086853")
    print("25000 | 0.03060007095336914  | 10.732481479644775")
    print("30000 | 0.03647446632385254  | 15.764815092086792")

    ITERACIONES = 30000
    
    lista_random_numeros = [
        rd.randint(0, 10000) for _ in range(ITERACIONES)
    ]

    print(f"\nDemostración con {ITERACIONES} elementos:")
    
    # quick_sort()
    start = time()
    lista = quick_sort(lista_random_numeros)
    end = time()
    tiempo_total = end - start
    print("\nquick_sort() (10000 elementos):")
    print(f"Tardó {tiempo_total} segundos\n")

    # selection_sort_v1()
    start = time()
    lista = selection_sort_v1(lista_random_numeros)
    end = time()
    tiempo_total = end - start
    print("\nselection_sort_v1() (10000 elementos):")
    print(f"Tardó {tiempo_total} segundos\n")

   
