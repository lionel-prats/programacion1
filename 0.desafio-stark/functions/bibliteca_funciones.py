import os

def show_menu_00(lista_personajes: list[dict]):
  """  
  run the program of challenge #00\n 
  receive the list of heroes

  ejecuta el programa del desafío 00\n
  recibe la lista de superheroes
  """
  menu = \
  """
  1 - Recorrer la 4lista imprimiendo por consola el nombre de cada superhéroe
  2 - Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
  3 - Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
  4 - Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
  5 - Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
  6 - Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
  7 - Calcular e informar cual es el superhéroe más y menos pesado.
  8 - Salir
  """

  while True:
    print(menu)
    selected_option = input("Elija una opcion: ")
    match selected_option:
      # 1 - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
      case "1":
          heading = "1- Listado superhéroes (nombre):"
          filtered_heroes_list = find_by_fields(lista_personajes, ["nombre"])

          print_dict_list(filtered_heroes_list, heading)

          if proceed():
            print("\nHasta la próxima!\n")
            break

      # 2 - Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
      case "2":
          heading = "2- Listado superhéroes (nombre y altura):"
          filtered_heroes_list = find_by_fields(lista_personajes, ["nombre", "altura"])
          filtered_heroes_list = format_value_in_numeric(filtered_heroes_list, ["altura"], "float")

          print_dict_list(filtered_heroes_list, heading)

          if proceed():
            print("\nHasta la próxima!\n")
            break

      # 3 - Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
      case "3":
          heading = "3- Héroe/s más alto/s:"
          # genero una nueva lista con los valores "nombre" y "altura"
          filtered_heroes_list = find_by_fields(lista_personajes, ["nombre", "altura"])
          # formateo como float los valores "altura" y "peso"
          filtered_heroes_list = format_value_in_numeric(filtered_heroes_list, ["altura"], "float")
          # obtengo la altura maxima de toda la lista  
          max_height = max_key_value_in_dict_list(filtered_heroes_list, 'altura')
          # genero una lista con todos los heroes cuya altura coincida con la maxima
          list_heroes_max_height = [hero for hero in filtered_heroes_list if hero["altura"] == max_height]
          
          print(f"\n3- Altura máxima = {max_height}")
          print_dict_list(list_heroes_max_height, heading)

          if proceed():
            print("\nHasta la próxima!\n")
            break

      # 4 - Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
      case "4":
          heading = "4- Héroe/s más bajo/s:"
          filtered_heroes_list = find_by_fields(lista_personajes, ["nombre", "altura"])
          filtered_heroes_list = format_value_in_numeric(filtered_heroes_list, ["altura"], "float")
          min_height = min_key_value_in_dict_list(filtered_heroes_list, 'altura')
          list_heroes_min_height = [hero for hero in filtered_heroes_list if hero["altura"] == min_height]
          
          print(f"\n4- Altura mínima = {min_height}")
          print_dict_list(list_heroes_min_height, heading)

          if proceed():
            print("\nHasta la próxima!\n")
            break

      # 5 - Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
      case "5":
          
          formated_list = format_value_in_numeric(lista_personajes, ["altura"], "float")
          
          average = get_average(formated_list, "altura")
          print(f"\n5- Altura promedio = {average}\n")
          
          if proceed():
            print("\nHasta la próxima!\n")
            break

      # 6 - Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
      case "6":
          filtered_heroes_list = find_by_fields(lista_personajes, ["nombre", "altura"])
          filtered_heroes_list = format_value_in_numeric(filtered_heroes_list, ["altura"], "float")
          
          max_height = max_key_value_in_dict_list(filtered_heroes_list, 'altura')
          list_heroes_max_height = [hero for hero in filtered_heroes_list if hero["altura"] == max_height]

          min_height = min_key_value_in_dict_list(filtered_heroes_list, 'altura')
          list_heroes_min_height = [hero for hero in filtered_heroes_list if hero["altura"] == min_height]
          
          heading_1 = "6- Héroe/s más alto/s:"
          print_dict_list(list_heroes_max_height, heading_1)
          
          heading_2 = "6- Héroe/s más bajo/s:"
          print_dict_list(list_heroes_min_height, heading_2)

          if proceed():
            print("\nHasta la próxima!\n")
            break

      # 7 - Calcular e informar cual es el superhéroe más y menos pesado.
      case "7":
          filtered_heroes_list = find_by_fields(lista_personajes, ["nombre", "peso"])
          filtered_heroes_list = format_value_in_numeric(filtered_heroes_list, ["peso"], "float")
          
          max_weight = max_key_value_in_dict_list(filtered_heroes_list, 'peso')
          list_heroes_max_weight = [hero for hero in filtered_heroes_list if hero["peso"] == max_weight]

          min_weight = min_key_value_in_dict_list(filtered_heroes_list, 'peso')
          list_heroes_min_weight = [hero for hero in filtered_heroes_list if hero["peso"] == min_weight]
          
          heading_1 = "6- Héroe/s más pesado/s:"
          print_dict_list(list_heroes_max_weight, heading_1)
          
          heading_2 = "6- Héroe/s menos pesado/s:"
          print_dict_list(list_heroes_min_weight, heading_2)

          if proceed():
            print("\nHasta la próxima!\n")
            break

      case "8":
          print("\nHasta la próxima!\n")
          break
       
      case _:
              print("\n--------------------------\n")
              print("Opcion incorrecta, elija entre 1 y 9.")

