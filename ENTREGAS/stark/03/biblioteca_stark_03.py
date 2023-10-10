""" 
Alumno: Lionel Prats 
DNI: 31367577
División: 1H
Nro. legajo: 115678
Desafío Stark 03
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

def obtener_nombre(diccionario: dict) -> str:
  """  
  obtiene el valor de la propiedad "nombre" de un diccionario y lo retorna en una leyenda (str):\n 
  PARAMETROS:\n
  [diccionario : dict] -> diccionario del cual se obtendra la el valor de la clave "nombre"\n
  return str
  """
  return f"Nombre: {diccionario.get('nombre', 'sin datos')}"

def obtener_nombre_y_dato(diccionario: dict, key: str) -> str:
  """  
  de un diccionario dado, retorna una leyenda (str) con los valores de las claves "nombre" y la especificada por parametro\n 
  [diccionario: dict] datos de un superheroe en formato dict\n
  [key: str] clave que se busca retornar junto a "nombre"\n
  return str "Nombre: xxx | [key]: xxx"
  """
  nombre = diccionario.get('nombre', 'sin datos')
  valor_dinamico = diccionario.get(key, 'sin datos')
  return f"Nombre: {nombre} | {key}: {valor_dinamico}"

def imprimir_dato(string: str):
  """  
  recibe un string y lo imprime por consola\n 
  [string : str] -> string a imprimir\n
  return None
  """
  print(string)

def limpiar_consola():
    """  
    limpia la consola
    """
    # os.system('cls' if os.name == 'nt' else 'clear')
    if os.name in ["ce", "nt", "dos"]: # windows
      os.system("cls")
    else: # linux o mac
      os.system("clear")

# --------------------------------- BLOQUE DE FUNCIONES 03 - INICIO ---------------------------------------

# 1.1
def es_genero(diccionario:dict, str_genero:str)-> bool:
  """  
  determina si el genero de un personaje recibido por parametro coincide con el genero recibido por parametro\n 
  [diccionario : dict] -> diccionario con la info de un heroe, incluida la clave "genero"\n
  [str_genero : str] -> string para realizar la verificacion ("F", "M" o "NB")\n
  return bool -> True si hay coincidencia, False caso contrario
  """
  if isinstance(diccionario, dict) and diccionario and "genero" in diccionario and diccionario["genero"].lower() == str_genero.lower():
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
def calcular_min_genero(lista_heroes: list[dict], clave: str, str_genero: str)-> float:
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
def calcular_max_genero(lista_heroes: list[dict], clave: str, str_genero: str)-> float:
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
def calcular_max_min_dato_genero(lista_heroes: list[dict], valor_buscado: str, clave: str, str_genero: str)-> list:
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
def stark_calcular_imprimir_heroe_genero(lista_heroes: list[dict], valor_buscado: str, clave: str, str_genero: str, margin_top: bool = False)-> None:
  """  
  dadas la lista de heroes, un string "minimo" o "maximo", una clave a analizar y un genero, imprime el listado de superheroes que coincidan con dichos criterios\n 
  [lista_heroes : list[dict]] -> listado de heroes\n
  [valor_buscado : str] -> "minimo"|"maximo", criterio de seleccion\n
  [clave : str] -> clave a evaluar\n
  [str_genero : str] -> genero a evaluar\n
  return None 
  """
  if not lista_heroes:
    return -1
  if margin_top:
    print("\n")
  lista_final = calcular_max_min_dato_genero(lista_heroes, valor_buscado, clave, str_genero)
  for heroe in lista_final:
    imprimir_dato(obtener_nombre_y_dato(heroe, clave))
  print("\n")

# 3.1
def sumar_dato_heroe_genero(lista_heroes: list[dict], clave: str, str_genero: str)-> float:
  """  
  dada la lista de diccionarios de superheroes, un genero ("F", "M" o "NB") y un campo numerico especificado (altura, fuerza o peso), retorna la suma de todos los valores de ese campo numerico hallados en todos los diccionarios cuyo campo genero coincida con el recibido por parametro\n 
  [lista_heroes: list[dict]] listado de heroes\n
  [clave: str] clave numrica a sumar\n
  [str_genero: str] genero a relevar\n
  return: float -> suma hallada 
  """
  heroes_genero = filter(lambda heroe: es_genero(heroe, str_genero), lista_heroes)
  # * las validaciones solicitadas requerimiento 3.1 se encuentran en la funcion es_genero y son aplicadas en la linea anterior
  return sum(castear_dato_a_float(heroe[clave]) for heroe in heroes_genero if clave in heroe and isinstance(castear_dato_a_float(heroe[clave]), (int, float)))

# 3.2
def cantidad_heroes_genero(lista_heroes: list[dict], str_genero: str)-> int:
  """  
  dada la lista de diccionarios de superheroes y un genero ("F", "M" o "NB"), retorna la cantidad de superheres cuyo genero coincide con el recibido por parametro\n 
  [lista_heroes: list[dict]] listado de heroes\n
  [str_genero: str] genero a relevar\n
  return: int -> cantidad hallada 
  """
  heroes_genero = list(filter(lambda heroe: es_genero(heroe, str_genero), lista_heroes))
  return len(heroes_genero)

# 3.3
def calcular_promedio_genero(lista_heroes: list[dict], clave: str, str_genero: str)->float:
  """  
  dada la lista de diccionarios de superheroes, un genero ("F", "M" o "NB") y un campo numerico especificado (altura, fuerza o peso), retorna el promedio resultante del total de los valores del campo numerico hallado en todos los diccionarios con el campo genero especificado\n 
  [lista_heroes: list[dict]] listado de heroes\n
  [clave: str] clave numrica a sumar\n
  [str_genero: str] genero a relevar\n
  return: float -> promedio hallado 
  """
  total_clave_especificada = sumar_dato_heroe_genero(lista_heroes, clave, str_genero)
  cantidad_heroes = cantidad_heroes_genero(lista_heroes, str_genero)
  return total_clave_especificada / cantidad_heroes

# 3.4
def stark_calcular_imprimir_promedio_altura_genero(lista_heroes: list[dict], clave: str, str_genero: str)->float:
  """  
  dada la lista de diccionarios de superheroes, un genero ("F", "M" o "NB") y un campo numerico especificado (altura, fuerza o peso), imprime una leyenda que incluye el promedio resultante del total de los valores del campo numerico hallado en todos los diccionarios con el campo genero especificado\n 
  [lista_heroes: list[dict]] listado de heroes\n
  [clave: str] campo numerico a sumar\n
  [str_genero: str] genero a relevar\n
  return: None -> imprime una leyenda (str) que incluye el promedio hallado 
  """
  if not lista_heroes:
    return "Error: Lista de héroes vacía"
  print("\n")
  print(f"{clave.capitalize()} promedio genero {str_genero.upper()}: {calcular_promedio_genero(lista_heroes, clave, str_genero)}")
  print("\n")

# 4.1
def calcular_cantidad_tipo(lista_heroes: list[dict], clave: str) -> dict:
  """  
  retorna un diccionario con los distintos valores del tipo de dato recibido por parámetro y la cantidad de cada uno\n 
  [lista_heroes: list[dict]] listado de heroes\n
  [clave: str] campo a procesar\n
  return bool|dict -> False si la lista de heroes recibida esta vacia|diccionario resultante
  """
  if not lista_heroes:
    return "Error: Lista de héroes vacía"
  diccionario_resultante = {}
  for heroe in lista_heroes:
      nueva_clave = heroe.get(clave, "No tiene") 
      if not nueva_clave:
        nueva_clave = "No tiene"
      diccionario_resultante[nueva_clave] = diccionario_resultante.get(nueva_clave, 0) + 1
  claves_ordenadas = sorted(diccionario_resultante.keys())
  diccionario_resultante = {key: diccionario_resultante[key] for key in claves_ordenadas}
  return diccionario_resultante

# 4.2
def imprimir_cantidad_heroes_tipo(diccionario: dict, clave: str) -> None:
  """  
  recibe un diccionario con los datos procesados de una propiedad en particular de los heroes en la lista de superheroes, los formatea e imprime el resultado por consola\n 
  [lista_heroes: list[dict]] listado de heroes\n
  [clave: str] propiedad asociada a los datos procesados en el diccionario\n
  return None -> imprime un informe por consola
  """
  imprimir_dato("\n")
  string = ""
  for k,v in diccionario.items():
    string += f"Característica: {clave} {k} - Cantidad de héroes: {v}\n"
  imprimir_dato(string) 
  imprimir_dato("\n")

# 4.3
def stark_calcular_cantidad_por_tipo(lista_heroes: list[dict], clave: str) -> None:
  """  
  recibe la lista de superheroes y un campo en particular a partir del cual se imprimira por pantalla un informe con los distintos valores existentes para ese campo y la cantidad de veces que se repite cada uno en la lista\n 
  [lista_heroes: list[dict]] listado de heroes\n
  [clave: str] campo a relevar en los diccionarios\n
  return None -> imprime un informe por consola
  """
  imprimir_cantidad_heroes_tipo(calcular_cantidad_tipo(lista_heroes, clave), clave)

# 5.1
def obtener_lista_de_tipos(lista_heroes: list[dict], clave: str) -> None:
  """  
  a partir de la lista de superheroes y un clave dada, genera una lista de str con todos los valores hallados para dicha clave, eliminando duplicados y agregando el elemento "N/A" si alguno de los diccionarios no contara con dicha clave o el valor de la clave fuera None\n 
  [lista_heroes: list[dict]] listado de heroes\n
  [clave: str] campo a relevar en los diccionarios\n
  return list -> lista de str
  """
  return sorted(list({heroe[clave] if clave in heroe and heroe[clave] else "N/A" for heroe in lista_heroes}))

# 5.2
def normalizar_dato(dato: str, string_default: str) -> str:
  """  
  valida si el string recibido como primer parametro no es un string vacio, en caso de serlo retorna el string recibido como segundo parametro\n 
  [dato: str] string a validar\n
  return [dato] si no es string vacio, "Sin datos" caso contrario
  """
  try:
    if not dato.strip():
      return string_default
    return dato.strip()
  except AttributeError as error:
    return "El primer parametro debe ser de tipo string"

# 5.3
def obtener_heroes_por_tipo(lista_heroes: list[dict], clave: str) -> None:
  from collections import defaultdict
  from collections import OrderedDict
  """  
  a partir de la lista de superheroes y un clave dada, genera un diccionario cuyas claves son las variedades encontradas de la clave recibida, y el valor de cada una de estas claves es la lista de los superheroes, agrupados segun cada variedad de la clave recibida\n 
  [lista_heroes: list[dict]] listado de heroes\n
  [clave: str] campo a relevar en los diccionarios\n
  return dict -> diccionario de listas
  """
  diccionario = defaultdict(list)
  for heroe in lista_heroes:
    valor_clave = heroe.get(clave, "Sin datos")
    valor_clave = "Sin datos" if not valor_clave else valor_clave
    nombre = heroe["nombre"]
    diccionario[valor_clave].append(nombre)
  return OrderedDict(sorted(dict(diccionario).items()))

# 5.4
def imprimir_heroes_por_tipo(lista_heroes: list[dict], clave: str) -> str:
  """  
  recibe la lista de heroes y una clave, detecta las variantes para esa clave e imprime por pantalla un informe agrupando a los superheroes cuyos valores para una determinada variedad de la clave recibida sean coincidentes\n 
  [lista_heroes: list[dict]] listado de heroes\n
  [clave: str] campo a relevar en los diccionarios\n
  return None -> imprime un informe por pantalla
  """
  print("\n")
  fila = ""
  diccionario_variedad = obtener_heroes_por_tipo(lista_heroes, clave)
  for variedad, lista_h in diccionario_variedad.items():
    fila += f"{clave} \"{variedad}\": " 
    for nombre in lista_h:
      fila += f"{nombre} | "
    fila = fila[:-2]
    fila += "\n"
  imprimir_dato(fila)
  print("\n")

# 5.5
def stark_listar_heroes_por_dato(lista_heroes: list[dict], clave: str) -> str:
  """  
  recibe la lista de heroes y una clave, detecta las variantes para esa clave e imprime por pantalla un informe agrupando a los superheroes cuyos valores para una determinada variedad de la clave recibida sean coincidentes\n 
  [lista_heroes: list[dict]] listado de heroes\n
  [clave: str] campo a relevar en los diccionarios\n
  return None -> imprime un informe por pantalla
  """
  imprimir_heroes_por_tipo(lista_heroes, clave)

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

# --------------------------------- BLOQUE DE FUNCIONES 03 - FIN ---------------------------------------

if __name__ == "__main__":
  limpiar_consola()
  from datos_stark import lista_personajes

  stark_listar_heroes_por_dato(lista_personajes, "color_ojos")


# cd Desktop/utn/cuatrimestre1/programacion_1/ENTREGAS/stark/03
# python biblioteca_stark_03.py
# python main.py