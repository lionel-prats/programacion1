import json
from data import lista_personajes

ROOT_DIR = "0.davila/09-archivos/json/"
ruta_archivo_json_a_crear = f"{ROOT_DIR}json_nuevo.json"

def generar_json(ruta_archivo_json_nuevo_a_crear: str, lista: list) -> None:

    with open(ruta_archivo_json_nuevo_a_crear, "w", encoding="utf-8") as archivo_json_nuevo:
        dict_json = {
            "lista_personajes": lista
        }
        json.dump(dict_json, archivo_json_nuevo, indent=4, ensure_ascii=False )
        
        print(f"\nel archivo '{ruta_archivo_json_nuevo_a_crear}' se ha creado correctamente\n")

generar_json(ruta_archivo_json_a_crear, lista_personajes)