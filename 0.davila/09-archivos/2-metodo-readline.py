ruta_al_archivo = r"C:\Users\User\Desktop\utn\cuatrimestre1\programacion_1\2023-10-05-clase11-archivos\repaso-clase-curso-anterior\teoria.txt"

modo_apertura = "r"

archivo = open(ruta_al_archivo, modo_apertura)

print("posicion puntero:", archivo.tell()) 
print(archivo.readline(), end="")
print("posicion puntero:", archivo.tell())
print(archivo.readline(), end="")
print("posicion puntero:", archivo.tell())
print(archivo.readline(), end="")
print("posicion puntero:", archivo.tell())
print(archivo.readline(), end="")
print("posicion puntero:", archivo.tell())
print(archivo.readline(), end="")
print("posicion puntero:", archivo.tell())

archivo.close()