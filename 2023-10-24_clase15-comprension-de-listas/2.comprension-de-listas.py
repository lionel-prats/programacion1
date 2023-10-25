def limpiar_consola():
    import os
    if os.name in ["ce", "nt", "dos"]: # windows
        os.system("cls")
    else: # linux o mac
        os.system("clear")    
def separador():
    print("\n---------------\n")

limpiar_consola()

numeros = [1, 2, 3, 4, 5] 
print(numeros)

separador()

lista_dobles_2 = list(map(lambda numero: numero * 2, numeros))
print(lista_dobles_2)

separador()

def multiplicar_por_dos(numero):
    return numero * 2
lista_dobles_3 = list(map(multiplicar_por_dos, numeros))
print(lista_dobles_3)

separador()

numeros = [1, 2, 3, 4, 5] 
comprension_lista_dobles = [numero * 2 for numero in numeros]
comprension_tupla_dobles = (numero * 2 for numero in numeros)
comprension_lista_filtro = [numero if numero >= 3 else None for numero in numeros]

comprension_lista_filtro = [numero >= 3 for numero in numeros]
comprension_lista_filtro = list(filter(lambda numero: numero >= 3, numeros))

print(comprension_lista_dobles)
print(comprension_tupla_dobles)
print(comprension_lista_filtro)

separador()