ruta_al_archivo = r"C:\Users\User\Desktop\utn\cuatrimestre1\programacion_1\2023-10-05-clase11-archivos\repaso-clase-curso-anterior\teoria.txt"

modo_apertura = "r"

archivo = open(ruta_al_archivo, modo_apertura)

print("\n\n", archivo.tell(), "\n\n") # 0 -> posicion del puntero

for linea in archivo:
    print(linea, end = "")

print("\n\n", archivo.tell(), "\n\n") # 1351 -> posicion del puntero

archivo.close()