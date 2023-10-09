ROOT_DIR = "./2023-10-05-clase11-archivos/"
ruta_archivo = f"{ROOT_DIR}requirements.txt"

archivo = open(ruta_archivo, "r", encoding="utf-8")
#archivo = open(ruta_archivo, "r")

#contenido = archivo.readlines()
contenido = archivo.read()

print(archivo)
print(contenido)

archivo.close()

# ----------------------------------------------------

# ROOT_DIR = "../"
# ruta_archivo = f"{ROOT_DIR}glosario_python.txt"

# archivo = open(ruta_archivo, "r", encoding="utf-8")

# contenido = archivo.readlines()

# print(archivo)
# print(contenido)

# archivo.close()