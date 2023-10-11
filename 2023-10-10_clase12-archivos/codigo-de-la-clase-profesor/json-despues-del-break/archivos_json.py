from archivos_csv import leer_csv, crear_csv, ruta_archivo, ROOT_DIR
import json

def crear_json(ruta: str, modo: str, lista_heroes: list[dict]) -> None:
    with open(ruta, modo, encoding='utf-8') as archivo_json:
        contenido = {
            "lista_heroes_marvel": lista_heroes
        }
        json.dump(contenido, archivo_json, indent=4)
        print(f'Archivo creado en la ruta: {ruta}')

def leer_json(ruta: str, modo: str, key: str) -> list[dict]:
    lista_de_archivo = []
    with open(ruta, modo, encoding='utf-8') as archivo_json:
        lista_de_archivo = json.load(archivo_json).get(key)
    return lista_de_archivo


if __name__ == '__main__':
    heroes = leer_csv(ruta_archivo, 'r')
    OUTPUT_JSON = f'{ROOT_DIR}heroes_stark.json'
    OUTPUT_JSON_F = f'{ROOT_DIR}heroes_stark_F.json'
    OUTPUT_JSON_BATMAN = f'{ROOT_DIR}heroes_stark_BATMAN.csv'
    # crear_json(OUTPUT_JSON, 'w', heroes)
    lista_heroes = leer_json(OUTPUT_JSON, 'r', "lista_heroes_dc")
    crear_csv(OUTPUT_JSON_BATMAN, 'w', lista_heroes)

    #crear_json(OUTPUT_JSON_F, 'w', heroinas)