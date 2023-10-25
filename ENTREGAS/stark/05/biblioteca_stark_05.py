from inspect import currentframe as linea
# imprimir_linea(linea().f_lineno)

def limpiar_consola():
    import os
    """  
    limpia la consola
    """
    # os.system('cls' if os.name == 'nt' else 'clear')
    if os.name in ["ce", "nt", "dos"]: # windows
      os.system("cls")
    else: # linux o mac
      os.system("clear")

def imprimir_linea(linea):
   # imprimir_linea(linea().f_lineno)
   print(f"Linea {linea}")

# 1.3
def stark_marvel_app_5(lista_personajes):
    """
    """
    limpiar_consola()
    while True:
        opcion_seleccionada = -1
        while opcion_seleccionada == -1:
            opcion_seleccionada = stark_menu_principal_desafio_5() 
            if opcion_seleccionada not in ("z", "Z"):
                limpiar_consola()
        match opcion_seleccionada:
            # a - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
            case "a" | "A":
                imprimir_dato("a- Listado superhéroes de género masculino(M):\n")
                stark_imprimir_heroe_genero(lista_personajes, "m")
            # b - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
            case "b" | "B":
                imprimir_dato("b- Listado superhéroes de género femenino(F):\n")
                stark_imprimir_heroe_genero(lista_personajes, "f")
            # c - Recorrer la lista y determinar cuál es el superhéroe más alto de género M
            case "c" | "C":
                imprimir_dato("c- Superhéroe más alto género masculino(M):\n")
                stark_calcular_imprimir_heroe_genero(lista_personajes, "maximo", "altura", "M", True)
            # e - Recorrer la lista y determinar cuál es el superhéroe más alto de género F
            case "d" | "D":
                imprimir_dato("d- Superhéroe más alto género femenino(F):\n")
                stark_calcular_imprimir_heroe_genero(lista_personajes, "maximo", "altura", "F", True)
            # e - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M
            case "e" | "E":
                imprimir_dato("e- Superhéroe más bajo género masculino(M):\n")
                stark_calcular_imprimir_heroe_genero(lista_personajes, "minimo", "altura", "M", True)
            # f - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F
            case "f" | "F":
                imprimir_dato("f- Superhéroe más bajo género femenino(F):\n")
                stark_calcular_imprimir_heroe_genero(lista_personajes, "minimo", "altura", "F", True)
            # g - Recorrer la lista y determinar la altura promedio de los superhéroes de género M
            case "g" | "G":
                imprimir_dato("g- Altura promedio superhéroes género masculino(M):\n")
                stark_calcular_imprimir_promedio_altura_genero(lista_personajes, "altura", "m")
            # h - Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
            case "h" | "H":
                imprimir_dato("h- Altura promedio superhéroes género femenino(M):\n")
                stark_calcular_imprimir_promedio_altura_genero(lista_personajes, "altura", "f")
            # i - Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
            case "i" | "I":
                imprimir_dato("i- Informe:")
                imprimir_dato("\nc- Superhéroe más alto género masculino(M)")
                stark_calcular_imprimir_heroe_genero(lista_personajes, "maximo", "altura", "M")

                imprimir_dato("\nd- Superhéroe más alto género femenino(F)")
                stark_calcular_imprimir_heroe_genero(lista_personajes, "maximo", "altura", "F")

                imprimir_dato("\ne- Superhéroe más bajo género masculino(M)")
                stark_calcular_imprimir_heroe_genero(lista_personajes, "minimo", "altura", "M")

                imprimir_dato("\nf- Superhéroe más bajo género femenino(F)")
                stark_calcular_imprimir_heroe_genero(lista_personajes, "minimo", "altura", "F")
            # j - Determinar cuántos superhéroes tienen cada tipo de color de ojos.
            case "j" | "J":
                imprimir_dato("j- Color de ojos (cantidad según tipo):\n")
                stark_calcular_cantidad_por_tipo(lista_personajes, "color_ojos")
            # k - Determinar cuántos superhéroes tienen cada tipo de color de pelo.
            case "k" | "K":
                imprimir_dato("k- Color de pelo (cantidad según tipo):\n")
                stark_calcular_cantidad_por_tipo(lista_personajes, "color_pelo")
            # l - Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con "No Tiene")
            case "l" | "L":
                imprimir_dato("l- Inteligencia (cantidad según tipo):\n")
                stark_calcular_cantidad_por_tipo(lista_personajes, "inteligencia")
            # m - Listar todos los superhéroes agrupados por color de ojos.
            case "m" | "M":
                imprimir_dato("m- Color de ojos (agrupados por tipo):\n")
                stark_listar_heroes_por_dato(lista_personajes, "color_ojos")
            # n - Listar todos los superhéroes agrupados por color de pelo.
            case "n" | "N":
                imprimir_dato("n- Color de pelo (agrupados por tipo):\n")
                stark_listar_heroes_por_dato(lista_personajes, "color_pelo")
            # o - Listar todos los superhéroes agrupados por tipo de inteligencia
            case "o" | "O":
                imprimir_dato("o- Inteligencia (agrupados por tipo):\n")
                stark_listar_heroes_por_dato(lista_personajes, "inteligencia")
            # salir del programa
            case "z" | "Z":
                print("\nHasta la próxima\n")
                break

