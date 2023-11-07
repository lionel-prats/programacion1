""" 
Fecha: 31-10-2023
Alumno: Lionel Prats 
DNI: 31367577
División: 1H
Nro. legajo: 115678
Parcial nro. 1
"""

# IMPORTANTE: para la creacion de archivos funcione hay que crear la carpeta /estadisticas_jugadores en la raiz del proyecto
# IMPORTANTE: crear la carpeta /db en la raiz del proyecto para que funcione la parte de base e datos

import os
import re

def limpiar_consola():
        """  
        limpia la consola
        """
        if os.name in ["ce", "nt", "dos"]: # windows
            os.system("cls")
        else: # linux o mac
            os.system("clear")

def separador():
    print("\n---------------\n")

def validar_dato(regex, dato, search = False):
    """  
    recibe una expresion regular y un string a validar\n
    a su vez, recibe un boolean opcional que define si se usa el metodo search o el metodo match del modulo re
    retorna True en caso de pasar la validacion, False en caso contrario
    """
    if search and re.search(regex, dato, re.IGNORECASE):
        return True
    elif re.match(regex, dato):
        return True
    return False 