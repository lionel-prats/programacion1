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
        print(f"Elegiste la opcion {opcion_seleccionada}")

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break
      # b - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
      case "b" | "B":
        print(f"Elegiste la opcion {opcion_seleccionada}")

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break
      # c - Recorrer la lista y determinar cuál es el superhéroe más alto de género M
      case "c" | "C":
        print(f"Elegiste la opcion {opcion_seleccionada}")

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break
      # e - Recorrer la lista y determinar cuál es el superhéroe más alto de género F
      case "d" | "D":
        print(f"Elegiste la opcion {opcion_seleccionada}")

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # e - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M
      case "e" | "E":
        print(f"Elegiste la opcion {opcion_seleccionada}")

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # f - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F
      case "f" | "F":
        print(f"Elegiste la opcion {opcion_seleccionada}")

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # g - Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
      case "g" | "G":
        print(f"Elegiste la opcion {opcion_seleccionada}")

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # h - Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
      case "h" | "H":
        print(f"Elegiste la opcion {opcion_seleccionada}")

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # i - Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
      case "i" | "I":
        print(f"Elegiste la opcion {opcion_seleccionada}")

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # j - Determinar cuántos superhéroes tienen cada tipo de color de ojos.
      case "j" | "J":
        print(f"Elegiste la opcion {opcion_seleccionada}")

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # k - Determinar cuántos superhéroes tienen cada tipo de color de pelo.
      case "k" | "K":
        print(f"Elegiste la opcion {opcion_seleccionada}")

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # l - Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’)
      case "l" | "L":
        print(f"Elegiste la opcion {opcion_seleccionada}")

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # m - Listar todos los superhéroes agrupados por color de ojos.
      case "m" | "M":
        print(f"Elegiste la opcion {opcion_seleccionada}")

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # n - Listar todos los superhéroes agrupados por color de pelo.
      case "n" | "N":
        print(f"Elegiste la opcion {opcion_seleccionada}")

        input_continuar = continuar(input(texto_default))
        if not input_continuar:
          break

      # o - Listar todos los superhéroes agrupados por tipo de inteligencia
      case "o" | "O":
        print(f"Elegiste la opcion {opcion_seleccionada}")

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