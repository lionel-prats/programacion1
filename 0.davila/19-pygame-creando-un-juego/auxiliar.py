import os
import pygame

class Auxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet(path, columnas, filas, flip=False):
        lista = []
        surface_imagen = pygame.image.load(path)
        fotograma_ancho = int(surface_imagen.get_width() / columnas)
        fotograma_alto = int(surface_imagen.get_height() / filas)

        # contador = 0
        for columna in range(columnas):
            for fila in range(filas):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto

                # print(f"Coordenada imagen {contador}: ({x},{y}) (ancho imagen = {fotograma_ancho}; alto imagen = {fotograma_alto})")
                # contador += 1

                surface_fotograma = surface_imagen.subsurface(x, y, fotograma_ancho, fotograma_alto)

                if flip:
                    # (frame, flip en x, flip en y)
                    surface_fotograma = pygame.transform.flip(surface_fotograma, True, False)

                lista.append(surface_fotograma)
        return lista
    

    def limpiar_consola():
        """  
        limpia la consola
        """
        # os.system('cls' if os.name == 'nt' else 'clear')
        if os.name in ["ce", "nt", "dos"]: # windows
            os.system("cls")
        else: # linux o mac
            os.system("clear")