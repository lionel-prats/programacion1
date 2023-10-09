# import biblioteca_stark_00
# from biblioteca_stark_00 import *
from biblioteca_stark_00 import (
    determina_heroe_mas_alto, determina_heroe_mas_bajo, 
    determina_identidad_heroe_alto_bajo, determinar_heroe_alto_bajo, 
    mostrar_menu, imprimir_nombres_de_heroes,
    imprimir_nombre_altura_de_heroes as print_name_heroes,
)
from testing_1 import el_nombre_de_esta_funcion_es_horrible_y_se_deberia_llamar_pepe as test1_pepe
from testing_2 import el_nombre_de_esta_funcion_es_horrible_y_se_deberia_llamar_pepe as test2_pepe



"""
J - Construir un menú que permita elegir qué dato obtener
"""

def main_app(lista_heroes: list[dict]):
    """
    Ejecuta todo nuestro programa.
    Recibe la lista de heroes
    """
   
    test1_pepe()
    while True:
        
        opcion_elegida = mostrar_menu()

        match opcion_elegida:
            case "1":
                imprimir_nombres_de_heroes(lista_heroes)
            case "2":
                print_name_heroes(lista_heroes)
            case "3":
                heroe_mas_alto = determinar_heroe_alto_bajo(lista_heroes, 'max')
            case "4":
                heroe_mas_bajo = determinar_heroe_alto_bajo(lista_heroes, 'min')
            case "5":
                pass
            case "6":
                determina_identidad_heroe_alto_bajo(lista_heroes, 'max')
                determina_identidad_heroe_alto_bajo(lista_heroes, 'min')
            case "7":
                pass
            case "8":
                break
            case _:
                print('Opcion incorrecta, elija entre 1 y 9')

