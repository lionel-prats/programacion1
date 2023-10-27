from utils import * 
from Estadistica import Estadistica

def funcion_principal(jugadores):
    """
    """
    limpiar_consola()
    while True:
        opcion_seleccionada = -1
        while opcion_seleccionada == -1:
            opcion_seleccionada = menu_principal(jugadores) 
            if opcion_seleccionada not in ("z", "Z"):
                limpiar_consola()
        match opcion_seleccionada:
            case "1":
                pass
            
            case "c" | "C":
                print("\nHasta la próxima\n")
                break
    
def menu_principal(jugadores):
    """ 
    """
    import re 
    imprimir_menu(jugadores)
    opcion_ingresada = input("Elija una opción: ")
    validacion = re.search(r"^[a-cA-C]{1}$", opcion_ingresada)
    if not validacion:
        return -1 
    return opcion_ingresada

def imprimir_menu(jugadores):
    menu = ""
    for jugador in jugadores:
        pass

    # print(jugadores[0])


    """  
    """
    menu = """\n1. asd asd - asdsad 
2. asd asd - asdsad 
3. asd asd - asdsad 
4. asd asd - asdsad 
5. asd asd - asdsad 
6. asd asd - asdsad 
7. asd asd - asdsad 
8. asd asd - asdsad 
9. asd asd - asdsad 
10. asd asd - asdsad (1)

promedio de puntos por partido de todo el equipo del Dream
Team, ordenado por nombre de manera ascendente. (5)

jugador con la mayor cantidad de rebotes totales: asdasdasd (7)

---------------

Menú de opciones:

A Estadísticas completas jugador (2 - 3)
B Logros jugador (4 - 6)
C Salir\n"""
    print(menu)


if __name__ == "__main__":
    limpiar_consola()

    estadistica = Estadistica()
    estadistica.imprimir_listado_jugadores()


"""  
1. Armstrong asd - Escolta - 28 puntos por partido
2. Chester asd - Base - 31 puntos por partido
3. Jordan asd - asdsad - 35 puntos por partido 
4. Princeton asd - asdsad - 48 puntos por partido 
5. asd asd - asdsad 
6. asd asd - asdsad 
7. asd asd - asdsad 
8. asd asd - asdsad 
9. asd asd - asdsad 
10. asd asd - asdsad (1 - 5)

jugador con la mayor cantidad de rebotes totales: Jordan (54) (7)

---------------

Menú de opciones:

A Estadísticas completas jugador (2 - 3)
B Logros jugador (4 - 6)
C Salir
"""