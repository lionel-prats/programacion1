from lista_diccionarios_paulina_cocina import paulina as lista_recetas_paulina
import re

def buscar_receta(lista_recetas: list[dict]) -> None:
    patron = input('Ingrese la 1° palabra a buscar para la receta: ')
    for receta in lista_recetas:
        hay_match = re.search(patron, receta["title"], re.IGNORECASE)
        if hay_match:
            titulo = receta["title"]
            palabra = f"\033[0;31m{hay_match.group()}\033[0;m"
            titulo = titulo.replace(hay_match.group(), palabra)
            print(titulo)

buscar_receta(lista_recetas_paulina)