# 1.2
def stark_menu_principal_desafio_5():
    """ 
    """
    import re 
    imprimir_menu_desafio_5()
    opcion_ingresada = input("Elija una opción: ")
    validacion = re.search(r"^[a-oA-OzZ]{1}$", opcion_ingresada)
    if not validacion:
        return -1 
    return opcion_ingresada

# 1.1
def imprimir_menu_desafio_5():
    """  
    """
    menu = """\na - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
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
z - Salir\n"""
    imprimir_dato(menu)

# 1.4
def leer_archivo(nombre_archivo_json):
    """ 
    Crear la función 'leer_archivo' la cual recibirá por parámetro un string que indicará el nombre y extensión del archivo a leer (Ejemplo: archivo.json). Dicho archivo se abrirá en modo lectura únicamente y retornará la lista de héroes como una lista de diccionarios.
    """
    import json
    with open(nombre_archivo_json, "r", encoding="utf-8") as archivo:
        contenido_json = json.load(archivo)
    return contenido_json["lista_personajes"]

# 1.5
def guardar_archivo(nombre_archivo_csv: str, contenido_csv:str):
    """
    genera o reescribe un .csv con el nombre y el contenido especificados por el usuario\n
    nombre_archivo_csv: str -> nombre del archivo a crear\n
    contenido_csv: str -> contenido del archivo a crear\n
    return bool -> True si el archivo se pudo crear, False caso contrario
    """ 
    # nombre_archivo_csv = "nombre_archivo.csv"
    # contenido_csv = "nombre;altura;fuerza\nHoward;78;4\nSantos;134,1"
    try:
      with open(f"csv/{nombre_archivo_csv}", "w", encoding="utf-8") as csv_nuevo:
        csv_nuevo.write(f"{contenido_csv}")
      print(f"Se creó el archivo: {nombre_archivo_csv}")
      return True
    except:  
      print(f"Error al crear el archivo: {nombre_archivo_csv}")
      return False

# 1.6
def capitalizar_palabras(string: str):
  """ 
  """
  lista_string = string.split(" ")
  lista_string = " ".join(list(map(str.capitalize, lista_string)))
  return lista_string

# 1.7
def obtener_nombre_capitalizado(diccionario_heroe: dict):
  return f"Nombre: {capitalizar_palabras(diccionario_heroe.get('nombre', ''))}"

# 1.8
def obtener_nombre_y_dato_stark05(diccionario: dict, key: str) -> str:
  """  
  de un diccionario dado, retorna una leyenda (str) con los valores de las claves "nombre" y la especificada por parametro\n 
  [diccionario: dict] datos de un superheroe en formato dict\n
  [key: str] clave que se busca retornar junto a "nombre"\n
  return str "Nombre: xxx | [key]: xxx"
  """
  valor_dinamico = diccionario.get(key, 'sin datos')
  return f"{obtener_nombre_capitalizado(diccionario)} | {capitalizar_palabras(key)}: {valor_dinamico}"

# 2.1
def es_genero_stark05(diccionario:dict, str_genero:str)-> bool:
  """  
  determina si el genero de un personaje recibido por parametro coincide con el genero recibido por parametro\n 
  [diccionario : dict] -> diccionario con la info de un heroe, incluida la clave "genero"\n
  [str_genero : str] -> string para realizar la verificacion ("F", "M" o "NB")\n
  return bool -> True si hay coincidencia, False caso contrario
  """
  if isinstance(diccionario, dict) and diccionario and "genero" in diccionario and diccionario.get("genero").lower() == str_genero.lower():
    return True 
  return False

# 2.2 
def stark_guardar_heroe_genero(lista_heroes: list[dict], genero: str):
  """  
  genera o reescribe un .csv con la info de la lista de heroes del genero recibido por parametro\n
  lista_heroes: list[dict] -> lista de heroes\n
  genero: str -> genero a buscar en la lista ("f", "m" o "nb")\n
  return bool -> True si el archivo se pudo crear, False caso contrario
  """
  contenido_csv = ",".join(lista_heroes[0].keys())
  contenido_csv += "\n"
  for heroe in lista_heroes:
    if(es_genero_stark05(heroe, genero)):
      contenido_csv += ",".join(heroe.values())
      contenido_csv += "\n"
      imprimir_dato(obtener_nombre_capitalizado(heroe))
  match genero.lower():
    case "f":
      nombre_archivo = "heroes_F.csv"
    case "m":
      nombre_archivo = "heroes_M.csv"
    case _:
      nombre_archivo = "heroes_NB.csv"
  if guardar_archivo(nombre_archivo, contenido_csv):
     return True
  else:
     return False

