""" 
Alumno: Lionel Prats 
DNI: 31367577
División: 1H
Nro. legajo: 115678
Desafío Stark 02
"""

import os

menu =\
{
  "desafio_00": """
DESAFIO STARK 02

1 - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
2 - Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
3 - Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
4 - Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
5 - Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
6 - Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
7 - Calcular e informar cual es el superhéroe más y menos pesado.
  """,
  "desafio_01": """
DESAFIO STARK 01

a - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
b - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
c - Recorrer la lista y determinar cuál es el superhéroe más alto de género M
d - Recorrer la lista y determinar cuál es el superhéroe más alto de género F
e - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M
f - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F
g - Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
h - Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
i - Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
j - Determinar cuántos superhéroes tienen cada tipo de color de ojos.
k - Determinar cuántos superhéroes tienen cada tipo de color de pelo.
l - Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’)
m - Listar todos los superhéroes agrupados por color de ojos.
n - Listar todos los superhéroes agrupados por color de pelo.
o - Listar todos los superhéroes agrupados por tipo de inteligencia
  """
}

texto_default = "Elija una opcion entre 1 y 7 o presione q para salir: "

def stark_normalizar_datos(lista: list[dict]) -> list[dict]:
  """  
  ACCION: recorre una lista de diccionarios y castea a float toda propiedad compatible con ese formato\n
  PARAMETROS:\n 
  [lista] -> lista de diccionarios a formatear\n
  RETURN: la lista recibida con las propiedades factibles de ser casteada a float, casteadas
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
  PARAMETROS:\n 
  [string] -> string a formatear\n
  RETURN: el string recibido casteado a float si el tipo de dato original es compatible, False en caso contrario
  """
  if type(string) == str:
    try:
      return float(string)
    except ValueError:
      return False
  return False

def obtener_nombre(diccionario: dict) -> str:
  """  
  ACCION: obtiene el valor de la propiedad "nombre" de un diccionario y lo retorna en una leyenda (str):\n 
  PARAMETROS:\n
  [diccionario] -> diccionario del cual se obtendra la el valor de la clave "nombre"\n
  RETURN: una leyenda (str)
  """
  return f"Nombre: {diccionario.get('nombre', 'sin datos')}"

def obtener_nombre_y_dato(diccionario: dict, key: str) -> str:
  """  
  ACCION: recibe un diccionario del que obtiene los valores de la propiedad "nombre" y de la propiedad especificada en [key], y con esos datos construye y retorna una leyenda (str):\n 
  PARAMETROS:\n
  [diccionario] -> diccionario del cual se obtendran los datos para construir la leyenda a retornar\n
  [key] -> clave dinamica recibida como parametro\n
  RETURN: "Nombre: xxx | [key]: xxx" (str)
  """
  nombre = diccionario.get('nombre', 'sin datos')
  valor_dinamico = diccionario.get(key, 'sin datos')
  return f"Nombre: {nombre} | {key}: {valor_dinamico}"

def calcular_max(lista: list[dict], clave: str):
  """ 
  ACCION: recibe una lista de diccionarios y una key para la que se buscará el máximo valor presente en la lista, y retorna una nueva lista de diccionarios de todos aquellos diccionarios cuyo valor para esta key coincida con el valor máximo hallado \n 
  PARAMETROS:\n
  [lista] -> lista de diccionarios\n
  [key] -> clave a evaluar\n
  RETURN: retorna un iterable de diccionarios
  """
  stark_normalizar_datos(lista)
  valor_maximo = max(lista, key = lambda diccionario: diccionario[clave])[clave]
  listado_heroes_valor_maximo = filter(lambda elemento: elemento[clave] == valor_maximo, lista)
  return listado_heroes_valor_maximo

