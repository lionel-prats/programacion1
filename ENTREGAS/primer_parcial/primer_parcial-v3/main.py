""" 
Fecha: 31-10-2023
Alumno: Lionel Prats 
DNI: 31367577
División: 1H
Nro. legajo: 115678
Parcial nro. 1
"""

# IMPORTANTE: para la creacion de archivos funcione hay que crear la carpeta /estadisticas_jugadores en la raiz del proyecto

from utils import *
from Equipo import Equipo

if __name__ == "__main__":
    
    equipo = Equipo("dream_team.json")

    limpiar_consola()
    
    inicio = True
    while True:
        if inicio:
            print("")
        inicio = False
        print("Menú de opciones:\n")
        print("1. Mostrar la lista de todos los jugadores del Dream Team.\n")
        print("""2. Permitir al usuario seleccionar un jugador por su índice (validar con regex) y mostrar sus estadísticas completas, 
incluyendo temporadas jugadas, puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, 
asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de tiros de campo, 
porcentaje de tiros libres y porcentaje de tiros triples.
Después de mostrar las estadísticas de un jugador seleccionado por el usuario, permite al usuario guardar las estadísticas 
de ese jugador en un archivo CSV. El archivo CSV debe contener los siguientes campos: nombre, posición, temporadas, puntos totales, 
promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, 
robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.\n""")
        print("""3. Permitir al usuario buscar un jugador por su nombre (validar con regex) y mostrar sus logros, como campeonatos de la NBA, 
participaciones en el All-Star y pertenencia al Salón de la Fama del Baloncesto, etc.\n""")
        print("4. Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente.\n")
        print("5. Permitir al usuario ingresar el nombre de un jugador (validar con regex) y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.\n")
        print("6. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.\n")
        print("7. Listado de jugadores ordenados de mayor a menor, según cantidad de robos totales.\n")
        print("8. Salir\n")

        opcion = input("Seleccione una opción entre 1 y 8: ")

        match opcion:
            case "1":
                limpiar_consola()
                print(f"\n{opcion}) Lista jugadores Dream Team:\n")
                for i, jugador in enumerate(equipo.get_lista_jugadores(), start=1):
                    print(f"{i}- {jugador.get_nombre()} - {jugador.get_posicion()}")
                separador()
            case "2":
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
                        guardar_csv = input("\n\"d\"+\"Enter\" para descargar la información, o cualquier otra tecla para volver al menú principal: ")
                        if guardar_csv.lower() == "d":
                            archivo_creado = equipo.guardar_estadisticas_jugador(indice_jugador) 
                            if archivo_creado:
                                print(f"\n{archivo_creado}")
                            else:
                                print("\nError")
                    else:
                        print(f"\nEl índice ingresado no es válido. Debe ingresar un número entre 0 y {cantidad_jugadores - 1}.")
                else:
                    print(f"\nEl índice ingresado no es válido. Debe ingresar un número entre 0 y {cantidad_jugadores - 1}.")
                separador()
            case "3":
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
            case "4":
                limpiar_consola()
                total_puntos_dream_team = 0
                lista_jugadores_ordenada_alfabeticamente = equipo.get_lista_jugadores_ordenada_alfabeticamente(equipo.get_lista_jugadores())
                print(f"\n{opcion}) Promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente:\n")
                print(f"Individuales:\n")
                for jugador in lista_jugadores_ordenada_alfabeticamente:
                    print(f"{jugador.get_nombre()}: {jugador.get_estadistica().get_promedio_puntos_por_partido()}")
                print(f"\nPromedio puntos general: {equipo.get_promedio_puntos_equipo():.2f}")
                separador()
            case "5":
                limpiar_consola()
                string = input(f"\n{opcion}) Ingrese el nombre de un jugador para saber si es miembro del salón de la fama: ")
                if(len(string) < 3):
                    print("\nDebe ingresar al menos 3 caracteres.")
                elif string.lower() not in equipo.get_lista_nombres_jugadores():
                    print(f"\n{string} no coincide con nuestros registros.")          
                elif string.lower() in equipo.get_miembros_salon_de_la_fama():
                    print(f"\n{string} es miembro del salón de la fama.")          
                else:
                    print(f"\n{string} NO es miembro del salón de la fama.")          
                separador()
            case "6":
                limpiar_consola()
                clave = "rebotes_totales"
                lista_jugadores_destacados = equipo.get_jugadores_destacados(clave)
                if lista_jugadores_destacados:
                    print(f"\n{opcion}) Jugador con mayor cantidad de {clave.replace('_',' ' )}:\n")
                    for jugador in equipo.get_jugadores_destacados(clave):
                        print(f"- {jugador.get('nombre')} ({jugador.get(clave)})") 
                else:
                    print("\nError")
                separador()
            case "7":
                limpiar_consola()
                clave = "robos_totales"
                print(f"\n{opcion}a) Listado de jugadores ordenados de mayor a menor, según cantidad de {clave.replace('_',' ' )}:\n")
                
                lista_jugadores_ordenada_por_estadistica = equipo.get_lista_jugadores_ordenada_por_clave_desc(equipo.get_lista_jugadores(), clave)
                
                print_pantalla = "" 
                contenido_csv = f"nombre;{clave}\n" 
                contenido_json = {
                    "jugadores": []
                }

                for i, jugador in enumerate(lista_jugadores_ordenada_por_estadistica, start=1):
                    print_pantalla += f"{i}- {jugador.get_nombre()} ({jugador.get_estadistica().get_robos_totales()})\n"
                    contenido_csv += f"{jugador.get_nombre()};{jugador.get_estadistica().get_robos_totales()}\n"
                    dict_jugador = {
                        "nombre": jugador.get_nombre(),
                        clave: jugador.get_estadistica().get_robos_totales()
                    }
                    contenido_json.get("jugadores").append(dict_jugador)
                print(print_pantalla)
                
                print(f"\n{opcion}b) Permitir guardar este listado ordenado en un archivo CSV con su apellido.csv")
                print(f"\n{opcion}c) Permitir guardar este listado ordenado en un archivo JSON y permitir al usuario ingresar el nombre del archivo a guardar (validar con regex)")

                opcion_usuario = input("\nSeleccione \"b\" o \"c\" para generar un archivo, o cualquier otra tecla para volver al menú anterior: ")

                if opcion_usuario.lower() == "b":
                    regex = r"^[a-zA-Z_]{1,10}$"
                    nombre_archivo = input("\nIngrese su apellido (solo letras y/o guión bajo; hasta 10 caracteres): ")
                    if validar_dato(regex, nombre_archivo):
                        print(f"\n{equipo.crear_csv(nombre_archivo, contenido_csv)}")
                    else:
                        print("\nError")

                elif opcion_usuario.lower() == "c":
                    regex = r"^[a-zA-Z_]{1,10}$"
                    nombre_archivo = input("\nIngrese el nombre del archivo json a crear (solo letras y/o guión bajo; hasta 10 caracteres): ")
                    if validar_dato(regex, nombre_archivo):
                        print(f"\n{equipo.crear_json(nombre_archivo, contenido_json)}")
                    else:
                        print("\nError")
                separador()

            case "8":
                limpiar_consola()
                print("\nHasta la próxima!")
                break
            case _:
                limpiar_consola()
                print("\nOpción no válida. Debe seleccionar una opción entre 1 y 8.")
                separador()