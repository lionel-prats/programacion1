""" 
Alumno: Lionel Prats 
DNI: 31367577
División: 1H
Nro. legajo: 115678
Desafío Stark 01
"""

import os

menu =\
{
  "desafio_00": """
DESAFIO STARK 00

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
l - Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con "No Tiene")
m - Listar todos los superhéroes agrupados por color de ojos.
n - Listar todos los superhéroes agrupados por color de pelo.
o - Listar todos los superhéroes agrupados por tipo de inteligencia
  """
}

lista_inputs_validos = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "q"]
texto_default = "Elija una opcion entre \"a\" y \"o\", o presione \"q\" para salir: "

def reducir_diccionarios_en_lista(lista: list[dict], campos: list[str]) -> list[dict]:
    """  
    genera una nueva lista de diccionarios a partir de una recibida, prsisitiendo en los diccionarios las claves especificadas por el usuario\n
    recibe una lista de diccionarios y la lista de claves que deben persistir\n
    retorna una lista de diccionarios reducidos respecto a los de la lista original
    """
    nueva_lista = [{campo: diccionario[campo] for campo in campos} for diccionario in lista]
    return nueva_lista

def imprimir_lista_de_diccionarios(lista: list[dict], titulo = None):
  """  
  imprime por consola un titulo (opcional) y un listado de diccionarios\n
  recibe un titulo (str - opcional) y una lista de diccionarios
  no retorna nada
  """
  if titulo:
    print(f"\n{titulo}\n")
  listado = ""
  nro_orden = 1
  for diccionario in lista: 
    listado += f"{nro_orden}- "
    for k, v in diccionario.items():
      listado += f"{k}: {v} | "
    listado = listado[:-3]
    listado += "\n"
    nro_orden += 1
  print(listado)

def imprimir_diccionario_formato_tabla(diccionario: dict, encabezado: str, titulo = None):
  """  
  ACCION: imprime por consola un titulo (opcional) [titulo] y un diccionarios [diccionario]\n
  PARAMETROS: el diccionario a imprimir [diccionario] y un titulo [titulo] opcional
  RETURN: None
  """
  if titulo:
    print(f"\n{titulo}")
  print("\n")
  listado = f"{encabezado}\n"
  for k, v in diccionario.items():
    listado += f"{k} | {v}\n"
  print(listado)    

def imprimir_lista_diccionarios_agrupando_segun_clave(titulo: str, subtitulo: str, lista: list[dict], clave_agrupamiento, claves_a_imprimir: list):
  """  
  ACCION: lista por consola la lista de diccionarios recibida, agrupando segun una clave determinada\n
  PARAMETROS:\n
  [titulo] = titulo que se mostrara por pantalla\n
  [subtitulo] = subtitulo para cada grupo de diccionarios\n
  [lista] = lista e diccionarios que se procesara\n
  [clave_agrupamiento] = clave por la cual se agruparan los diccionarios\n
  [claves_a_imprimir] = lista con las claves (y valores) que se quiere imprimir de cada diccionario\n
  RETURN: None
  """
  print(f"\n{titulo}\n")
  tipos_de_clave = listado_de_valores_existentes_segun_clave(lista, clave_agrupamiento)
  for tipo_de_clave in tipos_de_clave:
    pass     
    print(f"{subtitulo} \"{tipo_de_clave}\":")
    imprimir_lista_de_diccionarios( reducir_diccionarios_en_lista( filtrar_por_clave(lista, clave_agrupamiento, tipo_de_clave), claves_a_imprimir ) )

def valor_maximo_propiedad_en_lista_de_diccionarios(lista: list[dict], clave: str) -> float:
  """ 
  retorna el maximo valor en relacion a una clave especifica, de una lista de diccionarios\n
  recibe una lista de diccionarios y la clave a relevar (el tipo de dato debe ser int o float)
  """
  resultado = max(lista, key = lambda diccionario: diccionario[clave])[clave]
  return resultado

