import pygame 
from pygame.locals import * 
from auxiliar import *
from variables import *
from modulos.world import World

limpiar_consola()

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platformer")

# load images 
sun_img = pygame.image.load("img/sun.png")
bg_img = pygame.image.load("img/sky.png")

world = World(world_data, tile_size)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(bg_img, (0,0))
    screen.blit(sun_img, (100,100))
    
    world.draw(screen)

    draw_grid(
        screen=screen, 
        screen_width=screen_width, 
        screen_height=screen_height, 
        tile_size=tile_size
    )

    pygame.display.update()

pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/PYGAME_PRACTICAS/4.juego_tipo_mario/video01.version_final
# python main.py