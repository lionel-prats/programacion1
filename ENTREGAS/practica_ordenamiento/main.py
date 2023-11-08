# MIT License
#
# Copyright (c) 2022 [UTN FRA](https://fra.utn.edu.ar/) All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

""" 
Alumno: Lionel Prats 
DNI: 31367577
División: 1H
Nro. legajo: 115678
Practica Ordenamiento
"""

'''
{
    "nombre": "Deadpool",
    "identidad": "Wade Wilson",
    "altura": 188.0,
    "peso": 95.32,
    "fuerza": 35,
    "inteligencia": "good"
}

1 - Listar los primeros N heroes
2 - Ordenar heroes por altura [Ascendente o Descendente]
3 - Ordenar heroes por fuerza [Ascendente o Descendente]
4 - Buscar heroes por inteligencia [good, average, high] 
5 - Exportar lista Ordenada de heroes ordenada [ASC o DESC] por una clave que decida el usuario a CSV
7 - Salir
'''

import funciones as f

f.limpiar_consola()

def stark_parcial(lista_heroes):
    while True:
        f.imprimir_menu()
        respuesta = input("Elija una opción entre 1 y 7: ")
        match respuesta:
            case "1":
                f.limpiar_consola()

                # cantidad de heroes
                regex_1 = r"^[0-9]{1,2}$"
                input_usuario_1 = input(f"\n{respuesta} - Ingrese la cantidad de jugadores a mostrar (cantidad entre 1 y {len(lista_heroes)}): ")
                while not f.validar_dato(regex_1, input_usuario_1) or int(input_usuario_1) < 1 or int(input_usuario_1) > 24:
                    f.limpiar_consola()
                    input_usuario_1 = input(f"\n{respuesta} - Error! Ingrese la cantidad de jugadores a mostrar (cantidad entre 1 y {len(lista_heroes)}): ")
                lista_reducida = lista_heroes[:int(input_usuario_1)]
                print(f"\nListar los primeros {input_usuario_1} heroes:\n")
                for i, heroe in enumerate(lista_reducida, 1):
                    if i < 10:
                        print(f"{i}  - ", end="")
                    else:
                        print(f"{i} - ", end="")
                    print(f"Nombre: {heroe.get('nombre') } | Altura: {heroe.get('altura') }")
                f.separador()

            case "2":
                f.limpiar_consola()

                # ASC O DESC
                regex_2 = r"^(a|A|d|D){1}$"
                asc_desc = input(f"\n{respuesta} - Ordenar heroes por altura. Orden ascendente (A) o descendente (D)? ")
                while not f.validar_dato(regex_2, asc_desc):
                    f.limpiar_consola()
                    asc_desc = input(f"\n{respuesta} - Error! Ordenar heroes por altura. Orden ascendente (A) o descendente (D)? ")
                lista_ordenada = f.ordenar_lista_diccionarios_metodo_quick_sort(lista_heroes, "altura", asc_desc)

                print(f"\nOrdenar heroes por altura de {'menor a mayor' if asc_desc.lower() == 'a' else 'mayor a menor'}:\n")
                for i, heroe in enumerate(lista_ordenada, 1):
                    if i < 10:
                        print(f"{i}  - ", end="")
                    else:
                        print(f"{i} - ", end="")
                    print(f"Nombre: {heroe.get('nombre') } | Altura: {heroe.get('altura') }")
                f.separador()
                
            case "3":
                
                f.limpiar_consola()

                # ASC O DESC
                regex_3 = r"^(a|A|d|D){1}$"
                asc_desc = input(f"\n{respuesta} - Ordenar heroes por fuerza. Orden ascendente (A) o descendente (D)? ")
                while not f.validar_dato(regex_3, asc_desc):
                    f.limpiar_consola()
                    asc_desc = input(f"\n{respuesta} - Error! Ordenar heroes por fuerza. Orden ascendente (A) o descendente (D)? ")
                lista_ordenada = f.ordenar_lista_diccionarios_metodo_quick_sort(lista_heroes, "fuerza", asc_desc)

                print(f"\nOrdenar heroes por fuerza de {'menor a mayor' if asc_desc.lower() == 'a' else 'mayor a menor'}:\n")
                for i, heroe in enumerate(lista_ordenada, 1):
                    if i < 10:
                        print(f"{i}  - ", end="")
                    else:
                        print(f"{i} - ", end="")
                    print(f"Nombre: {heroe.get('nombre') } | Fuerza: {heroe.get('fuerza') }")
                f.separador()

            case "4":
                f.limpiar_consola()

                # good, average, high
                regex_4 = r"^(a|A|g|G|h|H){1}$"
                input_usuario_4 = input(f"\n{respuesta} - Listar heroes según tipo de inteligencia. Good (G), good, average (A) o high (H)? ")
                while not f.validar_dato(regex_4, input_usuario_4):
                    f.limpiar_consola()
                    input_usuario_4 = input(f"\n{respuesta} - Error! Listar heroes según tipo de inteligencia. Good (G), good, average (A) o high (H)? ")
                    
                tipo_inteligencia = f.obtener_inteligencia_ingresada(input_usuario_4)
                lista_comprimida = f.get_diccionaros_segun_clave(lista_heroes, "inteligencia", tipo_inteligencia)

                print(f"\nBuscar heroes por inteligencia [good, average, high]:\n")
                for i, heroe in enumerate(lista_comprimida, 1):
                    if i < 10:
                        print(f"{i}  - ", end="")
                    else:
                        print(f"{i} - ", end="")
                    print(f"Nombre: {heroe.get('nombre') } | Inteligencia: {heroe.get('inteligencia').capitalize()}")
                f.separador()

            case "5":
                f.limpiar_consola()

                claves_validas = f.obtener_claves_validas()
                
                input_usuario_5 = input(f"\n{respuesta} - Elija una característica de los heroes para guardar la información en un archivo .csv (altura, fuerza, identidad, inteligencia, nombre o peso): ")
                while not input_usuario_5.lower() in claves_validas:
                    f.limpiar_consola()
                    input_usuario_5 = input(f"\n{respuesta} - Error! Elija una característica de los heroes para guardar la información en un archivo .csv (altura, fuerza, identidad, inteligencia, nombre o peso): ")
                
                regex_2 = r"^(a|A|d|D){1}$"
                asc_desc = input(f"\nOrdenar el listado por nombre de forma ascendente (A) o descendente (D)? ")
                while not f.validar_dato(regex_2, asc_desc):
                    f.limpiar_consola()
                    print(f"\n{respuesta} Ordenar el listado por nombre de forma ascendente (A) o descendente (D)? {input_usuario_5.lower()}")
                    asc_desc = input(f"\nError! Ordenar el listado por nombre de forma ascendente (A) o descendente (D)? ")

                lista_ordenada = f.ordenar_lista_diccionarios_metodo_quick_sort(lista_heroes, input_usuario_5.lower(), asc_desc)

                archivo_creado = f.guardar_csv(lista_ordenada, f"datos_heroes_ordenados_por_{input_usuario_5}_{'asc' if asc_desc.lower() == 'a' else 'desc'}")

                if archivo_creado:
                    print(f"\n{archivo_creado}")
                else:
                    print("Error!")
                f.separador()
                                
            case "7":
                f.limpiar_consola()
                print('\nFin de la ejecucion')
                break
            
            case _:
                f.limpiar_consola()
                print("\nOpción no válida. Debe seleccionar una opción entre 1 y 7.")
                f.separador()

if __name__ == '__main__':

    ruta_archivo_heroes = "data_stark.json"
    lista_heroes = f.leer_json(ruta_archivo_heroes)

    if lista_heroes:
        stark_parcial(lista_heroes.get("heroes"))
    else:
        print(f"No se pudo cargar el archivo {ruta_archivo_heroes}")

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/ENTREGAS/practica_ordenamiento
# python main.py