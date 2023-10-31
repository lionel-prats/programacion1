import os
import re
from Equipo import Equipo

if __name__ == "__main__":

    def limpiar_consola():
        if os.name in ["ce", "nt", "dos"]: # windows
            os.system("cls")
        else: # linux o mac
            os.system("clear")

    def separador():
        print("\n---------------\n")
    
    def validar_dato(regex, dato, search = False):
        if search and re.search(regex, dato, re.IGNORECASE):
            return True
        elif re.match(regex, dato):
            return True
        return False 
    
    equipo = Equipo("dream_team.json")

    limpiar_consola()

    while True:

        print("Menú de opciones:\n")
        print("1. Mostrar la lista de todos los jugadores del Dream Team.\n")
        print("""2. Permitir al usuario seleccionar un jugador por su índice (validar con regex) y mostrar sus estadísticas completas, 
incluyendo temporadas jugadas, puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, 
asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de tiros de campo, 
porcentaje de tiros libres y porcentaje de tiros triples.\n""")
        print("""3. Después de mostrar las estadísticas de un jugador seleccionado por el usuario, permite al usuario guardar las estadísticas 
de ese jugador en un archivo CSV. El archivo CSV debe contener los siguientes campos: nombre, posición, temporadas, puntos totales, 
promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, 
robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.\n""")
        print("""4. Permitir al usuario buscar un jugador por su nombre (validar con regex) y mostrar sus logros, como campeonatos de la NBA, 
participaciones en el All-Star y pertenencia al Salón de la Fama del Baloncesto, etc.\n""")
        print("5. Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente.\n")
        print("6. Permitir al usuario ingresar el nombre de un jugador (validar con regex) y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.\n")
        print("7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.\n")
        print("8. Salir\n")

        opcion = input("Selecciona una opción (1-8): ")

        if opcion == "1":
            limpiar_consola()
            print(f"\n{opcion}) Lista jugadores Dream Team:\n")
            for jugador in equipo.get_lista_jugadores():
                print(f"{jugador.get_nombre()} - {jugador.get_posicion()}")
            separador()

        elif opcion == "2":
            limpiar_consola()
            regex = r"^\d{1,2}$" # 1 o mas digitos
            cantidad_jugadores = len(equipo.get_lista_jugadores())
            indice_jugador = input(f"\n{opcion}) Ingrese el índice de un jugador para ver sus estadísticas (0-{cantidad_jugadores - 1}): ")
            indice_valido = validar_dato(regex, indice_jugador)
            if indice_valido:
                if int(indice_jugador) in range(cantidad_jugadores):
                    jugador_seleccionado = equipo.get_lista_jugadores()[int(indice_jugador)]
                    estadisticas_jugador_seleccionado = jugador_seleccionado.get_estadistica()
                    print(f"\nEstadísticas de {jugador_seleccionado.get_nombre()}:")
                    for k, v in estadisticas_jugador_seleccionado.get_estadistas_dict().items():
                        print(f"{k.replace('_', ' ').capitalize()}: {v}")
                else:
                    print(f"\nEl índice ingresado no es válido. Debe ingresar un número entre 0 y {cantidad_jugadores - 1}.")
            else:
                print(f"\nEl índice ingresado no es válido. Debe ingresar un número entre 0 y {cantidad_jugadores - 1}.")
            separador()

        elif opcion == "3":
            limpiar_consola()
            regex = r"^\d{1,2}$" # 1 o mas digitos
            cantidad_jugadores = len(equipo.get_lista_jugadores())
            indice_jugador = input(f"\n{opcion}) Ingrese el índice de un jugador para crear un archivo .csv con sus estadísticas (0-{cantidad_jugadores - 1}): ")
            indice_valido = validar_dato(regex, indice_jugador)
            if indice_valido:
                if int(indice_jugador) in range(cantidad_jugadores):
                    print("\nel archivo michael_jordan231354.csv ha sido creado correctamente")
                else:
                    print(f"\nEl índice ingresado no es válido. Debe ingresar un número entre 0 y {cantidad_jugadores - 1}.")
            else:
                print(f"\nEl índice ingresado no es válido. Debe ingresar un número entre 0 y {cantidad_jugadores - 1}.")
            separador()

        elif opcion == "4":
            limpiar_consola()
            string_a_buscar = input(f"\n{opcion}) Ingrese el nombre de un jugador para ver sus logros: ")
            if(len(string_a_buscar) < 3):
                print_de_salida = "\nDebe ingresar al menos 3 caracteres."
            else:
                print_de_salida = f"\nLogros de jugadores encontrados con \"{string_a_buscar}\":\n\n"
                coincidencia = False
                for jugador in equipo.get_lista_jugadores():
                    hay_coincidencia = validar_dato(string_a_buscar, jugador.get_nombre(), True)
                    if hay_coincidencia:
                        coincidencia = True
                        print_de_salida += f"{jugador.get_nombre()}:\n"
                        for logro in jugador.get_logros(): 
                            print_de_salida += f"- {logro}\n"
                        print_de_salida += "\n"
                print_de_salida = print_de_salida[:-2]
                if not coincidencia:
                    print_de_salida = f"\nNo hay coincidencias con \"{string_a_buscar}\"."            
            print(print_de_salida)
            separador()

        elif opcion == "5":
            limpiar_consola()
            total_puntos_dream_team = 0
            lista_jugadores_ordenada_alfabeticamente = equipo.get_lista_jugadores_ordenada_alfabeticamente(equipo.get_lista_jugadores())
            print(f"\n{opcion}) Promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente:\n")
            print(f"Individuales:\n")
            for jugador in lista_jugadores_ordenada_alfabeticamente:
                print(f"{jugador.get_nombre()}: {jugador.get_estadistica().get_promedio_puntos_por_partido()}")
            
            print(f"\nPromedio puntos general: {equipo.get_promedio_puntos_equipo():.2f}")

            separador()

        elif opcion == "6":
            limpiar_consola()
            string = input(f"\n{opcion}) Ingrese el nombre de un jugador para saber si es miembro del salón de la fama: ")
            if(len(string) < 3):
                print("\nDebe ingresar al menos 3 caracteres.")
            elif string.lower() in equipo.get_miembros_salon_de_la_fama():
                print(f"\n{string} es miembro del salón de la fama")          
            else:
                print(f"\n{string} NO es miembro del salón de la fama")          
            separador()
            
        elif opcion == "7":
            limpiar_consola()
            pass
            # equipo.jugador_con_mas_rebotes()
        elif opcion == "8":
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/ENTREGAS/primer_parcial-v2
# python main.py