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