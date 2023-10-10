""" 
Alumno: Lionel Prats 
DNI: 31367577
División: 1H
Nro. legajo: 115678
Desafío Stark 03
"""

from biblioteca_stark_03 import(
  texto_default, limpiar_consola, continuar, mostrar_menu, stark_imprimir_heroe_genero, stark_calcular_imprimir_heroe_genero, stark_calcular_imprimir_promedio_altura_genero, stark_calcular_cantidad_por_tipo, stark_listar_heroes_por_dato
)

# funcion principal de la aplicacion
def stark_marvel_app_3(lista_personajes: list[dict]):
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
        stark_imprimir_heroe_genero(lista_personajes, "m")
        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break
      # b - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
      case "b" | "B":
        stark_imprimir_heroe_genero(lista_personajes, "f")
        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break
      # c - Recorrer la lista y determinar cuál es el superhéroe más alto de género M
      case "c" | "C":
        stark_calcular_imprimir_heroe_genero(lista_personajes, "maximo", "altura", "M", True)
        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break
      # e - Recorrer la lista y determinar cuál es el superhéroe más alto de género F
      case "d" | "D":
        stark_calcular_imprimir_heroe_genero(lista_personajes, "maximo", "altura", "F", True)
        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break
      # e - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M
      case "e" | "E":
        stark_calcular_imprimir_heroe_genero(lista_personajes, "minimo", "altura", "M", True)
        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break
      # f - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F
      case "f" | "F":
        stark_calcular_imprimir_heroe_genero(lista_personajes, "minimo", "altura", "F", True)
        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break
      # g - Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
      case "g" | "G":
        stark_calcular_imprimir_promedio_altura_genero(lista_personajes, "altura", "m")
        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break
      # h - Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
      case "h" | "H":
        stark_calcular_imprimir_promedio_altura_genero(lista_personajes, "altura", "f")
        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break
      # i - Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
      case "i" | "I":
        titulo = "- Héroe/s más alto/s género \"M\":"
        print(f"\n{titulo}")
        stark_calcular_imprimir_heroe_genero(lista_personajes, "maximo", "altura", "M")
        
        titulo = "- Héroe/s más alto/s género \"F\":"
        print(titulo)
        stark_calcular_imprimir_heroe_genero(lista_personajes, "maximo", "altura", "F")

        titulo = "- Héroe/s más bajo/s género \"M\":"
        print(titulo)
        stark_calcular_imprimir_heroe_genero(lista_personajes, "minimo", "altura", "M")
        
        titulo = "- Héroe/s más bajo/s género \"F\":"
        print(titulo)
        stark_calcular_imprimir_heroe_genero(lista_personajes, "minimo", "altura", "F")
      
        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break
      # j - Determinar cuántos superhéroes tienen cada tipo de color de ojos.
      case "j" | "J":
        stark_calcular_cantidad_por_tipo(lista_personajes, "color_ojos")
        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break
      # k - Determinar cuántos superhéroes tienen cada tipo de color de pelo.
      case "k" | "K":
        stark_calcular_cantidad_por_tipo(lista_personajes, "color_pelo")
        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break
      # l - Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con "No Tiene")
      case "l" | "L":
        stark_calcular_cantidad_por_tipo(lista_personajes, "inteligencia")
        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break
      # m - Listar todos los superhéroes agrupados por color de ojos.
      case "m" | "M":
        stark_listar_heroes_por_dato(lista_personajes, "color_ojos")
        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # n - Listar todos los superhéroes agrupados por color de pelo.
      case "n" | "N":
        stark_listar_heroes_por_dato(lista_personajes, "color_pelo")
        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # o - Listar todos los superhéroes agrupados por tipo de inteligencia
      case "o" | "O":
        stark_listar_heroes_por_dato(lista_personajes, "inteligencia")
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