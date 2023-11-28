import pygame
import random
from modules.enemies.enemy import Enemy

class Blob(Enemy):
    def __init__(self, path_image, x, y, tile_size, move_direction, amplitud):
        Enemy.__init__(self, path_image, x, y)
        
        self.image = pygame.transform.scale(self.image, (40, 35))

        # pongo a los blobs sobre el suelo si su altura es menor a la de las baldosas
        if self.rect.height < tile_size:
            self.rect.y += abs(self.rect.height - tile_size) 
        
        self.move_direction = move_direction
        self.amplitud = amplitud
        self.move_counter = random.randint(0,self.amplitud)

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1 
        if abs(self.move_counter) > self.amplitud:
            self.move_direction *= -1
            self.move_counter *= -1