def valor_minimo_propiedad_en_lista_de_diccionarios(lista: list[dict], clave: str) -> float:
  """ 
  retorna el minimo valor en relacion a una clave especifica, de una lista de diccionarios\n
  recibe una lista de diccionarios y la clave a relevar (el tipo de dato debe ser int o float)
  """
  resultado = min(lista, key = lambda diccionario: diccionario[clave])[clave]
  return resultado

def formatear_valores_diccionario_a_numericos(lista: list[dict], claves: list[str], tipo_casteo: str) -> list[dict]:
  """  
  castea como int o float valores de una lista de diccionarios que sean compatibles con estos formatos\n
  recibe la lista de diccionarios a formatear, las claves a castear en los diccionarios y el tipo de casteo que se busca
  """
  for diccionario in lista:
      for clave in claves:
          if(tipo_casteo == "int"):
            diccionario[clave] = int(diccionario[clave])
          elif(tipo_casteo == "float"):
            diccionario[clave] = float(diccionario[clave])
  return lista

def filtrar_por_clave(lista_diccionarios: list[dict], clave: str, valor_buscado) -> list[dict]:
  """
  ACCION: genera una lista de diccionarios a partir de una lista original [lista_diccionarios], persistiendo los diccionarios cuya clave "n" [clave] coincida con un valor dado [valor_buscado]\n
  PARAMETROS: lista de diccionarios [lista_diccionarios], clave a evaluar [clave], valor a evaluar [valor_buscado]
  """
  return [diccionario for diccionario in lista_diccionarios if diccionario[clave] == valor_buscado]

def obtener_total(lista: list[dict], k: str) -> float:
  """  
  calcula la suma de una determinada clave en una lista de diccionarios (el tipo de dato de la clave a sumar debe ser int o float)\n
  recibe una lista de diccionarios y la clave a contabilizar (el tipo de dato debe ser int o float)\n
  retorna la suma de los valores de la clave especificada 
  """
  total = sum(item[k] for item in lista)
  return total

def obtener_promedio(lista_diccionarios: list[dict], clave: str) -> float: 
  """  
  calcula el promedio de una determinada clave en una lista de diccionarios (el tipo de dato de la clave a considerar debe ser int o float)\n
  recibe una lista de diccionarios y la clave a considerar (el tipo de dato debe ser int o float)\n
  retorna el promedio de los valores de la clave especificada en relacion a la cantidad de diccionarios en la lista recibida 
  """
  promedio = round(obtener_total(lista_diccionarios, clave) / len(lista_diccionarios), 2) 
  return promedio

def mostrar_menu():
  limpiar_consola()
  print(menu["desafio_01"])
  
def continuar(input_usuario: str) -> bool:
  """  
  accion: valida si el usuario desea realizar una nueva consulta\n
  parametros: input del usuario [input_usuario]\n
  retorna: True si el input es valido o False si es "q"
  """
  while input_usuario == "Q" or not existe_elemento_en_lista(input_usuario, lista_inputs_validos):
    print(input_usuario)
    mostrar_menu()
    input_usuario = input(texto_default)
  if input_usuario == "q":
    limpiar_consola()
    return False
  return input_usuario

def existe_elemento_en_lista(elemento, lista: list):
  """  
  accion: valida si existe un elemento en una lista de un solo nivel de objetos\n
  parametros: elemento a buscar [elemento] y lista en la que buscar [lista]\n
  retorna: True si el elemento existe en la lista, False en caso contrario
  """
  elemento = elemento.lower() 
  return elemento in lista

def listado_de_valores_existentes_segun_clave(lista: list[dict], clave: str):
  """  
  ACCION: en una lista de diccionarios [lista] identifica los valores existentes para una determinada clave [clave]\n
  PARAMETROS: lista de diccionarios [lista] y clave a analizar [clave]\n
  RETURN: un iterable con los valores encontrados
  """
  iterable = set()
  for diccionario in lista:
      iterable.add(diccionario[clave])
  return iterable

