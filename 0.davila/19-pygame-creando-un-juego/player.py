import pygame
from constantes import *

def getSurfaceFromSpriteSheet(path, columnas, filas):
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
            lista.append(surface_fotograma)
    return lista

class Player:
    def __init__(self) -> None:
        self.walk = getSurfaceFromSpriteSheet(PATH_IMAGE + "caracters/stink/walk.png", 15, 1)
        self.stay = getSurfaceFromSpriteSheet(PATH_IMAGE + "caracters/stink/idle.png", 16, 1)
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()

    def control(self, x=0, y=0):
        self.move_x = x
        self.move_y = y

    def update(self):
        self.frame += 1
        if self.frame == (len(self.animation)):
            self.frame = 0
        self.rect.x += self.move_x
        self.rect.y += self.move_y

    def draw(self, screen):
        print(self.rect)
        self.image = self.animation[self.frame]
        # self.rect = self.image.get_rect()
        screen.blit(self.image, self.rect)