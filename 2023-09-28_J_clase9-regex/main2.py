# from data import paulina as lista_recetas_paulina 
import re 

lista_recetas_paulina = {

}


def bsucar_receta(lista_recetas: list[dict]) -> None:
    patron = input("Ingrese la palabra a buscar para la receta: ")
    for receta in lista_recetas:
        hay_match = re.search(patron, receta["title"], re.IGNORECASE)
        if hay_match:
            titulo = receta["title"]
            palabra = f"\033[0;31m{hay_match.group(0)}\033[0;m"
            titulo = titulo.replace(hay_match.group(0), palabra)


bsucar_receta(lista_recetas_paulina)