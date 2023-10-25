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

nombres = ["lionel", "fede", "maca"]
nombres2 = list(map(lambda nombre: nombre.lower(), nombres))
nombres2 = [nombre.capitalize() for nombre in nombres]
print(nombres2)

separador()

lista_dobles = [numero for numero in numeros if numero >= 3]
print(lista_dobles)

separador()

rango = range(1, 21, 2) # range es un tipo de dato
lista_uno_diez = [numero for numero in rango]

print(type(rango))
print(rango)
print(lista_uno_diez)

separador()

lista_personas = [
  {
    "nombre": "Lionel", "edad": 38
  },
#   {
#     "edad": 25
#   },
  {
    "nombre": "Sergio", "edad": 39
  },
  {
    "nombre": "Santiago", "edad": 35
  },
  {
    "nombre": "Luis", "edad": 18
  },
  {
    "nombre": "Emiliano", "edad": 28
  }
]

lista_iniciales_1 = []
for persona in lista_personas:
    inicial = persona.get("nombre")[0]
    lista_iniciales_1.append(inicial)
print(lista_iniciales_1)


lista_iniciales_2 = [persona.get("nombre", None)[0] for persona in lista_personas]
print(lista_iniciales_2)

# lista_iniciales_3 = [persona.get("nombre")[0] for persona in lista_personas]
# print(lista_iniciales_3)