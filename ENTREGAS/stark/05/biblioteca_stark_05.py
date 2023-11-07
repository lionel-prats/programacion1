""" 
Alumno: Lionel Prats 
DNI: 31367577
División: 1H
Nro. legajo: 115678
Stark 05
"""
# IMPORTANTE: para que la creacion de archivos funcione correctamente hay que crear la carpeta /csv en la raiz del proyecto

from inspect import currentframe as linea
import re
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

# 1.3
def stark_marvel_app_5(lista_personajes):
    """
    Funcion principal del programa
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
                for heroe in lista_personajes:
                  if es_genero_stark05(heroe, "M"):
                    print(obtener_nombre_y_dato_stark05(heroe, "genero"))

            # b - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
            case "b" | "B":
                imprimir_dato("b- Listado superhéroes de género femenino(F):\n")
                for heroe in lista_personajes:
                  if es_genero_stark05(heroe, "F"):
                    print(obtener_nombre_y_dato_stark05(heroe, "genero"))

            # c - Recorrer la lista y determinar cuál es el superhéroe más alto de género M
            case "c" | "C":
                imprimir_dato("c- Superhéroe más alto género masculino(M):\n")
                stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "maximo", "altura", "M")

            # d - Recorrer la lista y determinar cuál es el superhéroe más alto de género F
            case "d" | "D":
                imprimir_dato("d- Superhéroe más alto género femenino(F):\n")
                stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "maximo", "altura", "F")

            # e - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M
            case "e" | "E":
                imprimir_dato("e- Superhéroe más bajo género masculino(M):\n")
                stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "minimo", "altura", "M")

            # f - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F
            case "f" | "F":
                imprimir_dato("f- Superhéroe más bajo género femenino(F):\n")
                stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "minimo", "altura", "F")
                
            # g - Recorrer la lista y determinar la altura promedio de los superhéroes de género M
            case "g" | "G":
                imprimir_dato("g- Altura promedio superhéroes género masculino(M):\n")
                stark_calcular_imprimir_guardar_promedio_altura_genero(lista_personajes, "M")

            # h - Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
            case "h" | "H":
                imprimir_dato("h- Altura promedio superhéroes género femenino(M):\n")
                stark_calcular_imprimir_guardar_promedio_altura_genero(lista_personajes, "F")

            # i - Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
            case "i" | "I":
                imprimir_dato("i- Informe:")
                imprimir_dato("\nc- Superhéroe más alto género masculino(M)")
                stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "maximo", "altura", "M")

                imprimir_dato("\nd- Superhéroe más alto género femenino(F)")
                stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "maximo", "altura", "F")

                imprimir_dato("\ne- Superhéroe más bajo género masculino(M)")
                stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "minimo", "altura", "M")

                imprimir_dato("\nf- Superhéroe más bajo género femenino(F)")
                stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "minimo", "altura", "F")

            # j - Determinar cuántos superhéroes tienen cada tipo de color de ojos.
            case "j" | "J":
                imprimir_dato("j- Color de ojos (cantidad según tipo):\n")
                stark_calcular_cantidad_por_tipo_stark05(lista_personajes, "color_ojos")

            # k - Determinar cuántos superhéroes tienen cada tipo de color de pelo.
            case "k" | "K":
                imprimir_dato("k- Color de pelo (cantidad según tipo):\n")
                stark_calcular_cantidad_por_tipo_stark05(lista_personajes, "color_pelo")

            # l - Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con "No Tiene")
            case "l" | "L":
                imprimir_dato("l- Inteligencia (cantidad según tipo):\n")
                stark_calcular_cantidad_por_tipo_stark05(lista_personajes, "inteligencia")

            # m - Listar todos los superhéroes agrupados por color de ojos.
            case "m" | "M":
                imprimir_dato("m- Color de ojos (agrupados por tipo):\n")
                stark_listar_heroes_por_dato_stark05(lista_personajes, "color_ojos")

            # n - Listar todos los superhéroes agrupados por color de pelo.
            case "n" | "N":
                imprimir_dato("n- Color de pelo (agrupados por tipo):\n")
                stark_listar_heroes_por_dato_stark05(lista_personajes, "color_pelo")

            # o - Listar todos los superhéroes agrupados por tipo de inteligencia
            case "o" | "O":
                imprimir_dato("o- Inteligencia (agrupados por tipo):\n")
                stark_listar_heroes_por_dato_stark05(lista_personajes, "inteligencia")

            # salir del programa
            case "z" | "Z":
                print("\nHasta la próxima\n")
                break

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
def guardar_archivo(nombre_archivo: str, contenido_archivo:str):
  """
  La función `guardar_archivo` crea o sobrescribe un archivo con el nombre, extension y contenido especificados.
  :param nombre_archivo: El parámetro `nombre_archivo` es una cadena que representa el nombre y la extension del archivo que se creará o sobrescribirá
  :param contenido_archivo: El parámetro `contenido_archivo` es una cadena que representa el contenido del archivo. 
  :return: un valor booleano. Devuelve True si el archivo se creó correctamente o False si hubo un error al crear el archivo.
  """
  try:
    with open(f"csv/{nombre_archivo}", "w", encoding="utf-8") as csv_nuevo:
      csv_nuevo.write(f"{contenido_archivo}")
    print(f"Se creó el archivo: {nombre_archivo}")
    return True
  except:  
    print(f"Error al crear el archivo: {nombre_archivo}")
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

# 3.3 
def calcular_max_min_dato_genero_stark05(lista: list[dict], tipo_filtro: str, clave: str, genero: str):
  """ 
  recibe la lista de heroes, un tipo_filtro (minimo o maximo), un campo por el cual buscar y un genero ("f" o "m"); segun los parametros recibidos retornara una lista con los heroes del genero dado, cuyos valores para la clave dada coincidan con el minimo o maximo hallado en la lista (segun indique esl usuario)\n
  lista: list[dict] -> lista de heroes\n
  tipo_filtro: str -> "maximo" o "minimo"\n
  clave: str -> clave a evaluar\n
  genero: str -> genero a evaluar\n
  RETURN: retorna una nueva lista de heroes segun lo indicado anteriormente
  """
  if tipo_filtro == "minimo":
    return calcular_min_genero_stark05(lista, clave, genero)
  if tipo_filtro == "maximo":
    return calcular_max_genero_stark05(lista, clave, genero)
  else:
    return False

# 3.4
def stark_calcular_imprimir_guardar_heroe_genero(lista: list[dict], calculo: str, key: str, genero: str):
  """  
  lista -> lista de heroes
  calculo -> "minimo o maximo"
  key -> clave a evaluar
  genero -> genero a evaluar
  """
  resultado_busqueda = calcular_max_min_dato_genero_stark05(lista, calculo, key, genero)
  inicio = "Mayor" if calculo == "maximo" else "Menor"
  for heroe in resultado_busqueda:
    imprimir_dato(f"{inicio} {capitalizar_palabras(key)}: {obtener_nombre_y_dato(heroe, key)}")
  nombre_archivo_csv = f"heroes_{calculo}_{key}_{capitalizar_palabras(genero)}.csv"
  contenido_archivo_csv = generar_contenido_csv_lista_diccionarios(resultado_busqueda)
  if guardar_archivo(nombre_archivo_csv, contenido_archivo_csv):
    return True
  else:
    return False
  
# 4.1
def sumar_dato_heroe_genero_stark05(lista: list[dict], key: str, genero: str) -> float:
  """  
  dada una clave y un genero, retorna la suma total de esa clave para los heroes de ese genero\n
  """
  stark_normalizar_datos(lista)
  total = 0
  for diccionario in lista:
    if (isinstance(diccionario, dict) and diccionario 
        and diccionario.get("genero").lower() == genero.lower()):
      total += diccionario[key]
  return total

# 4.2
def cantidad_heroes_genero(lista_heroes: list[dict], str_genero: str)-> int:
  """  
  dada la lista de diccionarios de superheroes y un genero ("F", "M" o "NB"), retorna la cantidad de superheres cuyo genero coincide con el recibido por parametro\n 
  [lista_heroes: list[dict]] listado de heroes\n
  [str_genero: str] genero a relevar\n
  return: int -> cantidad hallada 
  """
  heroes_genero = list(filter(lambda heroe: es_genero(heroe, str_genero), lista_heroes))
  return len(heroes_genero)

# 4.3 
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
  return dividir(total_clave_especificada, cantidad_heroes)

#4.4
def stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes: list[dict], genero: str):
  """  
  """
  if not lista_heroes:
    imprimir_dato("Error: Lista de héroes vacía.")
    return False
  else:
    altura_promedio_genero = calcular_promedio_genero(lista_heroes, "altura", genero) 
    dato = f"Altura promedio género {capitalizar_palabras(genero)}: {altura_promedio_genero}"
    imprimir_dato(dato)
  nombre_archivo_csv = f"heroes_promedio_altura_{capitalizar_palabras(genero)}.csv"
  if guardar_archivo(nombre_archivo_csv, dato):
    return True
  else:
    return False

# 5.1
def calcular_cantidad_tipo(lista_heroes: list[dict], clave: str) -> dict:
  """  
  retorna un diccionario con los distintos valores del tipo de dato recibido por parámetro y la cantidad de cada uno\n 
  [lista_heroes: list[dict]] listado de heroes\n
  [clave: str] campo a procesar\n
  return bool|dict -> False si la lista de heroes recibida esta vacia|diccionario resultante
  """
  if not lista_heroes:
    return {"Error": "La lista se encuentra vacía"}
  diccionario_resultante = {}
  for heroe in lista_heroes:
      nueva_clave = capitalizar_palabras(heroe.get(clave, "No Tiene"))
      if not nueva_clave:
        nueva_clave = "No Tiene"
      diccionario_resultante[nueva_clave] = diccionario_resultante.get(nueva_clave, 0) + 1
  claves_ordenadas = sorted(diccionario_resultante.keys()) # lista de las claves del diccionario, ordenadas alfabeticamente
  diccionario_resultante = {key: diccionario_resultante[key] for key in claves_ordenadas}
  return diccionario_resultante

# 5.2
def guardar_cantidad_heroes_tipo(diccionario: dict, dato_relevado: str):
  """
  La función "guardar_cantidad_heroes_tipo" toma como entrada un diccionario y un dato relevado, y
  guarda la información en un archivo .txt con un nombre específico que incluye el dato relevado.
  :param diccionario: Un diccionario que contiene las características de los héroes y sus cantidades
  correspondientes
  :param dato_relevado: El parámetro "dato_relevado" representa el dato relevado o característica de
  los héroes presente en el diccionario. Podría ser algo como "fueza", "color_ojos", "color_pelo", etc
  :return: True si el archivo se creo correctamente o False si fallo la creacion.
  """
  nombre_archivo = f"heroes_cantidad_{dato_relevado}.txt"
  contenido_archivo = ""
  for k, v in diccionario.items():
    contenido_archivo += f"Caracteristica: {dato_relevado} {k} - Cantidad de heroes: {v}\n"

  print(contenido_archivo)

  archivo_guardado = guardar_archivo(nombre_archivo, contenido_archivo)  
  if archivo_guardado:
    return True
  else:
    return False

# 5.3
def stark_calcular_cantidad_por_tipo_stark05(lista_heroes: list[dict], clave_a_buscar: str):
  """
  La función "stark_calcular_cantidad_por_tipo_stark05" toma como entrada la lista de heroes y un dato a relevar 
  (puede ser algo como "fueza", "color_ojos", "color_pelo", etc).
  Calcula la cantidad de coincidencias para cada variante del dato a relevar y vuelca la informacion resultante
  en un .txt que guarda en la carpeta /csv.
  :param lista_heroes: lista de heroes
  :param dato_relevado: El parámetro "clave_a_buscar" representa el dato a relevar en toda la lista de heroes.
  :return: True si el archivo se creo correctamente o False si algo fallo durante la ejecucion.
  """
  diccionario_resultados = calcular_cantidad_tipo(lista_heroes, clave_a_buscar)
  archivo_guardado = guardar_cantidad_heroes_tipo(diccionario_resultados, clave_a_buscar)
  if archivo_guardado:
    return True
  else:
    return False

# 6.1
def obtener_lista_de_tipos(lista_heroes: list[dict], clave_a_buscar: str):
  """
  La función "obtener_lista_de_tipos" toma una lista de diccionarios y una clave para buscar, y
  devuelve un set de valores correspondientes a esa clave en los diccionarios y "N/A" para valores faltantes o vacíos.
  :param lista_heroes: Una lista de diccionarios que representan héroes. Cada diccionario contiene
  información sobre un héroe, como su nombre, edad y poderes
  :param clave_a_buscar: El parámetro "clave_a_buscar" es una cadena que representa la clave a buscar
  en los diccionarios dentro de la lista "lista_heroes"
  :return: el set de valores obtenidos de la clave especificada en cada diccionario de la lista
  dada.
  """
  lista_valores_segun_clave = [capitalizar_palabras(heroe[clave_a_buscar]) if (clave_a_buscar in heroe and heroe[clave_a_buscar]) else "N/A" for heroe in lista_heroes]
  return set(lista_valores_segun_clave)
    
# 6.2
def normalizar_dato(dato: str, dato_default: str):
  """
  La función normalizar_dato recibe los strings "dato" y "dato_default"
  devuelve `dato` si no está vacío, de lo contrario devuelve `dato_default`.
  :param dato: El parámetro `dato` es una cadena que representa los datos que deben normalizarse
  :param dato_default: El parámetro dato_default es una cadena que representa el valor predeterminado
  que se devolverá si el parámetro `dato` está vacío o Ninguno
  :return: La función `normalizar_dato` devuelve el valor de `dato` si no está vacía, en caso
  contrario devuelve el valor de `dato_default`.
  """
  if dato:
    return dato
  else:
    return dato_default

# 6.3
def normalizar_heroe(heroe: dict, clave: str):
  """
  La función normalizar_heroe toma un diccionario que representa un héroe y una clave
  normaliza el valor asociado con esa clave, capitaliza cada palabra de la clave nombre, 
  castea a int o float segun corresponda el valor de cada clave factible de ser casteada 
  y devuelve el diccionario del héroe actualizado.
  :param heroe: El parámetro `heroe` es un diccionario que representa a un héroe. 
  Contiene varios pares clave-valor donde las claves representan diferentes atributos del héroe (por ejemplo, "nombre" para el nombre, "fuerza" para la fuerza, etc.) 
  y los valores representan los valores correspondientes de esos atributos
  :param clave: El parámetro "clave" es una cadena que representa la clave en el diccionario "héroe"
  que debe normalizarse
  :return: un diccionario con los valores normalizados para la clave especificada.
  """
  regex_int = r'^\d+$'
  regex_float = r'^\d+\.\d+$'

  heroe_copy = heroe.copy()

  dato_normalizado = normalizar_dato(capitalizar_palabras(heroe_copy.get(clave)), "N/A")

  heroe_copy["nombre"] = capitalizar_palabras(heroe_copy.get("nombre"))
  heroe_copy[clave] = dato_normalizado

  for k, v in heroe_copy.items():
    pass
    if bool(re.match(regex_int, str(v))):
      heroe_copy[k] = int(v)
    elif bool(re.match(regex_float, str(v))):
      heroe_copy[k] = float(v)
  return heroe_copy

# 6.4
def obtener_heroes_por_tipo_stark05(lista_heroes: list[dict], set_variedades_segun_clave: set, clave_a_evaluar: str):
  """
  La función "obtener_heroes_por_tipo_stark05" toma una lista de diccionarios, un set de valores
  y una clave para evaluar, y devuelve un diccionario donde las claves son los valores del set y
  los valores son listas de nombres de héroes cuyo valor para la clave a evaluar coincide con la clave del diccionario a retornar.
  :param lista_heroes: Una lista de diccionarios que representan diferentes héroes
  :param set_variedades_segun_clave: El parámetro set_variedades_segun_clave es un set que
  contiene diferentes variedades o tipos de héroes en función de una clave específica. Por ejemplo, si la clave es "inteligencia", el set_variedades_segun_clave podría contener valores como "high", "good", etc.
  :param clave_a_evaluar: El parámetro "clave_a_evaluar" es una cadena que representa la clave en el
  diccionario de cada héroe que será evaluado. Se utiliza para determinar el tipo o categoría del
  héroe
  :return: un diccionario donde las claves son las diferentes variedades obtenidas del set
  `set_variedades_segun_clave`, y los valores son listas de nombres de héroes cuyo valor para la clave a evaluar coincide con la clave del diccionario a retornar.
  """

  diccionario_final = {}

  for variedad in set_variedades_segun_clave:
    if not variedad in diccionario_final:
      diccionario_final[variedad] = []
      for heroe in lista_heroes:
        heroe = normalizar_heroe(heroe, clave_a_evaluar)
        for k, v in heroe.items():
          if k == clave_a_evaluar and v == variedad:
            diccionario_final[variedad].append(capitalizar_palabras(heroe.get("nombre"))) 

  return diccionario_final
  
# 6.5
def guardar_heroes_por_tipo(diccionaro_heroes_segun_tipo: dict, dato_relevado: str):
  """
  La función "guardar_heroes_por_tipo" recibe un diccionario cuyas claves son las variedades de tipos para una
  caracteristica en particular (fuerza, color_ojos, etc) y los valores son listas de nombres de heroes cuyo valor para esa clave coincide con la clave
  tambien recibe dato_relevado, un string que representa la caracteristica a partir de la cual se estructura
  el diccionario
  la funcion guarda la informacion del diccionario en un archivo.csv en la carpeta /csv
  :param diccionaro_heroes_segun_tipo: Un diccionario que contiene héroes categorizados por sus tipos.
  Las claves del diccionario representan los tipos de héroes y los valores son listas de nombres de
  héroes que pertenecen a cada tipo
  :param dato_relevado: El parámetro "dato_relevado" es una cadena que representa los datos o
  información relevante que se está guardando. Se utiliza para crear el nombre del archivo que se
  guardará
  :return: un valor booleano. Si el archivo se guarda correctamente, devuelve Verdadero. De lo
  contrario, devuelve Falso.
  """
  nombre_archivo = f"heroes_segun_{dato_relevado}.csv"
  
  contenido_archivo = ""
  
  for tipo, nombres in diccionaro_heroes_segun_tipo.items():
    contenido_archivo += f"{dato_relevado} {tipo}: "
    for nombre_heroe in nombres:
      contenido_archivo += f"{nombre_heroe} | "
    contenido_archivo = contenido_archivo[:-3] 
    contenido_archivo += f"\n"
  
  print(contenido_archivo)

  archivo_guardado = guardar_archivo(nombre_archivo, contenido_archivo)  
  if archivo_guardado:
    return True
  else:
    return False

# 6.6
def stark_listar_heroes_por_dato_stark05(lista_heroes: list[dict], clave_a_evaluar: str):
  """
  La función `stark_listar_heroes_por_dato_stark05` recibe la lista de heroes y una clave para evaluar
  a partir de la clave a evaluar, analiza la lista para calcular la variedad de tipos para esa clave
  y que heroes coinciden con cada tipo
  guarda la informacion en un archivo .csv en la carpeta /csv
  :param lista_heroes: Una lista de diccionarios que representan diferentes héroes. Cada diccionario
  contiene información sobre un héroe, como su nombre, fuerza, inteligencia, etc.
  :param clave_a_evaluar: El parámetro "clave_a_evaluar" es un string que representa la clave o
  atributo del diccionario de héroes por el que se va a evaluar o filtrar la lista de héroes
  :return: un valor booleano. Si el archivo se guarda correctamente, devuelve True. De lo
  contrario, devuelve False.
  """
  set_clave_a_evaluar = obtener_lista_de_tipos(lista_heroes, clave_a_evaluar)
  heroes_por_tipo_segun_clave_a_evaluar = obtener_heroes_por_tipo_stark05(lista_heroes, set_clave_a_evaluar, clave_a_evaluar)
  archivo_guardado = guardar_heroes_por_tipo(heroes_por_tipo_segun_clave_a_evaluar, clave_a_evaluar)
  if archivo_guardado:
    return True
  else:
    return False

# extra
def generar_contenido_csv_lista_diccionarios(lista: list[dict]):
  contenido_csv = ",".join(lista[0].keys())
  contenido_csv += "\n"
  for diccionario in lista:
    contenido_csv += ",".join([str(value) for value in diccionario.values()])
    contenido_csv += "\n"
  return contenido_csv

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
  pass
  

# cd C:\Users\User\Desktop\utn\cuatrimestre1\programacion_1\ENTREGAS\stark\05
# python biblioteca_stark_05.py
# python main.py