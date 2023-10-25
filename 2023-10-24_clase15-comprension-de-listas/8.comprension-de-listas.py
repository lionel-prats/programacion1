def limpiar_consola():
    import os
    if os.name in ["ce", "nt", "dos"]: # windows
        os.system("cls")
    else: # linux o mac
        os.system("clear")    
def separador():
    print("\n---------------\n")

limpiar_consola()

lista_nombres = [["Maria", "Camila", "Solange", "Ana"], ["Juan", "Pedro", "Matias"]]

lista_letras = []
for lista in lista_nombres:
    for nombre in lista:
        for letra in nombre:
            lista_letras.append(letra)    
print(lista_letras)


lista_nombres_2 = ["Maria", "Camila", "Solange", "Ana"]
lista_letras_2 = [letra for nombre in lista_nombres_2 for letra in nombre] 
print(lista_letras_2)


lista_letras_3 = [letra for lista in lista_nombres for nombre in lista for letra in  nombre] 
print(lista_letras_3)

lista_letras_4 = [nombre for lista in lista_nombres for nombre in lista for letra in  nombre if nombre[0].lower() == "m"]
print(lista_letras_4)

separador()


print(set([1,1,1,2,2,2,3,4,4,4,2]))