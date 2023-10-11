ruta_archivo = "./2023-10-10_clase12/heroes.csv"


nuevo_personaje = "\nfatiga2024"
#lista_personajes = []
with open(ruta_archivo, "r+", encoding = "utf-8") as mi_archivo:
    for linea in mi_archivo:
        pass
        #if linea != "\n":
            #linea = linea.replace("\n", "")
            #lista_personajes.append(linea)
    #lista_personajes.append(nuevo_personaje)
    mi_archivo.write(nuevo_personaje)



