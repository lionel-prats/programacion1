lista = ["emmet", "marty", "biff"]
swap = True
while(swap):
    swap = False
    for i in range(len(lista)-1):
        if(lista[i] > lista[i+1]):
            swap = True
            lista[i], lista[i+1] = lista[i+1], lista[i]

print(lista)


# dict1 = {"nombre": "juan", "edad": 15}
# dict2 = dict(dict1)
# dict2 = dict1.copy()

# print(dict1 == dict2)

# print(dict1["sadsad"])

# for i in diccion2:
#     print(i)


string = "mono"

print(string.index("n"))

def sumar(a, b):
    resultado = a + b

print(sumar(10,20))

