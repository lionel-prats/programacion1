import pygame 
from modules.enemies.enemy import Enemy

class Lava(Enemy):
    def __init__(self, image, x, y, tile_size):
        Enemy.__init__(self, image, x, y)
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/lava.png')
        # 35//8 == 32 -> parte entera del cociente de la division
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        pass