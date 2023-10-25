def limpiar_consola():
    import os
    if os.name in ["ce", "nt", "dos"]: # windows
        os.system("cls")
    else: # linux o mac
        os.system("clear")    
def separador():
    print("\n---------------\n")

limpiar_consola()

lista_personas = [
  {"nombre": "Ignacio", "edad": 38},
  {"nombre": "Sergio", "edad": 39},
  {"nombre": "Alba", "edad": 35},
  {"nombre": "Luis", "edad": 18},
  {"nombre": "Emiliano", "edad": 28},
  {"nombre": "Damian", "edad": 19},
  {"nombre": "Laura", "edad": 33}
]


lista_iniciales_1 = []
for persona in lista_personas:
    for letra in persona.get("nombre"):
        lista_iniciales_1.append(letra)
print(lista_iniciales_1)




nombres = ["lionel", "lupi"]
lista_iniciales_2 = []
for nombre in nombres:
    lista_iniciales_2.extend(list(nombre))
print(lista_iniciales_2)

print(list("presidente"))
print("-".join("hola"))

separador()

lista_iniciales_3 = [letra for nombre in nombres for letra in nombre] 
print(lista_iniciales_3)

separador()