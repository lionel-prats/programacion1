""" 
Alumno: Lionel Prats 
DNI: 31367577
División: 1H
Nro. legajo: 115678
Desafío Stark 02
"""

from biblioteca_clase_7 import(
  texto_default, limpiar_consola, continuar, stark_imprimir_nombres_heroes, stark_imprimir_nombres_alturas, stark_calcular_imprimir_heroe, stark_calcular_imprimir_promedio_altura, imprimir_menu
)

def ejercicio_clase_7_main_app(lista: list[dict]):
  """  
  ACCION: se encarga de la ejecucion principal de nuestro programa\n 
  PARAMETROS:\n
  [lista] -> lista de superheroes
  RETURN: None
  """

  inicio = True
  while True:
    imprimir_menu()
    if inicio:
      inicio = False
      opcion_seleccionada = input(texto_default)
    else:
      opcion_seleccionada = input_continuar

    match opcion_seleccionada:

      # 1 - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
      case "1":

        stark_imprimir_nombres_heroes(lista)

        input_continuar = continuar(input(texto_default).lower())
        if not input_continuar:
          break

      # 2 - Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
      case "2":

        stark_imprimir_nombres_alturas(lista)

        input_continuar = continuar(input(texto_default).lower())
        if not input_continuar:
          break
        
      # 3 - Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
      case "3":

        print("\n3 - Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)\n")
        stark_calcular_imprimir_heroe(lista, "maximo", "altura")

        input_continuar = continuar(input(texto_default).lower())
        if not input_continuar:
          break
      # 4 - Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
      case "4":
        
        print("\n4 - Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)\n")
        stark_calcular_imprimir_heroe(lista, "minimo", "altura")

        input_continuar = continuar(input(texto_default).lower())
        if not input_continuar:
          break

      # 5 - Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
      case "5":

        stark_calcular_imprimir_promedio_altura(lista)
        
        input_continuar = continuar(input(texto_default).lower())
        if not input_continuar:
          break
      
      # 6 - Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
      case "6":

        print("\n6 - Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO)\n")
        stark_calcular_imprimir_heroe(lista, "maximo", "altura")
        
        print("\n6 - Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÍNIMO)\n")
        stark_calcular_imprimir_heroe(lista, "minimo", "altura")

        input_continuar = continuar(input(texto_default).lower())
        if not input_continuar:
          break
      # 7 - Calcular e informar cual es el superhéroe más y menos pesado.
      case "7":
        
        print("\n7 - Calcular e informar cual es el superhéroe más pesado.\n")
        stark_calcular_imprimir_heroe(lista, "maximo", "peso")
        
        print("\n7 - Calcular e informar cual es el superhéroe menos pesado.\n")
        stark_calcular_imprimir_heroe(lista, "minimo", "peso")

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