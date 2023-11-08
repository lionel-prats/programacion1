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

                # cantidad de heroes
                regex = r"^[0-9]{1,2}$"
                input_usuario = input(f"\nIngrese la cantidad de jugadores a mostrar (cantidad entre 1 y {len(lista_heroes)}): ")
                while not f.validar_dato(regex, input_usuario) or int(input_usuario) < 1 or int(input_usuario) > 24:
                    input_usuario = input(f"\nIngrese la cantidad de jugadores a mostrar (cantidad entre 1 y {len(lista_heroes)}): ")
                
                # ASC O DESC
                regex = r"^a|A|d|D$"
                asc_desc = input(f"\nOrden ascendente (A) o descendente (D)? ")
                while not f.validar_dato(regex, asc_desc):
                    asc_desc = input(f"\nOrden ascendente (A) o descendente (D)? ")
                
                f.limpiar_consola()

                lista_reducida = lista_heroes[:int(input_usuario)]
                
                lista_heroes_ordenada_por_nombre_asc = f.ordenar_lista_diccionarios_metodo_quick_sort(lista_reducida, "altura", asc_desc)
                
                print(f"\n{respuesta} - Listar los primeros N heroes:\n")
                for i, heroe in enumerate(lista_heroes_ordenada_por_nombre_asc, 1):
                    if i < 10:
                        print(f"{i}  - ", end="")
                    else:
                        print(f"{i} - ", end="")
                    print(f"Nombre: {heroe.get('nombre') } | Altura: {heroe.get('altura') }")
                
                f.separador()

            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                f.limpiar_consola()
                print('\nFin de la ejecucion')
                break
            
if __name__ == '__main__':

    ruta_archivo_heroes = "data_stark.json"
    lista_heroes = f.leer_json(ruta_archivo_heroes)

    if lista_heroes:
        stark_parcial(lista_heroes.get("heroes"))
    else:
        print(f"No se pudo cargar el archivo {ruta_archivo_heroes}")

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/ENTREGAS/practica_ordenamiento
# python main.py