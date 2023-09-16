from biblioteca_stark_01 import(
  texto_default, reducir_diccionarios_en_lista, imprimir_lista_de_diccionarios, valor_maximo_propiedad_en_lista_de_diccionarios, valor_minimo_propiedad_en_lista_de_diccionarios, filtrar_por_clave, formatear_valores_diccionario_a_numericos, obtener_promedio, limpiar_consola, continuar, mostrar_menu
)

# funcion principal de la aplicacion
def main_app(lista_personajes: list[dict]):
  """ 
  ejecuta todo nuestro programa\n
  recibe la lista de heroes 
  """
  inicio = True
  while True:
    mostrar_menu()
    if inicio:
      inicio = False
      opcion_seleccionada = input(texto_default)
    else:
      opcion_seleccionada = input_continuar

    match opcion_seleccionada:
      # a - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
      case "a" | "A":
        print(opcion_seleccionada)

        input_continuar = continuar(input(texto_default).lower())
        if not input_continuar:
          break
      # 2 - Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
      case "2":
        titulo = "2- Listado superhéroes (nombre y altura):"
        
        lista_heroes_nombre_altura = reducir_diccionarios_en_lista(lista_personajes, ["nombre", "altura"])
        formatear_valores_diccionario_a_numericos(lista_heroes_nombre_altura, ["altura"], "float") # aplico el formateo para que en la impresion por consola, la parte decimal de "altura" se redondee y reduza a 2 digitos

        imprimir_lista_de_diccionarios(lista_heroes_nombre_altura, titulo)

        input_continuar = continuar(input(texto_default).lower())
        if not input_continuar:
          break
      # 3 - Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
      case "3":

        # si el usuario elije (por ejemplo) la opcion "2" primero lista_heroes_nombre_altura queda cargado en memoria, si luego desea continuar y acto seguido elije la opcion "3", aca esta la demostracion de lo dicho anteriormente, y no esta bien porque la memoria deberia limpiarse ante una nueva ejecucion de una opcion para no saturarla
        # print(lista_heroes_nombre_altura)
        # exit()

        titulo = "3- Héroe/s más alto/s:"
        lista_heroes_nombre_altura = reducir_diccionarios_en_lista(lista_personajes, ["nombre", "altura"]) 
        formatear_valores_diccionario_a_numericos(lista_heroes_nombre_altura, ["altura"], "float")
        altura_maxima = valor_maximo_propiedad_en_lista_de_diccionarios(lista_heroes_nombre_altura, 'altura')
        lista_heroes_altura_maxima = filtrar_por_clave(lista_heroes_nombre_altura, "altura", altura_maxima)
        print(f"\n3- Altura máxima = {altura_maxima}")
        imprimir_lista_de_diccionarios(lista_heroes_altura_maxima, titulo)

        input_continuar = continuar(input(texto_default).lower())
        if not input_continuar:
          break
      # 4 - Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
      case "4":
        titulo = "4- Héroe/s más bajo/s:"
        lista_heroes_nombre_altura = reducir_diccionarios_en_lista(lista_personajes, ["nombre", "altura"])
        formatear_valores_diccionario_a_numericos(lista_heroes_nombre_altura, ["altura"], "float")
        altura_minima = valor_minimo_propiedad_en_lista_de_diccionarios(lista_heroes_nombre_altura, 'altura')
        lista_heroes_altura_minima = filtrar_por_clave(lista_heroes_nombre_altura, "altura", altura_minima)
        
        print(f"\n4- Altura mínima = {altura_minima}")
        imprimir_lista_de_diccionarios(lista_heroes_altura_minima, titulo)

        input_continuar = continuar(input(texto_default).lower())
        if not input_continuar:
          break
      # 5 - Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
      case "5":
        lista_heroes_altura = formatear_valores_diccionario_a_numericos(lista_personajes, ["altura"], "float")
        altura_promedio = obtener_promedio(lista_heroes_altura, "altura")
        print(f"\n5- Altura promedio = {altura_promedio}\n")

        input_continuar = continuar(input(texto_default).lower())
        if not input_continuar:
          break
      # 6 - Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
      case "6":
        lista_heroes_nombre_altura = reducir_diccionarios_en_lista(lista_personajes, ["nombre", "altura"])
        lista_heroes_nombre_altura = formatear_valores_diccionario_a_numericos(lista_heroes_nombre_altura, ["altura"], "float")
        altura_maxima = valor_maximo_propiedad_en_lista_de_diccionarios(lista_heroes_nombre_altura, 'altura')
        lista_heroes_altura_maxima = [hero for hero in lista_heroes_nombre_altura if hero["altura"] == altura_maxima]
        altura_minima = valor_minimo_propiedad_en_lista_de_diccionarios(lista_heroes_nombre_altura, 'altura')
        lista_heroes_altura_minima = [hero for hero in lista_heroes_nombre_altura if hero["altura"] == altura_minima]
        titulo_mas_alto = "6- Héroe/s más alto/s:"
        titulo_mas_bajo = "6- Héroe/s más bajo/s:"
        imprimir_lista_de_diccionarios(lista_heroes_altura_maxima, titulo_mas_alto)
        imprimir_lista_de_diccionarios(lista_heroes_altura_minima, titulo_mas_bajo)

        input_continuar = continuar(input(texto_default).lower())
        if not input_continuar:
          break
      # 7 - Calcular e informar cual es el superhéroe más y menos pesado.
      case "7":
        lista_heroes_nombre_peso = reducir_diccionarios_en_lista(lista_personajes, ["nombre", "peso"])
        lista_heroes_nombre_peso = formatear_valores_diccionario_a_numericos(lista_heroes_nombre_peso, ["peso"], "float")
        
        peso_maximo = valor_maximo_propiedad_en_lista_de_diccionarios(lista_heroes_nombre_peso, 'peso')
        lista_heroes_peso_maximo = [hero for hero in lista_heroes_nombre_peso if hero["peso"] == peso_maximo]

        peso_minimo = valor_minimo_propiedad_en_lista_de_diccionarios(lista_heroes_nombre_peso, 'peso')
        lista_heroes_peso_minimo = [hero for hero in lista_heroes_nombre_peso if hero["peso"] == peso_minimo]
        
        titulo_mas_pesado = "7- Héroe/s más pesado/s:"
        titulo_menos_pesado = "7- Héroe/s menos pesado/s:"
        
        imprimir_lista_de_diccionarios(lista_heroes_peso_maximo, titulo_mas_pesado)
        imprimir_lista_de_diccionarios(lista_heroes_peso_minimo, titulo_menos_pesado)

        input_continuar = continuar(input(texto_default).lower())
        if not input_continuar:
          break

      # salir del programa
      case "q":
        limpiar_consola()
        break
      case _:
        limpiar_consola()
        inicio = True