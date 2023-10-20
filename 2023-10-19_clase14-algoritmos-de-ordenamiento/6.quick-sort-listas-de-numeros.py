import random as rd
from time import time 

def limpiar_consola():
    import os
    if os.name in ["ce", "nt", "dos"]: # windows
        os.system("cls")
    else: # linux o mac
        os.system("clear")
limpiar_consola()

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

def unir_listas(lista):
    return lista   
    
if __name__ == "__main__":

    lista1 = ["lionel", "luis", "rodri"]
    lista2 = ["tomy", "rafa", "leo"]
    lista3 = ["marian", "alex"]
    print(type(unir_listas(lista1 + lista2 + lista3)))
    print(unir_listas(lista1 + lista2 + lista3))

    print("\nDemostracion con lista de 10 elementos:")
    lista_random_numeros = [5, 0.44, -4, 0, -8, 4, 1, 6, -4, 6]

    print("\nLista original:")
    print(lista_random_numeros)

    start = time()
    lista = quick_sort(lista_random_numeros)
    end = time()
    tiempo_total = end - start
    print("\nCopia ordenada con quick_sort()")
    print(lista)
    print(f"Tardó: {tiempo_total}")

    print("\nLista original:")
    print(lista_random_numeros)

    print("\n----------------------------------------------------------\n")

    print("Registros:")
    print("Cantidad elementos | TIEMPO DE PROCESAMIENTO (segundos) ")
    print("10000  | 0.010201215744018555")
    print("15000  | 0.017278194427490234")
    print("20000  | 0.02420496940612793")
    print("25000  | 0.03060007095336914")
    print("30000  | 0.03647446632385254")
    print("50000  | 0.06639385223388672")
    print("100000 | 0.1494600772857666")
    print("650000 | 0.1494600772857666")
    print("421000 | 1.0415151119232178")

    print("demostracion con lista de 10000 elementos:")
    ITERACIONES = 421000
    lista_random_numeros = [
        rd.randint(0, 10000) for _ in range(ITERACIONES)
    ]
    print(f"\nDemostración con {ITERACIONES} elementos:")
    start = time()
    lista = quick_sort(lista_random_numeros)
    end = time()
    tiempo_total = end - start
    print("\nquick_sort() (10000 elementos):")
    print(f"Tardó {tiempo_total} segundos\n")
    print(lista)