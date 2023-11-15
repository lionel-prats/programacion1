import pygame 
from pygame.locals import * 
from auxiliar import *
from variables import *
from classes.world import World

limpiar_consola()

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platformer")

# load images 
sun_img = pygame.image.load("img/sun.png")
bg_img = pygame.image.load("img/sky.png")

"""  
print("surface original:")
print(sun_img)
print(sun_img.get_rect(), "\n")

surface_modificada_en_ancho_y_alto = pygame.transform.scale(sun_img, (tile_size, tile_size))
print("surface modificada en ancho y alto:")
print(surface_modificada_en_ancho_y_alto, "\n")

rectangulo_de_la_surface_modificada = surface_modificada_en_ancho_y_alto.get_rect()
print("rectangulo de la surface modificada en ancho y alto:")
print(rectangulo_de_la_surface_modificada, "\n")

rectangulo_de_la_surface_modificada.x = 700
rectangulo_de_la_surface_modificada.y = 700
print("coordenada x0,y0 del rectangulo de la surface modificada en ancho y alto, modificada:")
print(rectangulo_de_la_surface_modificada)
"""

world = World(world_data, tile_size)
# for element in world.tile_list:
#     print(element)

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

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/PYGAME_PRACTICAS/4.juego_tipo_mario/video01.version-lio
# python main.py