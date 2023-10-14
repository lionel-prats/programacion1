def parse_json(ruta_archivo: str)-> dict:
    import json
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        contenido_json = json.load(archivo)
    return contenido_json

def limpiar_consola():
    import os
    if os.name in ["ce", "nt", "dos"]: # windows
        os.system("cls")
    else: # linux o mac
        os.system("clear")
        
def separador():
    print("\n---------------\n")