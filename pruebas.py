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

personas = [
  {
    "nombre": "Lionel",
    "apellido": "Prats",
    # "edad": 38,
    "anio_nacimiento": "1985",
    # "altura": "1.83",
    "patente": "A010BO"
  },
  {
    "nombre": "Sergio",
    "apellido": "Balestrini",
    # "edad": 39,
    # "anio_nacimiento": "1984",
    # "altura": "1.85",
    "patente": "AF154HJ"
  },
  {
    "nombre": "Santiago",
    "apellido": "Fiorini",
    # "edad": 40,
    # "anio_nacimiento": "1983",       
    # "altura": "1.90",
    "patente": "PFG264"
  },"sad"
]

string = "AC010BO"

print(string.isdecimal())

