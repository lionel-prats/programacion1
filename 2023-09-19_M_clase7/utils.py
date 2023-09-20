import os

def limpiar_consola():
    """ 
    ACCION: limpia la consola\n
    PARAMETROS: None\n
    RETURN: None
    """
    if os.name in ["ce", "nt", "dos"]: # windows
        os.system("cls")
    else: # linux o mac
        os.system("clear")

def separador():
    print("\n------------------\n")