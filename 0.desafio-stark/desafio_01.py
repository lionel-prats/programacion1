from functions.bibliteca_funciones import *

def show_menu_01(lista_personajes: list[dict]):
  """  
  ejecuta el programa del desafío 01\n
  recibe la lista de superheroes
  """
  menu = \
  """
  A Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
  B Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
  C Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
  D Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
  E Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
  F Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
  G Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
  H Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
  I Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
  J Determinar cuántos superhéroes tienen cada tipo de color de ojos.
  K Determinar cuántos superhéroes tienen cada tipo de color de pelo.
  L Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
  M Listar todos los superhéroes agrupados por color de ojos.
  N Listar todos los superhéroes agrupados por color de pelo.
  O Listar todos los superhéroes agrupados por tipo de inteligencia
  Q Salir
  """
  while True:
    print(menu)
    selected_option = input("Elija una opcion: ")
    match selected_option:
      # A Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
      case "a" | "A":
        heading = "1- Listado heroínas:"
        list_heroines = select_by_field(lista_personajes, {"genero": "M"})
        compressed_list = find_by_fields()
        print_dict_list(heroines, heading)

        if proceed():
          print("\nHasta la próxima!\n")
          break

      # B Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
      case "b" | "B":
        print("B")
        # heading = "2- Listado superhéroes (nombre y altura):"
        # filtered_heroes_list = find_by_fields(lista_personajes, ["nombre", "altura"])
        # filtered_heroes_list = format_value_in_numeric(filtered_heroes_list, ["altura"], "float")

        # print_dict_list(filtered_heroes_list, heading)

        if proceed():
          print("\nHasta la próxima!\n")
          break

      # C Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
      case "c" | "C":
        print("C")
        # heading = "3- Héroe/s más alto/s:"
        # # genero una nueva lista con los valores "nombre" y "altura"
        # filtered_heroes_list = find_by_fields(lista_personajes, ["nombre", "altura"])
        # # formateo como float los valores "altura" y "peso"
        # filtered_heroes_list = format_value_in_numeric(filtered_heroes_list, ["altura"], "float")
        # # obtengo la altura maxima de toda la lista  
        # max_height = max_key_value_in_dict_list(filtered_heroes_list, 'altura')
        # # genero una lista con todos los heroes cuya altura coincida con la maxima
        # list_heroes_max_height = [hero for hero in filtered_heroes_list if hero["altura"] == max_height]
        
        # print(f"\n3- Altura máxima = {max_height}")
        # print_dict_list(list_heroes_max_height, heading)

        if proceed():
          print("\nHasta la próxima!\n")
          break

      # D Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
      case "d" | "D":
        print("D")
        # heading = "4- Héroe/s más bajo/s:"
        # filtered_heroes_list = find_by_fields(lista_personajes, ["nombre", "altura"])
        # filtered_heroes_list = format_value_in_numeric(filtered_heroes_list, ["altura"], "float")
        # min_height = min_key_value_in_dict_list(filtered_heroes_list, 'altura')
        # list_heroes_min_height = [hero for hero in filtered_heroes_list if hero["altura"] == min_height]
        
        # print(f"\n4- Altura mínima = {min_height}")
        # print_dict_list(list_heroes_min_height, heading)

        if proceed():
          print("\nHasta la próxima!\n")
          break

      # E Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M
      case "e" | "E":
        print("E")
        
        # formated_list = format_value_in_numeric(lista_personajes, ["altura"], "float")
        
        # average = get_average(formated_list, "altura")
        # print(f"\n5- Altura promedio = {average}\n")
        
        if proceed():
          print("\nHasta la próxima!\n")
          break

      # F Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F
      case "f" | "F":
        print("F")
        # filtered_heroes_list = find_by_fields(lista_personajes, ["nombre", "altura"])
        # filtered_heroes_list = format_value_in_numeric(filtered_heroes_list, ["altura"], "float")
        
        # max_height = max_key_value_in_dict_list(filtered_heroes_list, 'altura')
        # list_heroes_max_height = [hero for hero in filtered_heroes_list if hero["altura"] == max_height]

        # min_height = min_key_value_in_dict_list(filtered_heroes_list, 'altura')
        # list_heroes_min_height = [hero for hero in filtered_heroes_list if hero["altura"] == min_height]
        
        # heading_1 = "6- Héroe/s más alto/s:"
        # print_dict_list(list_heroes_max_height, heading_1)
        
        # heading_2 = "6- Héroe/s más bajo/s:"
        # print_dict_list(list_heroes_min_height, heading_2)

        if proceed():
          print("\nHasta la próxima!\n")
          break

      # G Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
      case "g" | "G":
        print("G")
        # filtered_heroes_list = find_by_fields(lista_personajes, ["nombre", "peso"])
        # filtered_heroes_list = format_value_in_numeric(filtered_heroes_list, ["peso"], "float")
        
        # max_weight = max_key_value_in_dict_list(filtered_heroes_list, 'peso')
        # list_heroes_max_weight = [hero for hero in filtered_heroes_list if hero["peso"] == max_weight]

        # min_weight = min_key_value_in_dict_list(filtered_heroes_list, 'peso')
        # list_heroes_min_weight = [hero for hero in filtered_heroes_list if hero["peso"] == min_weight]
        
        # heading_1 = "6- Héroe/s más pesado/s:"
        # print_dict_list(list_heroes_max_weight, heading_1)
        
        # heading_2 = "6- Héroe/s menos pesado/s:"
        # print_dict_list(list_heroes_min_weight, heading_2)

        if proceed():
          print("\nHasta la próxima!\n")
          break

      # H Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
      case "h" | "H":
        print("H")
        if proceed():
          print("\nHasta la próxima!\n")
          break

      # I Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
      case "i" | "I":
        print("I")
        if proceed():
          print("\nHasta la próxima!\n")
          break
      # J Determinar cuántos superhéroes tienen cada tipo de color de ojos.
      case "j" | "J":
        print("J")
        if proceed():
          print("\nHasta la próxima!\n")
          break
      # K Determinar cuántos superhéroes tienen cada tipo de color de pelo.
      case "k" | "K":
        print("K")
        if proceed():
          print("\nHasta la próxima!\n")
          break
      # L Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
      case "l" | "L":
        print("L")
        if proceed():
          print("\nHasta la próxima!\n")
          break
      # M Listar todos los superhéroes agrupados por color de ojos.
      case "m" | "M":
        print("M")
        if proceed():
          print("\nHasta la próxima!\n")
          break
      # N Listar todos los superhéroes agrupados por color de pelo.
      case "n" | "N":
        print("N")
        if proceed():
          print("\nHasta la próxima!\n")
          break
      # O Listar todos los superhéroes agrupados por tipo de inteligencia
      case "o" | "O":
        print("O")
        if proceed():
          print("\nHasta la próxima!\n")
          break

      # salir
      case "q" | "Q":
          print("\nHasta la próxima!\n")
          break
       
      case _:
              print("\n--------------------------\n")
              print("Opcion incorrecta, elija entre a|A y o|O o q|Q.")