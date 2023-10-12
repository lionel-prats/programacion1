import os
if os.name in ["ce", "nt", "dos"]: # windows
    os.system("cls")
else: # linux o mac
    os.system("clear")

def sort_list(list: list, asc: bool = True)-> list:
    for i in range(len(list) - 1):
        for j in range(i+1, len(list)):
            if asc:
                if list[j] < list[i]:
                    aux = list[i]
                    list[i] = list[j]
                    list[j] = aux 
            else:
                if list[j] > list[i]:
                    aux = list[i]
                    list[i] = list[j]
                    list[j] = aux 

lista = [5, 1, 8, 6, 12, 49, 1, 0, 7.5, 2, -1]

print(lista, "\n")

sort_list(lista)
print(lista, "\n")

sort_list(lista, False)
print(lista, "\n")