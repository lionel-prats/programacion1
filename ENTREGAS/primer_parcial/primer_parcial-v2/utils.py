import os
import re

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