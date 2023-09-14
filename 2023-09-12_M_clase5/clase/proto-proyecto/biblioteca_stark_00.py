# """  
# ... 
# :type mode: str
# """
# heroe = determinar_heroe_alto_bajo(lista_heroes, modo)
# mensaje = f"su identidad es {heroe.get('identidad')}"

def mostrar_menu() -> str:
    menu =\
    """
    1 - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
    2 - Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
    3 - Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
    4 - Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
    5 - Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
    6 - Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
    7 - Calcular e informar cual es el superhéroe más y menos pesado.
    8 - Salir
    """
    print(menu)
    opcion_elegida = input("Elija una opcion: ")
    return opcion_elegida