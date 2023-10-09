"""
B - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
"""

def obtener_nombre(heroe: dict) -> str:
    """
    Obtiene el valor de la clave "nombre" del heroe.
    Recibe un diccionario que representa a un heroe.
    Retorna el nombre del heroe como un string.
    """
    nombre = heroe.get("nombre")
    return nombre

def imprimir_nombres_de_heroes(lista_heroes: list[dict]):
    for heroe in lista_heroes:
        # nombre = heroe.get("nombre")
        nombre = obtener_nombre(heroe)
        print(nombre)

# imprimir_nombres_de_heroes(lista_personajes)


"""
C - Recorrer la lista imprimiendo por consola nombre de cada 
superhéroe junto a la altura del mismo
"""

def imprimir_nombre_altura_de_heroes(lista_heroes: list[dict]):
    """
    TESTING
    The function "imprimir_nombre_altura_de_heroes" takes a list of dictionaries representing heroes,
    retrieves their names and heights, and prints them in a formatted message.
    
    :param lista_heroes: A list of dictionaries representing heroes. Each dictionary should have a
    "nombre" key for the hero's name and an "altura" key for the hero's height
    :type lista_heroes: list[dict]
    """
    for heroe in lista_heroes:
        nombre = obtener_nombre(heroe)
        altura = heroe.get("altura")
        mensaje = f'Nombre: {nombre} | Altura: {altura}'
        print(mensaje)

# imprimir_nombre_altura_de_heroes(lista_personajes)

"""
D - Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
"""

def determina_heroe_mas_alto(lista_heroes: list[dict]) -> dict:
    """
    Itera la lista de heroes determinando cual es el que posee mayor altura
    Recibe: la lista de heroes
    Retorna: el heroe de mayor estatura [como diccionario].
    """
    heroe_mas_alto = None

    for heroe in lista_heroes:
        if heroe_mas_alto == None or float(heroe_mas_alto.get("altura")) < float(heroe.get("altura")):
            heroe_mas_alto = heroe
    
    print(f"El heroe mas alto es {heroe_mas_alto.get('nombre')} y mide {heroe_mas_alto.get('altura')} mts")
    return heroe_mas_alto

def determina_heroe_mas_bajo(lista_heroes: list[dict]) -> dict:
  """
  The function `determina_heroe_mas_bajo` takes a list of dictionaries representing heroes and returns
  the hero with the shortest height.
  
  :param lista_heroes: A list of dictionaries, where each dictionary represents a hero. Each hero
  dictionary should have the following keys: "nombre" (name) and "altura" (height). The value of
  "altura" should be a float representing the height of the hero in centimeters
  :return: a dictionary that represents the shortest hero in the given list of heroes.
  """
  heroe_mas_bajo = None

  for heroe in lista_heroes:
      if heroe_mas_bajo == None or float(heroe_mas_bajo.get("altura")) > float(heroe.get("altura")):
          heroe_mas_bajo = heroe
  print(f"El heroe mas bajo es {heroe_mas_bajo.get('nombre')} y mide {heroe_mas_bajo.get('altura')} mts")
  return heroe_mas_bajo

def determinar_heroe_alto_bajo(lista_heroes: list[dict], modo: str) -> dict:
  """
  The function `determinar_heroe_alto_bajo` takes a list of dictionaries representing heroes and a
  mode ('max' or 'min') and returns the hero with the maximum or minimum height, respectively.
  
  :param lista_heroes: A list of dictionaries representing different heroes. Each dictionary should
  have the following keys: 'nombre' (name), 'altura' (height), and 'edad' (age)
  :type lista_heroes: list[dict]
  :param modo: The parameter "modo" is a string that determines the mode of operation. It can have two
  possible values: "max" or "min"
  :type modo: str
  :return: a dictionary that represents a hero.
  """
  heroe = {}
  if modo == 'max':
      heroe = determina_heroe_mas_alto(lista_heroes)
  elif modo == 'min':
      heroe = determina_heroe_mas_bajo(lista_heroes)
  return heroe

def determina_identidad_heroe_alto_bajo(lista_heroes: list[dict], modo: str):
  """
  The function `determina_identidad_heroe_alto_bajo` determines the identity of a hero based on their
  height and prints a message with the hero's identity.
  
  :param lista_heroes: A list of dictionaries representing different heroes. Each dictionary should
  have the following keys: "nombre" (name), "identidad" (identity), and "altura" (height)
  :type lista_heroes: list[dict]
  :param modo: The "modo" parameter is a string that determines whether we want to find the hero with
  the highest or lowest height. It can have two possible values: "alto" (high) or "bajo" (low)
  :type modo: str
  """
  heroe = determinar_heroe_alto_bajo(lista_heroes, modo)
  mensaje = f'su identidad es {heroe.get("identidad")}'
  print(mensaje)

# heroe_mas_alto = determina_heroe_mas_alto(lista_personajes)
# print(obtener_nombre(heroe_mas_alto))

def pedir_opcion_menu() -> str:
    return input("Elija una opcion: ")

def mostrar_menu() -> str:
    menu =\
    """
    1 - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
    2 - Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
    3 - Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
    4 - Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
    5 - Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
    6 - Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
    7 - Calcular e informar cual es el superhéroe más y menos pesado.
    8 - Salir
    """
    print(menu)
    return pedir_opcion_menu()