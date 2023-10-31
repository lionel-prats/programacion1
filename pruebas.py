# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1
# python pruebas.py

import os
if os.name in ["ce", "nt", "dos"]: # windows
    os.system("cls")
else: # linux o mac
    os.system("clear")

"""
estoy trabajando en python
tengo que esta lista de diccionarios
necesito optimizar la funcion obtener_lista_de_tipos() 
cual es la forma mas eficiente y profesional de hacerlo?
"""

personas = [
  {
    "nombre": "Lionel",
    "apellido": "Prats",
    "edad": 38,
    "anio_nacimiento": "1985",
    "altura": "1.83",
    #"patente": "A010BO"
    "equipo": "River"
  },
  {
    "nombre": "Sergio",
    "apellido": "Balestrini",
    "edad": 39,
    "anio_nacimiento": "1984",
    "altura": "1.85",
    "patente": "ZYX987",
    "equipo": "Racing"
  },
  {
    "nombre": "Santiago",
    "apellido": "Fiorini",
    "edad": 40,
    "anio_nacimiento": "1983",       
    "altura": "1.90",
    "patente": "",
    "equipo": "Boca"
  },
  {
    "nombre": "Luis",
    "apellido": "Fiorini",
    "edad": 40,
    "anio_nacimiento": "1983",       
    "altura": "1.90",
    "patente": "ABC123",
    "equipo": "Velez"

  },
  {
    "nombre": "Emiliano",
    "apellido": "Fernandez",
    "edad": 40,
    "anio_nacimiento": "1983",       
    "altura": "1.90",
    "patente": "ABC123",
    "equipo": ""

  },
  {
    "nombre": "Gabriel",
    "apellido": "Villalobos",
    "edad": 40,
    "anio_nacimiento": "1983",       
    "altura": "1.90",
    "patente": "ABC123",
    "equipo": "Independiente"

  },
  {
    "nombre": "Gastón",
    "apellido": "Gambetta",
    "edad": 40,
    "anio_nacimiento": "1983",       
    "altura": "1.90",
    "patente": "ABC123",
    "equipo": "River"

  },
  {
    "nombre": "Mariano",
    "apellido": "Tolosa",
    "edad": 40,
    "anio_nacimiento": "1983",       
    "altura": "1.90",
    "patente": "ABC123",
    "equipo": "Boca"

  },
  {
    "nombre": "Juan",
    "apellido": "Peverelli",
    "edad": 40,
    "anio_nacimiento": "1983",       
    "altura": "1.90",
    "patente": "ABC123",
    "equipo": "Boca"

  },
  {
    "nombre": "Batata",
    "apellido": "Zinser",
    "edad": 40,
    "anio_nacimiento": "1983",       
    "altura": "1.90",
    "patente": "ABC123",
    "equipo": "Independiente"

  },
  {
    "nombre": "Emiliano",
    "apellido": "Romero",
    "edad": 40,
    "anio_nacimiento": "1983",       
    "altura": "1.90",
    "patente": "ABC123"

  }
]

""" def obtener_lista_de_tipos(lista_heroes: list[dict], clave: str) -> None:
    diccionario = {}
    for heroe in lista_heroes:
      if not clave in heroe or not heroe[clave]:
          if not "sin datos" in diccionario:
            diccionario["sin datos"] = []
            diccionario["sin datos"].append(heroe["apellido"]) 
          else:
            diccionario["sin datos"].append(heroe["apellido"]) 
      elif not heroe[clave] in diccionario:
          diccionario[heroe[clave]] = []
          diccionario[heroe[clave]].append(heroe["apellido"]) 
      else:
          diccionario[heroe[clave]].append(heroe["apellido"]) 
    return diccionario

resultado = obtener_lista_de_tipos(personas, "equipo")

print(resultado) """

from collections import defaultdict

def obtener_lista_de_tipos(lista_personas: list[dict], clave: str) -> dict:
    diccionario = defaultdict(list)
    for persona in lista_personas:
      valor_clave = persona.get(clave, "sin datos")
      valor_clave = "sin datos" if not valor_clave else valor_clave
      apellido = persona["apellido"]
      diccionario[valor_clave].append(apellido)
    return dict(diccionario)

resultado = obtener_lista_de_tipos(personas, "equipo")
# print(resultado)

""" 
{
  "Celestes": [“Capitan America”, “Tony Stark”],
  "Verde": [“Hulk”, “Viuda Negra”]
}

"""





"""
estoy trabajando con python
tengo las listas:
claves = ["nombre", "apellido", "edad"]
valores = ["lionel", "prats", "38"]
necesito armar el diccionario:
diccionario = {
  "nombre": "lionel", 
  "apellido": "prats", 
  "edad": "38"
}
cual es la forma mas eficiente y profesional de hacerlo?
"""

claves = ["nombre", "apellido", "edad"]
valores = ["lionel", "prats", "38"]

# objeto = zip(claves, valores)
# print(type(objeto), objeto)
# for item in objeto:
#     print(type(item), item)

# lista = list(zip(claves, valores))
# print(type(lista), lista)
# for item in lista:
#   print(type(item), item)

diccionario = dict(zip(claves, valores))
print(type(diccionario), diccionario)
for k, v in diccionario.items():
  print(k, v)




