import pygame 
from modules.enemies.enemy import Enemy

class Lava(Enemy):
    def __init__(self, image, x, y, tile_size):
        Enemy.__init__(self, image, x, y)
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size // 2))