def cantidad_valores_segun_clave(lista: list[dict], clave, mensaje_error = None) ->dict:
  """  
  ACCION: dada una lista de diccionarios [lista] y una clave a analizar [clave], retornara un nuevo diccionario con los valores existentes de dicha clave en la lista de diccionarios (informando si en algun caso no existe o es None mediante el parametro opcional [mensaje_error]) y la cantidad de repeticiones de cada uno\n
  PARAMETROS: lista de diccionarios [lista], clave a analizar [clave] y opcionalmente el mensaje de error [mensaje_error]\n
  RETURN: diccionario con los resultados
  """
  diccionario_resultante = {}
  for diccionario in lista:
      nueva_clave = diccionario.get(clave, mensaje_error) 
      if not nueva_clave:
        nueva_clave = mensaje_error
      diccionario_resultante[nueva_clave] = diccionario_resultante.get(nueva_clave, 0) + 1
  return diccionario_resultante


# --------------------------------- BLOQUE DE FUNCIONES 02 ---------------------------------------
def obtener_nombre(diccionario: dict) -> str:
  """  
  obtiene el valor de la propiedad "nombre" de un diccionario y lo retorna en una leyenda (str):\n 
  PARAMETROS:\n
  [diccionario : dict] -> diccionario del cual se obtendra la el valor de la clave "nombre"\n
  return str
  """
  return f"Nombre: {diccionario.get('nombre', 'sin datos')}"

def imprimir_dato(string: str):
  """  
  recibe un string y lo imprime por consola\n 
  [string : str] -> string a imprimir\n
  return None
  """
  print(string)

# --------------------------------- BLOQUE DE FUNCIONES 02 ---------------------------------------

# --------------------------------- BLOQUE DE FUNCIONES 03 ---------------------------------------

# 1.1
def es_genero(diccionario:dict, str_genero:str) -> bool:
  """  
  determina si el genero de un personaje recibido por parametro coincide con el genero recibido por parametro\n 
  [diccionario : dict] -> diccionario con la info de un heroe, incluida la clave "genero"\n
  [str_genero : str] -> string para realizar la verificacion ("F", "M" o "NB")\n
  return bool -> True si hay coincidencia, False caso contrario
  """
  if diccionario["genero"].upper() == str_genero.upper():
    return True
  return False

# 1.2
def stark_imprimir_heroe_genero(lista_heroes: list[dict], str_genero: str) -> None:
  """  
  imprime los nombres de los heroes cuyo genero coincida con el recibido por parametro\n 
  [lista_heroes : list[dict]] -> lista de heroes\n
  [str_genero : str] -> string para realizar la verificacion ("F", "M" o "NB")\n
  return None
  """
  heroes_genero = filter(lambda heroe: es_genero(heroe, str_genero), lista_heroes)
  print("\n")
  for heroe in heroes_genero:
    imprimir_dato(obtener_nombre(heroe))
  print("\n")

# 2.1
def calcular_min_genero(lista_heroes: list[dict], clave: str, str_genero: str)->float:
  """  
  analiza la lista de heroes del genero especificado por parametro y retorna el valor minimo del campo numerico especificado (altura, fuerza o peso)\n 
  [lista_heroes : list[dict]] -> listado de heroes\n
  [clave] -> clave a analizar\n
  [str_genero] -> genero a analizar\n
  return -> (float) valor minimo hallado 
  """
  heroes_genero = filter(lambda heroe: es_genero(heroe, str_genero), lista_heroes)
  valor_minimo_hallado = min(heroes_genero, key = lambda heroe: castear_dato_a_float(heroe[clave]))[clave]
  return valor_minimo_hallado

