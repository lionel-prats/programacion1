import pygame 
from pygame.locals import * 
from auxiliar import *
from variables import *

from modules.player import Player
from modules.world import World


limpiar_consola()

pygame.init()

configs = open_configs()

clock = pygame.time.Clock()

screen_dimentions = (configs.get("screen").get("screen_width"), configs.get("screen").get("screen_height"))
screen = pygame.display.set_mode(screen_dimentions)
pygame.display.set_caption("VIDEO 5 - POO")

# load images 
# sun_img = pygame.image.load(configs.get("screen").get("images").get("sky"))
sun_img = pygame.image.load("img/sun.png")
bg_img = pygame.image.load("img/sky.png")

player = Player(configs.get("player1"))

blob_group = pygame.sprite.Group()

world = World(configs.get("screen"), configs.get("enemies"), enemy_sprite_group=blob_group)


# class Prueba_video_5(pygame.sprite.Sprite):
# 	def __init__(self, x, y):
#             pygame.sprite.Sprite.__init__(self)
#             self.image = pygame.image.load('img/start_btn.png')
#             self.image = pygame.transform.scale(self.image, (100,100))
#             self.rect = self.image.get_rect()
#             self.rect.x = x
#             self.rect.y = y
# blob_group.add(Prueba_video_5(50,50))

run = True
while run:

    clock.tick(configs.get("fps"))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == \
            pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False

    screen.blit(bg_img, (0,0))
    screen.blit(sun_img, (100,100))
    # world.draw_backgroung(screen)
    
    world.draw(screen)

    # .draw -> metodo de la clase Group para blitear los elementos de un objeto de tipo Group (sprites)
    # .update -> metodo de la clase Group que busca y ejecuta el metodo update() de los sprites que tenga dentro
    blob_group.update()
    blob_group.draw(screen)

    player.update(screen, configs.get("screen").get("screen_height"), tile_list = world.tile_list)

    world.draw_grid(screen)

    pygame.display.update()

pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/PYGAME_PRACTICAS/4.juego_tipo_mario/video5/video_05_POO
# python main.py