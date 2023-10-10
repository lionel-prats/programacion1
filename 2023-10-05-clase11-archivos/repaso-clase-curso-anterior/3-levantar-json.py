import json

ruta_archivo_json = r"C:\Users\User\Desktop\utn\cuatrimestre1\programacion_1\2023-10-05-clase11-archivos\repaso-clase-curso-anterior\data.json"

metodo_apertura = "r"

def parse_json(ruta_archivo: str)-> dict:
    lista = []
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        lista = json.load(archivo)
        # for linea in archivo:
        #     print(linea, end = "")
    return lista[0]["name"]

lista = parse_json(ruta_archivo_json)
print(lista)

# dejé el video en 1h45'