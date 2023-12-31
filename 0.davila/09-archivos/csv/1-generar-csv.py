from data import lista_personajes

ROOT_DIR = "0.davila/09-archivos/"
ruta_archivo_csv_a_crear = f"{ROOT_DIR}csv/csv_nuevo.csv"

def generar_csv(ruta_archivo_csv_nuevo_a_crear: str, lista: list[dict]) -> None:
    """  
    [ruta_archivo_csv_nuevo_a_crear]: str -> ruta con nombre del archivo csv a crear\n
    [lista]: list[dict] -> lista de diccionarios que sera el contenido del nuevo archivo\n
    return None  
    """
    texto = ",".join(list(lista[0].keys()))
    texto += "\n"
    with open(ruta_archivo_csv_nuevo_a_crear, "w", encoding="utf-8") as archivo_csv_nuevo:
        for i, heroe in enumerate(lista):
            texto += ",".join(list(lista[i].values()))
            texto += "\n"
        # archivo_csv_nuevo.write(texto[:-1])
        archivo_csv_nuevo.write(texto)
    print(f"\nel archivo '{ruta_archivo_csv_nuevo_a_crear}' se ha creado correctamente\n")

generar_csv(ruta_archivo_csv_a_crear, lista_personajes)