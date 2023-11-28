import pygame
import random
from modules.enemies.enemy import Enemy

class Blob(Enemy):
    def __init__(self, path_image, x, y, tile_size, move_direction, amplitud, tile_list):
        Enemy.__init__(self, path_image, x, y)
        
        self.image = pygame.transform.scale(self.image, (40, 35))
        
        # pongo a los blobs sobre el suelo si su altura es menor a la de las baldosas
        if self.rect.height < tile_size:
            self.rect.y += abs(self.rect.height - tile_size) 
        
        self.move_direction = move_direction
        self.amplitud = amplitud
        # self.move_counter = random.randint(self.amplitud*-1, self.amplitud)
        self.move_counter = 0

        self.tile_list = tile_list


    # def update(self):
    #     self.rect.x += self.move_direction
    #     self.move_counter += 1 
    #     if abs(self.move_counter) > self.amplitud:
    #         self.move_direction *= -1
    #         self.move_counter *= -1

    def update(self):
        
        for tile in self.tile_list: 
        # tile == (<Surface(50x50x24 SW)>, <rect(coord_x, coord_y, width, hright)>)
            if tile[1].colliderect(self): 
                self.move_direction * -1
        self.rect.x += self.move_direction
        print(self.rect)

