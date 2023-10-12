import os
if os.name in ["ce", "nt", "dos"]: # windows
    os.system("cls")
else: # linux o mac
    os.system("clear")

lista = [5, 1, 6, 12, 1, 0, 2]

print(lista)

# pos 0 de la lista
for i in range(1, len(lista)):
    if lista[i] < lista[0]:
        aux = lista[0]
        lista[0] = lista[i]
        lista[i] = aux

# pos 1 de la lista
for i in range(2, len(lista)):
    if lista[i] < lista[1]:
        aux = lista[1]
        lista[1] = lista[i]
        lista[i] = aux

# pos 2 de la lista
for i in range(3, len(lista)):
    if lista[i] < lista[2]:
        aux = lista[2]
        lista[2] = lista[i]
        lista[i] = aux

# pos 3 de la lista
for i in range(4, len(lista)):
    if lista[i] < lista[3]:
        aux = lista[3]
        lista[3] = lista[i]
        lista[i] = aux

# pos 4 de la lista
for i in range(5, len(lista)):
    if lista[i] < lista[4]:
        aux = lista[4]
        lista[4] = lista[i]
        lista[i] = aux

# pos 5 de la lista
for i in range(6, len(lista)):
    if lista[i] < lista[5]:
        aux = lista[5]
        lista[5] = lista[i]
        lista[i] = aux

print(lista)