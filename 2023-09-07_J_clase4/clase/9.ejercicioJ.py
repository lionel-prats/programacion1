""" 
Alumno: Lionel Prats 
DNI: 31367577
División: 1H
Nro. legajo: 115678
Desafío 00_Stark
"""

import os

lista_personajes =\
[
  {
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
  },
  {
    "nombre": "Rocket Raccoon",
    "identidad": "Rocket Raccoon",
    "empresa": "Marvel Comics",
    "altura": "122.77",
    "peso": "25.73",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Brown",
    "fuerza": "5",
    "inteligencia": "average"
  },
  {
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
  },
  {
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
  },
  {
    "nombre": "Mystique",
    "identidad": "Raven Darkholme",
    "empresa": "Marvel Comics",
    "altura": "178.65000000000001",
    "peso": "54.960000000000001",
    "genero": "F",
    "color_ojos": "Yellow (without irises)",
    "color_pelo": "Red / Orange",
    "fuerza": "15",
    "inteligencia": "good"
  },
  {
    "nombre": "Spider-Man",
    "identidad": "Peter Parker",
    "empresa": "Marvel Comics",
    "altura": "178.28",
    "peso": "74.25",
    "genero": "M",
    "color_ojos": "Hazel",
    "color_pelo": "Brown",
    "fuerza": "55",
    "inteligencia": "high"
  },
  {
    "nombre": "Storm",
    "identidad": "Ororo Munroe",
    "empresa": "Marvel Comics",
    "altura": "180.72",
    "peso": "57.5",
    "genero": "F",
    "color_ojos": "Blue",
    "color_pelo": "White",
    "fuerza": "10",
    "inteligencia": "good"
  },
  {
    "nombre": "Gamora",
    "identidad": "Gamora Zen Whoberi Ben Titan",
    "empresa": "Marvel Comics",
    "altura": "183.65000000000001",
    "peso": "77.769999999999996",
    "genero": "F",
    "color_ojos": "Yellow",
    "color_pelo": "Black",
    "fuerza": "85",
    "inteligencia": "good"
  },
  {
    "nombre": "Thing",
    "identidad": "Ben Grimm",
    "empresa": "Marvel Comics",
    "altura": "183.55000000000001",
    "peso": "225.41999999999999",
    "genero": "M",
    "color_ojos": "Blue",
    "color_pelo": "No Hair",
    "fuerza": "85",
    "inteligencia": "good"
  },
  {
    "nombre": "Thor",
    "identidad": "Thor Odinson",
    "empresa": "Marvel Comics",
    "altura": "198.34999999999999",
    "peso": "288.61000000000001",
    "genero": "M",
    "color_ojos": "Blue",
    "color_pelo": "Blond",
    "fuerza": "100",
    "inteligencia": "good"
  },
  {
    "nombre": "Colossus",
    "identidad": "Piotr Nikolaievitch Rasputin",
    "empresa": "Marvel Comics",
    "altura": "226.13",
    "peso": "225.52000000000001",
    "genero": "M",
    "color_ojos": "Silver",
    "color_pelo": "Black",
    "fuerza": "85",
    "inteligencia": "good"
  },
  {
    "nombre": "Hulk",
    "identidad": "Bruce Banner",
    "empresa": "Marvel Comics",
    "altura": "244.40000000000001",
    "peso": "630.89999999999998",
    "genero": "M",
    "color_ojos": "Green",
    "color_pelo": "Green",
    "fuerza": "100",
    "inteligencia": "high"
  },
  {
    "nombre": "Groot",
    "identidad": "Groot",
    "empresa": "Marvel Comics",
    "altura": "701.12",
    "peso": "4.8200000000000003",
    "genero": "M",
    "color_ojos": "Yellow",
    "color_pelo": "",
    "fuerza": "85",
    "inteligencia": "good"
  },
  {
    "nombre": "Daredevil",
    "identidad": "Matt Murdock",
    "empresa": "Marvel Comics",
    "altura": "183.68000000000001",
    "peso": "90.450000000000003",
    "genero": "M",
    "color_ojos": "Blue",
    "color_pelo": "Red",
    "fuerza": "15",
    "inteligencia": "good"
  },
  {
    "nombre": "Nick Fury",
    "identidad": "Nicholas Joseph Fury",
    "empresa": "Marvel Comics",
    "altura": "185.88",
    "peso": "99.280000000000001",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Brown / White",
    "fuerza": "15",
    "inteligencia": "good"
  },
  {
    "nombre": "Punisher",
    "identidad": "Frank Castle",
    "empresa": "Marvel Comics",
    "altura": "183.25999999999999",
    "peso": "90.900000000000006",
    "genero": "M",
    "color_ojos": "Blue",
    "color_pelo": "Black",
    "fuerza": "20",
    "inteligencia": "good"
  },
  {
    "nombre": "Star-Lord",
    "identidad": "Peter Jason Quill",
    "empresa": "Marvel Comics",
    "altura": "188.25",
    "peso": "79.209999999999994",
    "genero": "M",
    "color_ojos": "Blue",
    "color_pelo": "Blond",
    "fuerza": "20",
    "inteligencia": "good"
  },
  {
    "nombre": "Deadpool",
    "identidad": "Wade Wilson",
    "empresa": "Marvel Comics",
    "altura": "188.0",
    "peso": "95.319999999999993",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "No Hair",
    "fuerza": "35",
    "inteligencia": "good"
  },
  {
    "nombre": "Captain America",
    "identidad": "Steve Rogers",
    "empresa": "Marvel Comics",
    "altura": "188.00999999999999",
    "peso": "108.94",
    "genero": "M",
    "color_ojos": "blue",
    "color_pelo": "blond",
    "fuerza": "20",
    "inteligencia": "good"
  },
  {
    "nombre": "Ghost Rider",
    "identidad": "Johnny Blaze",
    "empresa": "Marvel Comics",
    "altura": "188.50999999999999",
    "peso": "99.200000000000003",
    "genero": "M",
    "color_ojos": "Red",
    "color_pelo": "No Hair",
    "fuerza": "55",
    "inteligencia": "average"
  },
  {
    "nombre": "Blade",
    "identidad": "Eric Brooks",
    "empresa": "Marvel Comics",
    "altura": "188.44999999999999",
    "peso": "97.400000000000006",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Black",
    "fuerza": "30",
    "inteligencia": "good"
  },
  {
    "nombre": "Hawkeye",
    "identidad": "Clint Barton",
    "empresa": "Marvel Comics",
    "altura": "191.00999999999999",
    "peso": "104.93000000000001",
    "genero": "M",
    "color_ojos": "Blue",
    "color_pelo": "Blond",
    "fuerza": "15",
    "inteligencia": "average"
  },
  {
    "nombre": "Drax the Destroyer",
    "identidad": "Arthur Sampson Douglas",
    "empresa": "Marvel Comics",
    "altura": "193.00999999999999",
    "peso": "306.42000000000002",
    "genero": "M",
    "color_ojos": "Red",
    "color_pelo": "No Hair",
    "fuerza": "80",
    "inteligencia": "average"
  },
  {
    "nombre": "Iron Man",
    "identidad": "Tony Stark",
    "empresa": "Marvel Comics",
    "altura": "198.91",
    "peso": "191.88",
    "genero": "M",
    "color_ojos": "Blue",
    "color_pelo": "Black",
    "fuerza": "85",
    "inteligencia": "high"
  }
]

def show_menu(lista_heroes: list[dict]):
  """  
  run the program\n 
  receive the list of heroes

  ejecuta el programa\n
  recibe la lista de superheroes
  """
  menu = \
  """
  1 - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
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

# App 
show_menu(lista_personajes)