ruta_archivo = r"C:\Users\User\Desktop\utn\cuatrimestre1\programacion_1\2023-10-10_clase12\requirements_2.txt"
ruta_archivo = "./2023-10-10_clase12/requirements_3.txt"

metodo_apertura = "a+"

nuevo_personaje = "fatiga2023\n"
lista_personajes = []
archivo = open(ruta_archivo, metodo_apertura, encoding = "utf-8")

archivo.seek(1)
print(archivo.tell(), archivo.read())

# for linea in archivo:
#     if linea != "\n":
#         linea = linea.replace("\n", "")
#         lista_personajes.append(linea)
# lista_personajes.append(nuevo_personaje)
# archivo.write(nuevo_personaje)
# archivo.close()

# for item in lista_personajes:
#     print(item)