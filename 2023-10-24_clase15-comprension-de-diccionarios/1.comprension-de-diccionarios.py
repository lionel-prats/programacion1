def limpiar_consola():
    import os
    if os.name in ["ce", "nt", "dos"]: # windows
        os.system("cls")
    else: # linux o mac
        os.system("clear")    
def separador():
    print("\n---------------\n")

limpiar_consola()

lista_nombres = ["Maria", "Camila", "Solange", "Juana", "Valeria",
                "Ana", "Juan", "Pedro", "Matias"]


diccionario = {}
for nombre in lista_nombres:
    diccionario[nombre] = len(nombre)
print(diccionario)

separador()

diccionario = {f"{nombre}{i+1}": f"{len(nombre)}" for i, nombre in enumerate(lista_nombres)}
print(diccionario)

separador()

diccionario2 = {f"{nombre}{lista_nombres.index(nombre) + 1}": f"{len(nombre)}" for i, nombre in enumerate(lista_nombres)}
print(diccionario2)

separador()