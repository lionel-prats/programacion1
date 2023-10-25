def limpiar_consola():
    import os
    if os.name in ["ce", "nt", "dos"]: # windows
        os.system("cls")
    else: # linux o mac
        os.system("clear")    
def separador():
    print("\n---------------\n")

limpiar_consola()

def mayor_a_cero(numero):
    return numero > 0 and numero < 10

def doble(lista_numeros):
    return [numero * 2 for numero in lista_numeros if mayor_a_cero(numero)]

funcion_rango = range(10) 
lista_unos_1 = []
for _ in funcion_rango:
    lista_unos_1.append(1)

print(lista_unos_1)

lista_unos_2 = [1 for _ in range(10)]
print(lista_unos_2)