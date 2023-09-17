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
necesito que valores existen para la propiedad "cuadro"
cual es la forma mas eficiente y profesional de hacerlo?
"""

listado_personas = [
    {
      "nombre": "ale",
      "cuadro": "estudiantes"
    },
    {
      "nombre": "bata",
      "cuadro": "independiente"
    },
    {
      "nombre": "cabe",
      "cuadro": "boca"
    },
    {
      "nombre": "checho",
      "cuadro": "racing"
    },
    {
      "nombre": "emi",
      "cuadro": "boca"
    },
    {
      "nombre": "fara",
      "cuadro": "independiente"
    },
    {
      "nombre": "juan",
      "nombre": "cabe",
      "cuadro": "boca"
    },
    {
      "nombre": "lionel",
      "cuadro": "all boys"
    },
    {
      "nombre": "maro",
      "cuadro": "boca"
    },
    {
      "nombre": "negro",
      "cuadro": "river"
    }
]

cuadro_objetivo = "boca"

# Usar filter con una función lambda para filtrar los diccionarios
personas_con_cuadro_objetivo = list(filter(lambda persona: persona["cuadro"] == cuadro_objetivo, listado_personas))

# Imprimir la lista de personas con el cuadro "independiente"
for i, persona in enumerate(personas_con_cuadro_objetivo):
    print(f"{i+1}: {persona['nombre']} - Cuadro: {persona['cuadro']}")


