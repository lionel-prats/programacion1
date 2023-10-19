def stark_marvel_app_5(lista_personajes):
    """
    """
    opcion_seleccionada = -1
    while opcion_seleccionada == -1:
        limpiar_consola()
        opcion_seleccionada = stark_menu_principal_desafio_5() 
        
    match opcion_seleccionada:
        # a - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
        case "a" | "A":
            pass
            stark_imprimir_heroe_genero(lista_personajes, "m")
            # input_continuar = continuar(input(texto_default))
            # if not input_continuar:
            # break
        # b - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
        case "b" | "B":
            pass
            # stark_imprimir_heroe_genero(lista_personajes, "f")
            # input_continuar = continuar(input(texto_default))
            # if not input_continuar:
            # break
        # c - Recorrer la lista y determinar cuál es el superhéroe más alto de género M
        case "c" | "C":
            pass
            # stark_calcular_imprimir_heroe_genero(lista_personajes, "maximo", "altura", "M", True)
            # input_continuar = continuar(input(texto_default))
            # if not input_continuar:
            # break
        # e - Recorrer la lista y determinar cuál es el superhéroe más alto de género F
        case "d" | "D":
            pass
            # stark_calcular_imprimir_heroe_genero(lista_personajes, "maximo", "altura", "F", True)
            # input_continuar = continuar(input(texto_default))
            # if not input_continuar:
            # break
        # e - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M
        case "e" | "E":
            pass
            # stark_calcular_imprimir_heroe_genero(lista_personajes, "minimo", "altura", "M", True)
            # input_continuar = continuar(input(texto_default))
            # if not input_continuar:
            # break
        # f - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F
        case "f" | "F":
            pass
            # stark_calcular_imprimir_heroe_genero(lista_personajes, "minimo", "altura", "F", True)
            # input_continuar = continuar(input(texto_default))
            # if not input_continuar:
            # break
        # g - Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
        case "g" | "G":
            pass
            # stark_calcular_imprimir_promedio_altura_genero(lista_personajes, "altura", "m")
            # input_continuar = continuar(input(texto_default))
            # if not input_continuar:
            # break
        # h - Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
        case "h" | "H":
            pass
            # stark_calcular_imprimir_promedio_altura_genero(lista_personajes, "altura", "f")
            # input_continuar = continuar(input(texto_default))
            # if not input_continuar:
            # break
        # i - Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
        case "i" | "I":
            pass
            # titulo = "- Héroe/s más alto/s género \"M\":"
            # print(f"\n{titulo}")
            # stark_calcular_imprimir_heroe_genero(lista_personajes, "maximo", "altura", "M")

            # titulo = "- Héroe/s más alto/s género \"F\":"
            # print(titulo)
            # stark_calcular_imprimir_heroe_genero(lista_personajes, "maximo", "altura", "F")

            # titulo = "- Héroe/s más bajo/s género \"M\":"
            # print(titulo)
            # stark_calcular_imprimir_heroe_genero(lista_personajes, "minimo", "altura", "M")

            # titulo = "- Héroe/s más bajo/s género \"F\":"
            # print(titulo)
            # stark_calcular_imprimir_heroe_genero(lista_personajes, "minimo", "altura", "F")

            # input_continuar = continuar(input(texto_default))
            # if not input_continuar:
            # break
        # j - Determinar cuántos superhéroes tienen cada tipo de color de ojos.
        case "j" | "J":
            pass
            # stark_calcular_cantidad_por_tipo(lista_personajes, "color_ojos")
            # input_continuar = continuar(input(texto_default))
            # if not input_continuar:
            # break
        # k - Determinar cuántos superhéroes tienen cada tipo de color de pelo.
        case "k" | "K":
            pass
            # stark_calcular_cantidad_por_tipo(lista_personajes, "color_pelo")
            # input_continuar = continuar(input(texto_default))
            # if not input_continuar:
            # break
        # l - Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con "No Tiene")
        case "l" | "L":
            pass
            # stark_calcular_cantidad_por_tipo(lista_personajes, "inteligencia")
            # input_continuar = continuar(input(texto_default))
            # if not input_continuar:
            # break
        # m - Listar todos los superhéroes agrupados por color de ojos.
        case "m" | "M":
            pass
            # stark_listar_heroes_por_dato(lista_personajes, "color_ojos")
            # input_continuar = continuar(input(texto_default))
            # if not input_continuar:
            # break

        # n - Listar todos los superhéroes agrupados por color de pelo.
        case "n" | "N":
            pass
            # stark_listar_heroes_por_dato(lista_personajes, "color_pelo")
            # input_continuar = continuar(input(texto_default))
            # if not input_continuar:
            # break

        # o - Listar todos los superhéroes agrupados por tipo de inteligencia
        case "o" | "O":
            pass
            # stark_listar_heroes_por_dato(lista_personajes, "inteligencia")
            # input_continuar = continuar(input(texto_default))
            # if not input_continuar:
            # break

        # salir del programa
        case "q":
            pass
            limpiar_consola()
            # break

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
    menu = """a - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
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

1.5
def guardar_archivo():
   """
    Crear la función 'guardar_archivo' la cual recibirá por parámetro un string que indicará el nombre con el cual se guardará el archivo junto con su extensión (ejemplo: 'archivo.csv') y como segundo parámetro tendrá un string el cual será el contenido a guardar en dicho archivo. Debe abrirse el archivo en modo escritura, ya que en caso de no existir, lo creara y en caso de existir, lo va a sobreescribir La función debera retornar True si no hubo errores, caso contrario False, además en caso de éxito, deberá imprimir un mensaje respetando el formato:
    .Se creó el archivo: nombre_archivo.csv
    En caso de retornar False, el mensaje deberá decir: ‘Error al crear el archivo: nombre_archivo’
    Donde nombre_archivo será el nombre que recibirá el archivo a ser creado, conjuntamente con su extensión. (Manejar posibles Excepciones)
    """ 
   pass

# --------------------------------- BLOQUE DE FUNCIONES STARKS ANTERIORES - INICIO ---------------------------------------

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
  print("\n")
  for heroe in heroes_genero:
    imprimir_dato(obtener_nombre(heroe))
  print("\n")

# --------------------------------- BLOQUE DE FUNCIONES STARKS ANTERIORES - FIN ---------------------------------------

def imprimir_dato(string: str):
  """  
  recibe un string y lo imprime por consola\n 
  [string: str] -> string a imprimir\n
  return None
  """
  print(string)

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

# -----------------------------

if __name__ == "__main__":
    limpiar_consola()
    lista_heroes = leer_archivo("data_stark.json")
    stark_marvel_app_5(lista_heroes)

# cd C:\Users\User\Desktop\utn\cuatrimestre1\programacion_1\ENTREGAS\stark\05
# python biblioteca_stark_05.py
# python main.py
