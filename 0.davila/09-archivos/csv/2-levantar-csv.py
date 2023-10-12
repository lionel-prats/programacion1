ROOT_DIR = "0.davila/09-archivos/"
ruta_archivo_csv_a_levantar = f"{ROOT_DIR}csv/csv_nuevo.csv"

def parse_csv(ruta_archivo_csv: str) -> list[dict]:
    """  
    [ruta_archivo_csv]: str -> ruta con nombre del archivo csv a levantar\n
    return: list[dict] -> csv parseado en una lista de diccionarios
    """
    with open(ruta_archivo_csv, "r", encoding="utf-8") as archivo_csv:
        lista_diccionarios = []
        lista_claves_filas = archivo_csv.readline()[:-1].split(",")
        for fila_datos in archivo_csv:
            lista_valores_fila = fila_datos[:-1].split(",")
            diccionario_fusionado = dict(zip(lista_claves_filas, lista_valores_fila))
            lista_diccionarios.append(diccionario_fusionado)
        return lista_diccionarios
    
heroes = parse_csv(ruta_archivo_csv_a_levantar)
primera_iteracion = True
print("\nTipo de dato retornado: ", type(heroes))
for heroe in heroes:
    if primera_iteracion:
        print("\nTipo de dato elementos de la lista retornada: ", type(heroe), "\n")
        primera_iteracion = False
    print(heroe, "\n")
    