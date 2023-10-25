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


diccionario = {nombre: len(nombre) for nombre in lista_nombres}
print(diccionario)


