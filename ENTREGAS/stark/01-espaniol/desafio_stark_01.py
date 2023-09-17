from biblioteca_stark_01 import(
  texto_default, reducir_diccionarios_en_lista, imprimir_lista_de_diccionarios, valor_maximo_propiedad_en_lista_de_diccionarios, valor_minimo_propiedad_en_lista_de_diccionarios, filtrar_por_clave, formatear_valores_diccionario_a_numericos, obtener_promedio, limpiar_consola, continuar, mostrar_menu, cantidad_valores_segun_clave, imprimir_diccionario_formato_tabla, listado_de_valores_existentes_segun_clave, imprimir_lista_diccionarios_agrupando_segun_clave
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
        titulo = "a - Lista de superheroes genero M:"
        lista_heroes_genero_m = filtrar_por_clave(lista_personajes, "genero", "M")
        imprimir_lista_de_diccionarios(reducir_diccionarios_en_lista(lista_heroes_genero_m, ["nombre"]), titulo)
        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break
      # b - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
      case "b" | "B":
        titulo = "b - Lista de superheroes genero F:"
        lista_heroes_genero_f = filtrar_por_clave(lista_personajes, "genero", "F")
        imprimir_lista_de_diccionarios(reducir_diccionarios_en_lista(lista_heroes_genero_f, ["nombre"]), titulo)

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break
      # c - Recorrer la lista y determinar cuál es el superhéroe más alto de género M
      case "c" | "C":
        titulo = "c - Héroe/s más alto/s género \"M\":"
        lista_heroes_genero_m = filtrar_por_clave(lista_personajes, "genero", "M")
        formatear_valores_diccionario_a_numericos(lista_heroes_genero_m, ["altura"], "float")
        altura_maxima = valor_maximo_propiedad_en_lista_de_diccionarios(lista_heroes_genero_m, 'altura')
        lista_heroes_M_altura_maxima = filtrar_por_clave(lista_heroes_genero_m, "altura", altura_maxima)
        imprimir_lista_de_diccionarios(reducir_diccionarios_en_lista(lista_heroes_M_altura_maxima, ["nombre", "genero", "altura"]), titulo)
        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break
      # e - Recorrer la lista y determinar cuál es el superhéroe más alto de género F
      case "d" | "D":
        titulo = "d - Héroe/s más alto/s género \"F\":"
        lista_heroes_genero_F = filtrar_por_clave(lista_personajes, "genero", "F")
        formatear_valores_diccionario_a_numericos(lista_heroes_genero_F, ["altura"], "float")
        altura_maxima = valor_maximo_propiedad_en_lista_de_diccionarios(lista_heroes_genero_F, 'altura')
        lista_heroes_M_altura_maxima = filtrar_por_clave(lista_heroes_genero_F, "altura", altura_maxima)
        imprimir_lista_de_diccionarios(reducir_diccionarios_en_lista(lista_heroes_M_altura_maxima, ["nombre", "genero", "altura"]), titulo)
        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # e - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M
      case "e" | "E":
        titulo = "e - Héroe/s más bajo/s género \"M\":"
        lista_heroes_genero_m = filtrar_por_clave(lista_personajes, "genero", "M")
        formatear_valores_diccionario_a_numericos(lista_heroes_genero_m, ["altura"], "float")
        altura_minima = valor_minimo_propiedad_en_lista_de_diccionarios(lista_heroes_genero_m, 'altura')
        lista_heroes_M_altura_minima = filtrar_por_clave(lista_heroes_genero_m, "altura", altura_minima)
        imprimir_lista_de_diccionarios(reducir_diccionarios_en_lista(lista_heroes_M_altura_minima, ["nombre", "genero", "altura"]), titulo)

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # f - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F
      case "f" | "F":
        titulo = "f - Héroe/s más bajo/s género \"F\":"
        lista_heroes_genero_F = filtrar_por_clave(lista_personajes, "genero", "F")
        formatear_valores_diccionario_a_numericos(lista_heroes_genero_F, ["altura"], "float")
        altura_minima = valor_minimo_propiedad_en_lista_de_diccionarios(lista_heroes_genero_F, 'altura')
        lista_heroes_F_altura_minima = filtrar_por_clave(lista_heroes_genero_F, "altura", altura_minima)
        imprimir_lista_de_diccionarios(reducir_diccionarios_en_lista(lista_heroes_F_altura_minima, ["nombre", "genero", "altura"]), titulo)

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # g - Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
      case "g" | "G":
        lista_heroes_genero_M = filtrar_por_clave(lista_personajes, "genero", "M")
        formatear_valores_diccionario_a_numericos(lista_heroes_genero_M, ["altura"], "float")
        altura_promedio_genero_M = obtener_promedio(lista_heroes_genero_M, "altura")
        print(f"\ng - La altura promedio de los héroes de genero M es: {altura_promedio_genero_M}\n")

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # h - Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
      case "h" | "H":

        lista_heroes_genero_F = filtrar_por_clave(lista_personajes, "genero", "F")
        formatear_valores_diccionario_a_numericos(lista_heroes_genero_F, ["altura"], "float")
        altura_promedio_genero_F = obtener_promedio(lista_heroes_genero_F, "altura")
        print(f"\nh - La altura promedio de los héroes de genero F es: {altura_promedio_genero_F}\n")

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # i - Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
      case "i" | "I":
       
        print("\ni - Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F):")

        titulo = "* Héroe/s más alto/s género \"M\":"
        lista_heroes_segun_genero = filtrar_por_clave(lista_personajes, "genero", "M")
        formatear_valores_diccionario_a_numericos(lista_heroes_segun_genero, ["altura"], "float")
        altura_buscada = valor_maximo_propiedad_en_lista_de_diccionarios(lista_heroes_segun_genero, 'altura')
        lista_heroes_altura_buscada_segun_genero = filtrar_por_clave(lista_heroes_segun_genero, "altura", altura_buscada)
        imprimir_lista_de_diccionarios(reducir_diccionarios_en_lista(lista_heroes_altura_buscada_segun_genero, ["nombre", "genero", "altura"]), titulo)

        titulo = "* Héroe/s más alto/s género \"F\":"
        lista_heroes_segun_genero = filtrar_por_clave(lista_personajes, "genero", "F")
        formatear_valores_diccionario_a_numericos(lista_heroes_segun_genero, ["altura"], "float")
        altura_buscada = valor_maximo_propiedad_en_lista_de_diccionarios(lista_heroes_segun_genero, 'altura')
        lista_heroes_altura_buscada_segun_genero = filtrar_por_clave(lista_heroes_segun_genero, "altura", altura_buscada)
        imprimir_lista_de_diccionarios(reducir_diccionarios_en_lista(lista_heroes_altura_buscada_segun_genero, ["nombre", "genero", "altura"]), titulo)

        titulo = "* Héroe/s más bajo/s género \"M\":"
        lista_heroes_segun_genero = filtrar_por_clave(lista_personajes, "genero", "M")
        formatear_valores_diccionario_a_numericos(lista_heroes_segun_genero, ["altura"], "float")
        altura_buscada = valor_minimo_propiedad_en_lista_de_diccionarios(lista_heroes_segun_genero, 'altura')
        lista_heroes_altura_buscada_segun_genero = filtrar_por_clave(lista_heroes_segun_genero, "altura", altura_buscada)
        imprimir_lista_de_diccionarios(reducir_diccionarios_en_lista(lista_heroes_altura_buscada_segun_genero, ["nombre", "genero", "altura"]), titulo)
        
        titulo = "* Héroe/s más bajo/s género \"F\":"
        lista_heroes_segun_genero = filtrar_por_clave(lista_personajes, "genero", "F")
        formatear_valores_diccionario_a_numericos(lista_heroes_segun_genero, ["altura"], "float")
        altura_buscada = valor_minimo_propiedad_en_lista_de_diccionarios(lista_heroes_segun_genero, 'altura')
        lista_heroes_altura_buscada_segun_genero = filtrar_por_clave(lista_heroes_segun_genero, "altura", altura_buscada)
        imprimir_lista_de_diccionarios(reducir_diccionarios_en_lista(lista_heroes_altura_buscada_segun_genero, ["nombre", "genero", "altura"]), titulo)

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # j - Determinar cuántos superhéroes tienen cada tipo de color de ojos.
      case "j" | "J":

        titulo = "j - Determinar cuántos superhéroes tienen cada tipo de color de ojos."
        encabezado = "COLOR DE OJOS | CANTIDAD SUPERHÉROES"
        mensaje_error = "Sin datos"
        diccionario = cantidad_valores_segun_clave(lista_personajes, "color_ojos", mensaje_error)
        imprimir_diccionario_formato_tabla(diccionario = diccionario, titulo = titulo, encabezado = encabezado)

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # k - Determinar cuántos superhéroes tienen cada tipo de color de pelo.
      case "k" | "K":

        titulo = "k - Determinar cuántos superhéroes tienen cada tipo de color de pelo."
        encabezado = "COLOR DE PELO | CANTIDAD SUPERHÉROES"
        mensaje_error = "Sin datos"
        diccionario = cantidad_valores_segun_clave(lista_personajes, "color_pelo", mensaje_error)
        imprimir_diccionario_formato_tabla(diccionario = diccionario, titulo = titulo, encabezado = encabezado)

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # l - Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con "No Tiene")
      case "l" | "L":

        titulo = "l - Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con \"No Tiene\")"
        encabezado = "INTELIGENCIA | CANTIDAD SUPERHÉROES"
        mensaje_error = "No tiene"
        diccionario = cantidad_valores_segun_clave(lista_personajes, "inteligencia", mensaje_error)
        imprimir_diccionario_formato_tabla(diccionario = diccionario, titulo = titulo, encabezado = encabezado)

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # m - Listar todos los superhéroes agrupados por color de ojos.
      case "m" | "M":
        
        titulo = "m - Listar todos los superhéroes agrupados por color de ojos."
        subtitulo = "Color de ojos"
        imprimir_lista_diccionarios_agrupando_segun_clave(titulo, subtitulo, lista_personajes, "color_ojos", ["nombre", "identidad"])
        
        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # n - Listar todos los superhéroes agrupados por color de pelo.
      case "n" | "N":

        titulo = "n - Listar todos los superhéroes agrupados por color de pelo."
        subtitulo = "Color de pelo"
        imprimir_lista_diccionarios_agrupando_segun_clave(titulo, subtitulo, lista_personajes, "color_pelo", ["nombre", "fuerza"])

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # o - Listar todos los superhéroes agrupados por tipo de inteligencia
      case "o" | "O":

        titulo = "o - Listar todos los superhéroes agrupados por tipo de inteligencia."
        subtitulo = "Inteligencia:"
        imprimir_lista_diccionarios_agrupando_segun_clave(titulo, subtitulo, lista_personajes, "inteligencia", ["nombre", "genero"])

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # salir del programa
      case "q":
        limpiar_consola()
        break
      case _:
        limpiar_consola()
        inicio = True