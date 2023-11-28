import pygame

class Exit(pygame.sprite.Sprite):
    def __init__(self, path_img, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self)
        
        img = pygame.image.load(path_img)
        
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 2)))
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        print(self.rect)
        self.rect.y = y - tile_size       
        self.rect.y = y - 38      