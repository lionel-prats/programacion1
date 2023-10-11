import json

ROOT_DIR = "0.davila/09-archivos/json/"
ruta_archivo_json = f"{ROOT_DIR}data.json"

def parse_json(ruta_archivo: str)-> dict:
    lista = []
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        lista = json.load(archivo)
        # for linea in archivo:
        #     print(linea, end = "")
    return lista

lista = parse_json(ruta_archivo_json)
print(lista)

# dejé el video en 1h45'
