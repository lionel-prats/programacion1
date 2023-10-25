def limpiar_consola():
    import os
    if os.name in ["ce", "nt", "dos"]: # windows
        os.system("cls")
    else: # linux o mac
        os.system("clear")    
limpiar_consola()
def leer_archivo(nombre_archivo_json):
    """ 
    Crear la función 'leer_archivo' la cual recibirá por parámetro un string que indicará el nombre y extensión del archivo a leer (Ejemplo: archivo.json). Dicho archivo se abrirá en modo lectura únicamente y retornará la lista de héroes como una lista de diccionarios.
    """
    import json
    with open(nombre_archivo_json, "r", encoding="utf-8") as archivo:
        contenido_json = json.load(archivo)
    return contenido_json["lista_personajes"]

lista_heroes = leer_archivo("0.data_stark.json")

contenido_csv = ";".join(lista_heroes[0].keys())
contenido_csv += "\n"

for heroe in lista_heroes:
    contenido_csv += ";".join(heroe.values())
    contenido_csv += "\n"

with open("0.data_stark.csv", "w", encoding="utf-8") as csv_nuevo:
    csv_nuevo.write(contenido_csv)