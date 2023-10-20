import random as rd
from time import time 

def limpiar_consola():
    import os
    if os.name in ["ce", "nt", "dos"]: # windows
        os.system("cls")
    else: # linux o mac
        os.system("clear")
limpiar_consola()

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

if __name__ == "__main__":
    print("\nDemostracion con lista de 10 elementos:")
    lista_random_numeros = [5, 0.44, -4, 0, -8, 4, 1, 6, -4, 6]

    print("\nLista original:")
    print(lista_random_numeros)

    start = time()
    lista = burbujeo_con_swap(lista_random_numeros)
    end = time()
    tiempo_total = end - start
    print("\nCopia ordenada con burbujeo_con_swap()")
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
    lista = burbujeo_con_swap(lista_random_numeros)
    end = time()
    tiempo_total = end - start
    print("\nCopia ordenada con burbujeo_con_swap():")
    print(f"Tardó: {tiempo_total} segundos\n")