# 3.1
def calcular_min_genero_stark05(lista: list[dict], clave: str, genero: str):
  """ 
  dado un genero y una clave hallara el valor minimo de esa clave para los heroes de ese genero en la lista de heroes\n 
  lista: list[dict] -> lista de diccionarios\n
  key: str -> clave a evaluar\n
  genero: str -> genero("f" o "m")\n
  list[dict] -> retorna una lista con los heroes del genero dado, cuyos valores para la clave dada coincida con el minimo hallado
  """
  listado_heroes_segun_genero = [heroe for heroe in lista if heroe.get("genero").lower() == genero.lower()]
  stark_normalizar_datos(listado_heroes_segun_genero)
  valor_minimo = min(listado_heroes_segun_genero, key = lambda diccionario: diccionario[clave])[clave]
  listado_heroes_valor_minimo = [heroe for heroe in listado_heroes_segun_genero if heroe.get(clave) == valor_minimo]
  return list(listado_heroes_valor_minimo)

# 3.2
def calcular_max_genero_stark05(lista: list[dict], clave: str, genero: str):
  """ 
  dado un genero y una clave hallara el valor maximo de esa clave para los heroes de ese genero en la lista de heroes\n 
  lista: list[dict] -> lista de diccionarios\n
  key: str -> clave a evaluar\n
  genero: str -> genero("f" o "m")\n
  list[dict] -> retorna una lista con los heroes del genero dado, cuyos valores para la clave dada coincida con el maximo hallado
  """
  listado_heroes_segun_genero = [heroe for heroe in lista if heroe.get("genero").lower() == genero.lower()]
  stark_normalizar_datos(listado_heroes_segun_genero)
  valor_minimo = max(listado_heroes_segun_genero, key = lambda diccionario: diccionario[clave])[clave]
  listado_heroes_valor_minimo = [heroe for heroe in listado_heroes_segun_genero if heroe.get(clave) == valor_minimo]
  return list(listado_heroes_valor_minimo)

# --------------------------------- BLOQUE DE FUNCIONES STARKS ANTERIORES - INICIO ---------------------------------------

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
  ACCION: recibe una lista de diccionarios y una key para la que se buscará el mínimo valor presente en la lista, y retorna una nueva lista de diccionarios de todos aquellos diccionarios cuyo valor para esta key coincida con el valor mínimoximo hallado \n 
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
    # if margin_top:
    # print("\n")
  lista_final = calcular_max_min_dato_genero(lista_heroes, valor_buscado, clave, str_genero)
  for heroe in lista_final:
    imprimir_dato(obtener_nombre_y_dato(heroe, clave))
    # print("\n")

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

def cantidad_heroes_genero(lista_heroes: list[dict], str_genero: str)-> int:
  """  
  dada la lista de diccionarios de superheroes y un genero ("F", "M" o "NB"), retorna la cantidad de superheres cuyo genero coincide con el recibido por parametro\n 
  [lista_heroes: list[dict]] listado de heroes\n
  [str_genero: str] genero a relevar\n
  return: int -> cantidad hallada 
  """
  heroes_genero = list(filter(lambda heroe: es_genero(heroe, str_genero), lista_heroes))
  return len(heroes_genero)

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
  print(f"{clave.capitalize()} promedio genero {str_genero.upper()}: {calcular_promedio_genero(lista_heroes, clave, str_genero)}")

def obtener_nombre(diccionario: dict) -> str:
  """  
  obtiene el valor de la propiedad "nombre" de un diccionario y lo retorna en una leyenda (str):\n 
  PARAMETROS:\n
  [diccionario : dict] -> diccionario del cual se obtendra la el valor de la clave "nombre"\n
  return str
  """
  return f"Nombre: {diccionario.get('nombre', 'sin datos')}"

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

def stark_imprimir_heroe_genero(lista_heroes: list[dict], str_genero: str) -> None:
  """  
  imprime los nombres de los heroes cuyo genero coincida con el recibido por parametro\n 
  [lista_heroes : list[dict]] -> lista de heroes\n
  [str_genero : str] -> string para realizar la verificacion ("F", "M" o "NB")\n
  return None
  """
  heroes_genero = filter(lambda heroe: es_genero(heroe, str_genero), lista_heroes)
  for heroe in heroes_genero:
    imprimir_dato(obtener_nombre(heroe))

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

