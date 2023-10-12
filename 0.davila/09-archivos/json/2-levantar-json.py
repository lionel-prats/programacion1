import json

ROOT_DIR = "0.davila/09-archivos/json/"
ruta_archivo_json = f"{ROOT_DIR}json_nuevo.json"

def parse_json(ruta_archivo: str)-> dict:
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        contenido_json = json.load(archivo)
    return contenido_json

resultado = parse_json(ruta_archivo_json)
print(type(resultado))
print(resultado)