# 2.2
def calcular_max_genero(lista_heroes: list[dict], clave: str, str_genero: str)->float:
  """  
  analiza la lista de heroes del genero especificado por parametro y retorna el valor maximo del campo numerico especificado (altura, fuerza o peso)\n 
  [lista_heroes : list[dict]] -> listado de heroes\n
  [clave] -> clave a analizar\n
  [str_genero] -> genero a analizar\n
  return -> (float) valor maximo hallado 
  """
  heroes_genero = filter(lambda heroe: es_genero(heroe, str_genero), lista_heroes)
  valor_maximo_hallado = max(heroes_genero, key = lambda heroe: castear_dato_a_float(heroe[clave]))[clave]
  return valor_maximo_hallado

# 2.3
def calcular_max_min_dato_genero(lista_heroes: list[dict], valor_buscado: str, clave: str, str_genero: str)->float:
  """  
  dadas la lista de heroes, un string "minimo" o "maximo", una clave a analizar y un genero, retorna el listado de superheroes que coincidan con dichos criterios\n 
  [lista_heroes : list[dict]] -> listado de heroes\n
  [valor_buscado : str] -> "minimo"|"maximo", criterio de seleccion\n
  [clave : str] -> clave a analizar\n
  [str_genero : str] -> genero a analizar\n
  return -> (list) listado resultante 
  """
  if(valor_buscado.lower() == "minimo"):
    valor_hallado = calcular_min_genero(lista_heroes, clave, str_genero)
  elif(valor_buscado.lower() == "maximo"):
    valor_hallado = calcular_max_genero(lista_heroes, clave, str_genero)
  
  heroes_genero = filter(lambda heroe: es_genero(heroe, str_genero), lista_heroes)
  lista_final = list(filter(lambda heroe: heroe[clave] == valor_hallado, heroes_genero))
  return lista_final

# 2.4
def stark_calcular_imprimir_heroe_genero(lista_heroes: list[dict], valor_buscado: str, clave: str, str_genero: str)->float:
  """  
  dadas la lista de heroes, un string "minimo" o "maximo", una clave a analizar y un genero, imprime el listado de superheroes que coincidan con dichos criterios\n 
  [lista_heroes : list[dict]] -> listado de heroes\n
  [valor_buscado : str] -> "minimo"|"maximo", criterio de seleccion\n
  [clave : str] -> clave a analizar\n
  [str_genero : str] -> genero a analizar\n
  return None 
  """
  if not lista_heroes:
    return -1
  print("\n")
  lista_final = calcular_max_min_dato_genero(lista_heroes, valor_buscado, clave, str_genero)
  for heroe in lista_final:
    print(heroe["nombre"], " | ", heroe[clave])
  print("\n")

# extra
def castear_dato_a_float(dato):
  """  
  recibe un dato y si es posible lo retorna casteado a float\n 
  [dato] -> dato a intentar castear a float\n
  return -> (float) dato casteado a float (si es posible), (bool) False si no se puede castear 
  """
  if type(dato) == int or type(dato) == str and dato.replace(".", "", 1).isdigit():
    return float(dato)
  elif type(dato) == float:
    return dato
  return False

# --------------------------------- BLOQUE DE FUNCIONES 03 ---------------------------------------

def limpiar_consola():
    """  
    limpia la consola
    """
    # os.system('cls' if os.name == 'nt' else 'clear')
    if os.name in ["ce", "nt", "dos"]: # windows
      os.system("cls")
    else: # linux o mac
      os.system("clear")

if __name__ == "__main__":
  limpiar_consola()
  from datos_stark import lista_personajes
  resultado = calcular_max_min_dato_genero(lista_personajes, "mInImO", "peso", "M")

  for heroe in resultado:
    print(heroe["nombre"], " | ", heroe["peso"])

  stark_calcular_imprimir_heroe_genero(lista_personajes, "MAXimo", "peso", "M")
  print(stark_calcular_imprimir_heroe_genero([], "MAXimo", "peso", "M"))
  
  


# cd Desktop/utn/cuatrimestre1/programacion_1/ENTREGAS/stark/03
# python biblioteca_stark_03.py
# python main.py