def calcular_min(lista: list[dict], clave: str):
  """ 
  ACCION: recibe una lista de diccionarios y una key para la que se buscará el mínimo valor presente en la lista, y retorna una nueva lista de diccionarios de todos aquellos diccionarios cuyo valor para esta key coincida con el valor mínimo hallado \n 
  PARAMETROS:\n
  [lista] -> lista de diccionarios\n
  [key] -> clave a evaluar\n
  RETURN: retorna un iterable de diccionarios
  """
  stark_normalizar_datos(lista)
  valor_minimo = min(lista, key = lambda diccionario: diccionario[clave])[clave]
  listado_heroes_valor_minimo = filter(lambda elemento: elemento[clave] == valor_minimo, lista)
  return listado_heroes_valor_minimo

def calcular_max_min_dato(lista: list[dict], tipo_calculo: str, clave: str):
  """ 
  ACCION: recibe una lista de diccionarios [lista], un string "maximo" o "minimo" [tipo_calculo] y una key a evaluar. Dependiendo de [tipo_calculo] hallará el valor correspondiente para [clave] y retornara un iterable con todos los superheroes cuyo valor para [clave] coincida con el hallado\n
  PARAMETROS:\n
  [lista] -> lista de heroes\n
  [tipo_calculo] -> "maximo" o "minimo"\n
  [clave] -> clave a evaluar\n
  RETURN: retorna un iterable de diccionarios
  """
  if tipo_calculo == "minimo": 
    return calcular_min(lista, clave)
  elif tipo_calculo == "maximo": 
    return calcular_max(lista, clave)
  return -1

def sumar_dato_heroe(lista: list[dict], key: str) -> float:
  """  
  ACCION: calcula la suma de una determinada clave [key] en una lista de diccionarios [lista] (el tipo de dato de la clave a sumar debe ser int o float)\n
  PARAMETROS:\n
  [lista] -> lista de heroes\n
  [key] -> clave a sumar (type str | value int o float)\n
  RETURN: la suma de los valores de la clave especificada 
  \n
  """
  stark_normalizar_datos(lista)
  total = 0
  for diccionario in lista:
    if isinstance(diccionario, dict) and len(diccionario):
      total += diccionario[key]
  return total

def dividir(dividendo: float, divisor: float) -> float:
  """  
  ACCION: calcula el resultado de la division entre dos numeros\n
  PARAMETROS:\n
  [divisor] -> divisor\n
  [dividendo] -> dividendo\n
  RETURN: el resultado de la division 
  """
  if divisor:
    return dividendo / divisor
  return divisor

def calcular_promedio(lista: list[dict], key: str) -> float:
  """  
  ACCION: en una lista de diccionarios [lista] calcula el promedio (valor numerico) de una clave dada [key]\n
  PARAMETROS:\n
  [lista] -> lista de diccionarios\n
  [key] -> clave a considerar para realizar el calculo\n
  RETURN: el resultado del calculo (si la lista no tiene elementos, la funcion retonara 0) 
  """
  dividendo = sumar_dato_heroe(lista, key)
  divisor = len(lista)
  return dividir(dividendo, divisor)

def validar_entero(string) -> bool:
  """  
  ACCION: recibe un string. Verifica si esta conformado unicamente por digitos\n 
  PARAMETROS:\n
  [string] -> str\n
  RETURN: True si esta conformado unicamente por digitos, False en caso contrario 
  """
  return string.isdigit()

def stark_menu_principal() -> int:
  """  
  ACCION: imprime el menu principal y almacena y valida el input ingresado por el usuario\n 
  PARAMETROS: None\n
  RETURN: si el input es un entero, retorna dicho input casteado como int, caso contrario retorna -1
  """
  imprimir_menu()
  opcion_seleccionada = input(texto_default)
  if validar_entero(opcion_seleccionada):
    return int(opcion_seleccionada)
  return -1

def stark_imprimir_nombres_heroes(lista: list[dict]):
  """  
  ACCION: imprime el listado de nombres de los heroes:\n
  PARAMETROS:\n
  [lista] -> lista de heroes\n
  RETURN: si la lista está vacía retornará -1, caso contrario None
  """
  if not len(lista):
    return -1
  imprimir_dato("\n1 - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe\n")
  for i, heroe in enumerate(lista):
    imprimir_dato(f"{i + 1}- {obtener_nombre(heroe)}")
  imprimir_dato("\n")