def imprimir_cantidad_heroes_tipo(diccionario: dict, clave: str) -> None:
  """  
  recibe un diccionario con los datos procesados de una propiedad en particular de los heroes en la lista de superheroes, los formatea e imprime el resultado por consola\n 
  [lista_heroes: list[dict]] listado de heroes\n
  [clave: str] propiedad asociada a los datos procesados en el diccionario\n
  return None -> imprime un informe por consola
  """
  string = ""
  for k,v in diccionario.items():
    string += f"Característica: {clave} {k} - Cantidad de héroes: {v}\n"
  imprimir_dato(string[:-1]) 

def stark_calcular_cantidad_por_tipo(lista_heroes: list[dict], clave: str) -> None:
  """  
  recibe la lista de superheroes y un campo en particular a partir del cual se imprimira por pantalla un informe con los distintos valores existentes para ese campo y la cantidad de veces que se repite cada uno en la lista\n 
  [lista_heroes: list[dict]] listado de heroes\n
  [clave: str] campo a relevar en los diccionarios\n
  return None -> imprime un informe por consola
  """
  imprimir_cantidad_heroes_tipo(calcular_cantidad_tipo(lista_heroes, clave), clave)

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

def imprimir_heroes_por_tipo(lista_heroes: list[dict], clave: str) -> str:
  """  
  recibe la lista de heroes y una clave, detecta las variantes para esa clave e imprime por pantalla un informe agrupando a los superheroes cuyos valores para una determinada variedad de la clave recibida sean coincidentes\n 
  [lista_heroes: list[dict]] listado de heroes\n
  [clave: str] campo a relevar en los diccionarios\n
  return None -> imprime un informe por pantalla
  """
  fila = ""
  diccionario_variedad = obtener_heroes_por_tipo(lista_heroes, clave)
  for variedad, lista_h in diccionario_variedad.items():
    fila += f"{clave} \"{variedad}\": " 
    for nombre in lista_h:
      fila += f"{nombre} | "
    fila = fila[:-2]
    fila += "\n"
  imprimir_dato(fila[:-1])

def stark_listar_heroes_por_dato(lista_heroes: list[dict], clave: str) -> str:
  """  
  recibe la lista de heroes y una clave, detecta las variantes para esa clave e imprime por pantalla un informe agrupando a los superheroes cuyos valores para una determinada variedad de la clave recibida sean coincidentes\n 
  [lista_heroes: list[dict]] listado de heroes\n
  [clave: str] campo a relevar en los diccionarios\n
  return None -> imprime un informe por pantalla
  """
  imprimir_heroes_por_tipo(lista_heroes, clave)

# --------------------------------- BLOQUE DE FUNCIONES STARKS ANTERIORES - FIN ---------------------------------------

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

def imprimir_dato(string: str):
  """  
  recibe un string y lo imprime por consola\n 
  [string: str] -> string a imprimir\n
  return None
  """
  print(string)

# -----------------------------

if __name__ == "__main__":
  limpiar_consola()
  hombre ={
      "nombre": "Wolverine",
      "identidad": "Logan",
      "empresa": "Marvel Comics",
      "altura": "160.69999999999999",
      "peso": "135.21000000000001",
      "genero": "M",
      "color_ojos": "Blue",
      "color_pelo": "Black",
      "fuerza": "35",
      "inteligencia": "good"
  }
  mujer = {
      "nombre": "Black Widow",
      "identidad": "Natasha Romanoff",
      "empresa": "Marvel Comics",
      "altura": "170.78999999999999",
      "peso": "59.340000000000003",
      "genero": "F",
      "color_ojos": "Green",
      "color_pelo": "Auburn",
      "fuerza": "15",
      "inteligencia": "good"
  }
  lista_heroes = leer_archivo("data_stark.json")
  limpiar_consola()
  hombre = {
    "nombre": "Wolverine",
    "identidad": "Logan",
    "empresa": "Marvel Comics",
    "altura": "160.69999999999999",
    "peso": "135.21000000000001",
    "genero": "M",
    "color_ojos": "Blue",
    "color_pelo": "Black",
    "fuerza": "35",
    "inteligencia": "good"
  }
  mujer = {
    "nombre": "Black Widow",
    "identidad": "Natasha Romanoff",
    "empresa": "Marvel Comics",
    "altura": "170.78999999999999",
    "peso": "59.340000000000003",
    "genero": "F",
    "color_ojos": "Green",
    "color_pelo": "Auburn",
    "fuerza": "15",
    "inteligencia": "good"
  }
  # print(es_genero_stark05(hombre, "F"))
  # print(es_genero_stark05(mujer, "M"))
  print(calcular_min_genero_stark05(lista_heroes, "altura", "F"))
  print(calcular_max_genero_stark05(lista_heroes, "altura", "F"))


   
    


# cd C:\Users\User\Desktop\utn\cuatrimestre1\programacion_1\ENTREGAS\stark\05
# python biblioteca_stark_05.py
# python main.py
