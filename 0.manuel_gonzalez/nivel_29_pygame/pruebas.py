lista_1 = [2,4,6,8]
for numero in lista_1:
    if numero == 4 or numero == 6:
        lista_1.remove(numero)   
print(lista_1)
# --------------------------------------
lista_2 = [2,4,6,8]
for numero in list(lista_2):
    if numero == 4 or numero == 6:
        lista_2.remove(numero)   
print(lista_2)

