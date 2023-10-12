import os
if os.name in ["ce", "nt", "dos"]: # windows
    os.system("cls")
else: # linux o mac
    os.system("clear")

lista = [5, 1, 6, 12, 1, 0, 7.5, 2, -1]

print(lista)

for i in range(len(lista) - 1):
    for j in range(i+1, len(lista)):
        if lista[j] < lista[i]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

print(lista)