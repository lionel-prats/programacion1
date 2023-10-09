ROOT_DIR = "./2023-10-05-clase11-archivos/"

texto = "escribi un archivo nuevo"

ruta_archivo = f"{ROOT_DIR}requirements.txt"

archivo = open(ruta_archivo, "w", encoding="utf-8")

contenido = archivo.readlines()

print(archivo)
print(contenido)

archivo.close()