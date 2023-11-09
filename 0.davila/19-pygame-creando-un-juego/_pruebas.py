ancho_columna = 100
alto_fila = 200
filas = 3
columnas = 4

# asi recorro las columnas de arriba a abajo y al final salto de columna
# contador = 0
# for columna in range(columnas):
#     for fila in range(filas):
#         x = columna * ancho_columna
#         y = fila * alto_fila
#         print(f"Coordenada imagen {contador}: ({x},{y}) (ancho imagen = {ancho_columna})")
#         contador += 1 

# asi recorro las filas de izquierda a derecha y al final salto de fila
contador = 0
for fila in range(filas):
    for columna in range(columnas):
        x = columna * ancho_columna
        y = fila * alto_fila
        print(f"Coordenada imagen {contador}: ({x},{y}) (ancho imagen = {ancho_columna}; alto imagen = {alto_fila})")
        contador += 1 