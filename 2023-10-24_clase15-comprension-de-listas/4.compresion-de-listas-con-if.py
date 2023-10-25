def limpiar_consola():
    import os
    if os.name in ["ce", "nt", "dos"]: # windows
        os.system("cls")
    else: # linux o mac
        os.system("clear")    
def separador():
    print("\n---------------\n")

limpiar_consola()

nombres = ["lionel", "fede", "maca"]

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

def mayor_a_cero(numero):
    return numero > 0 and numero < 10

def doble(lista_numeros):
    return [numero * 2 for numero in lista_numeros if mayor_a_cero(numero)]

lista_numeros = [1, -2, 10, -5, 4, 5] 
numeros_dobles_2 = doble(lista_numeros)
print(numeros_dobles_2)
print(lista_numeros)

separador()

# de esta manera es obligatorio que tenga un else la condicion
print(list(map(lambda num: num -100 if num > 4 else num + 100, [1,2,3,4,5,6,7,8])))

#con comprension no hace falta que lo tenga
print([num * 2 for num in [1,2,3,4,5,6,7,8] if num > 4])