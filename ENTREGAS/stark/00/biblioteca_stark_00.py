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
l - Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’)
m - Listar todos los superhéroes agrupados por color de ojos.
n - Listar todos los superhéroes agrupados por color de pelo.
o - Listar todos los superhéroes agrupados por tipo de inteligencia
  """
}

texto_default = "Elija una opcion entre 1 y 7 o presione q para salir: "

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
  print(menu["desafio_00"])
  
def continuar(input_usuario: str) -> bool:
  """  
  valida si el usuario desea realizar una nueva consulta\n
  recibe un input del usuario: "c" para realizar una consulta o "q" para salir del programa\n
  retorna True si "c" o False si "n"
  """
  while input_usuario != "1" and input_usuario != "2" and input_usuario != "3" and input_usuario != "4" and input_usuario != "5" and input_usuario != "6" and input_usuario != "7" and input_usuario != "q":
    mostrar_menu()
    input_usuario = input(texto_default).lower()
  if input_usuario == "q":
    limpiar_consola()
    return False
  return input_usuario

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
  pass  

# python biblioteca_stark_00.py