def find_by_fields(list: list[dict], fields: list[str]) -> list[dict]:
    """  
    genera una nueva lista de diccionarios a partir de una recibida, prsisitiendo en los diccionarios las claves especificadas por el usuario\n
    recibe una lista de diccionarios y la lista de claves que deben persistir\n
    retorna una lista de diccionarios comprimidos respecto a los recibidos
    """
    new_list = [{field: dict[field] for field in fields} for dict in list]
    return new_list

def print_dict_list(list: list[dict], heading = None):
  """  
  imprime por consola un titulo (opcional) y un listado de diccionarios
  recibe un titulo (str - opcional) y una lista de diccionarios
  """
  if heading:
    print(f"\n{heading}\n")
  content = ""
  position = 1
  for dict in list: 
    content += f"{position}- "
    for k, v in dict.items():
      content += f"{k}: {v} | "
    content = content[:-3]
    content += "\n"
    position += 1
  print(content)
      
def max_key_value_in_dict_list(list: list[dict], key: str) -> float:
  """ 
  retorna el maximo valor en relacion a una clave especifica, de una lista de diccionarios
  recibe una lista de diccionarios y la clave a relevar (el tipo de dato debe ser int o float)
  """
  result = max(list, key = lambda item: item[key])[key]
  return result

def min_key_value_in_dict_list(list: list[dict], key: str) -> float:
  """ 
  retorna el minimo valor en relacion a una clave especifica, de una lista de diccionarios
  recibe una lista de diccionarios y la clave a relevar (el tipo de dato debe ser int o float)
  """
  result = min(list, key = lambda item: item[key])[key]
  return result

def format_value_in_numeric(list: list[dict], keys: list[str], type: str) -> list[dict]:
  """  
  castea como int o float valores de una lista de diccionarios que sean compatibles con estos formatos\n
  recibe la lista de diccionarios a formatear, las claves a castear en los diccionarios y el tipo de casteo
  """
  for item in list:
      for key in keys:
          if(type == "int"):
            item[key] = int(item[key])
          elif(type == "float"):
            item[key] = float(item[key])
  return list

def get_total(list: list[dict], k: str) -> float:
  """  
  calcula la suma de una determinada clave en una lista de diccionarios
  recibe una lista de diccionarios y la clave a relevar (el tipo de dato debe ser inn o float)
  retorna la suma de los valores de la clave especificada 
  """
  total = sum(item[k] for item in list)
  return total

def get_average(list: list[dict], k: str) -> float: 
  """  
  recorre una lista de diccionarios y calcula el promedio, a partir de una clave especificada
  recibe una lista de diccionarios y la clave a relevar (el tipo de dato debe ser inn o float)
  retorna el promedio de los valores de la clave especificada 
  """
  average = round(get_total(list, k) / len(list), 2) 
  return average

def select_by_field(lista: list[dict], key_value):
  
  key = list(key_value.keys())[0]
  value = key_value[key]

  result = list(filter(lambda el: el[key] == value, lista))
  return result


def proceed():
    """  
    valida si el usuario desea seguir ejecutando el programa luego de una consulta realizada\n
    recibe un determinado input por parte del usuario y en base a lo obtenido corta la ejecucion o permite que se siga ejecutando el programa
    """
    proceed = input("Quieres realizar una nueva consulta (s-n)? ").lower()
    while proceed != "s" and proceed != "n":
      proceed = input("Quieres realizar una nueva consulta (s-n)? ").lower()
    if proceed == "n":
      return True
    else:
      clear_console() 

def clear_console():
  """  
  limpia la consola
  """
  os.system('cls' if os.name == 'nt' else 'clear')