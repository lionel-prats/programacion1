from biblioteca_stark_01 import(
  menu, find_by_fields, print_dict_list, max_key_value_in_dict_list, min_key_value_in_dict_list,
  format_value_in_numeric, get_average, proceed
)

def main_app(lista_personajes: list[dict]):
  """ 
  Ejecuta todo nuestro programa
  Recibe la lista de heroes 
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