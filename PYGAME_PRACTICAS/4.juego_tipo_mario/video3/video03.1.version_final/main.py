import pygame 
from pygame.locals import * 
from auxiliar import *
from variables import *
from modulos.world import World
from modulos.player import Player

limpiar_consola()

pygame.init()

configs = open_configs()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((configs.get("screen").get("screen_width"), configs.get("screen").get("screen_height")))
pygame.display.set_caption("Platformer")

# load images 
sun_img = pygame.image.load("img/sun.png")
bg_img = pygame.image.load("img/sky.png")

player = Player(configs.get("player1"))
world = World(configs.get("screen").get("world_data"), configs.get("screen").get("tile_size"))

run = True
while run:

    clock.tick(configs.get("fps"))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(bg_img, (0,0))
    screen.blit(sun_img, (100,100))
    
    world.draw(screen)

    player.update(screen, configs.get("screen").get("screen_height"))

    draw_grid(screen, configs.get("screen").get("screen_width"), configs.get("screen").get("screen_height"), configs.get("screen").get("tile_size"))
    # world.draw_grid(screen, configs.get("screen").get("screen_width"), configs.get("screen").get("screen_height"), configs.get("screen").get("tile_size"))

    pygame.display.update()

pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/PYGAME_PRACTICAS/4.juego_tipo_mario/video3/video03.1.version_final
# python main.py