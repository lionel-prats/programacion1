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
  }
]

def stark_normalizar_datos(lista: list[dict]) -> list[dict]:
  """  
  ACCION: recorre una lista de diccionarios y castea a float toda propiedad compatible con ese formato\n
  PARAMETROS:\n 
  [lista] -> lista de diccionarios a formatear\n
  RETURN: una lista de diccionarios igual a la recibida, en la que cada propiedad factible de ser casteada a float será de ese tipo de dato
  """
  if not len(lista):
    return "Error: Lista de héroes vacía"
  respuesta = None
  for diccionario in lista:
    for k, v in diccionario.items():
      if type(v) == str:
        resultado_casteo = convertir_string_en_float(v)
        if resultado_casteo:
          diccionario[k] = resultado_casteo
          if not respuesta:
            respuesta = "Datos normalizados"
        else:
          diccionario[k] = v
      else:
        diccionario[k] = v
  return respuesta

def convertir_string_en_float(string):
  """ 
  ACCION: recibe una string, y de ser compatible es casteado a float:\n 
  [string] -> string a formatear\n
  RETURN: el string recibido casteado a float si el tipo de dato original es compatible, False en caso contrario
  """
  if type(string) == str:
    try:
      return float(string)
    except ValueError:
      return False
  return False
  

print(personas, "\n")

print(stark_normalizar_datos(personas), "\n")

print(personas)

# print(convertir_string_en_float([1]))