def stark_imprimir_nombres_alturas(lista: list[dict]):
  """  
  ACCION: imprime el listado de nombres y alturas de los heroes:\n
  PARAMETROS:\n
  [lista] -> lista de heroes\n
  RETURN: si la lista está vacía retornará -1, caso contrario None
  """
  if not len(lista):
    return -1
  imprimir_dato("\n2 - Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo\n")
  for i, heroe in enumerate(lista):
    imprimir_dato(f"{i + 1}- {obtener_nombre_y_dato(heroe, 'altura')}")
  imprimir_dato("\n")

def stark_calcular_imprimir_heroe(lista: list[dict], tipo_calculo: str, clave: str):
  """  
  ACCION: recibe la lista de heroes [lista] e imprime por consola los heroes cuyo valor de clave [clave] coincida con el maximo o minimo [tipo_calculo] hallado para esa clave en toda la lista\n
  PARAMETROS:\n
  [lista] -> lista de heroes\n
  [tipo_calculo] -> "maximo" o "minimo"\n
  [clave] -> clave a evaluar\n
  RETURN: si len([]) == 0, retorna -1, caso contrario None  
  """
  if not len(lista):
    return -1
  heroes_valor_buscado = calcular_max_min_dato(lista, tipo_calculo, clave)
  if tipo_calculo == "minimo":
    inicio = "Menor"
  else:
    inicio = "Mayor"
  for heroe in heroes_valor_buscado:
    imprimir_dato(f"{inicio} {clave}: {obtener_nombre_y_dato(heroe, clave)}")
  imprimir_dato("\n")

def stark_calcular_imprimir_promedio_altura(lista: list[dict]):
  """  
  ACCION: recibe la lista de heroes [lista] e imprime por consola la altura promedio del total de los mismos\n
  PARAMETROS:\n
  [lista] -> lista de heroes\n
  RETURN: si la lista de heroes esta vacia retorna -1, caso contrario None  
  """
  if not len(lista):
    return -1
  imprimir_dato("\n5 - Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)\n")
  imprimir_dato(f"Altura promedio: {calcular_promedio(lista, 'altura')}")
  imprimir_dato("\n")

def imprimir_menu():
  """ 
  ACCION: imprime el menu de opciones en consola\n
  PARAMETROS: None\n
  RETURN: None
  """
  limpiar_consola()
  imprimir_dato(menu["desafio_00"])
  
def imprimir_dato(string: str):
  """  
  ACCION: recibe un string y lo imprime por consola\n 
  PARAMETROS:\n
  [string] -> string a imprimir\n
  RETURN: None
  """
  print(string)

def continuar(input_usuario: str) -> bool:
  """ 
  ACCION: valida si el usuario desea realizar una nueva consulta o finalizar la ejecuciond el programa\n
  PARAMETROS: None\n
  [input_usuario] -> opcion ingresada por el usuario: con "q" o "Q" finaliza la ejecucion; entre "1" y "7" las opciones validas para acceder a la informacion proporcionada por la aplicacion; cualquier otro input ingresado, el programa le pedira nuevamente que ingrese una opcion 
  RETURN: True si ingreso entre "1" y "7", False si ingreso "q" o "Q"
  """
  while input_usuario != "1" and input_usuario != "2" and input_usuario != "3" and input_usuario != "4" and input_usuario != "5" and input_usuario != "6" and input_usuario != "7" and input_usuario != "q":
    imprimir_menu()
    input_usuario = input(texto_default).lower()
  if input_usuario == "q":
    limpiar_consola()
    return False
  return input_usuario

def limpiar_consola():
    """ 
    ACCION: limpia la consola\n
    PARAMETROS: None\n
    RETURN: None
    """
    if os.name in ["ce", "nt", "dos"]: # windows
      os.system("cls")
    else: # linux o mac
      os.system("clear")

if __name__ == "__main__":
  limpiar_consola()
  print(stark_menu_principal())

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/ENTREGAS/stark/02
# python stark_biblioteca.py