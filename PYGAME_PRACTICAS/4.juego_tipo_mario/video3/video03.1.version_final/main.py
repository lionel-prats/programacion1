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

screen_dimentions = (configs.get("screen").get("screen_width"), configs.get("screen").get("screen_height"))
screen = pygame.display.set_mode(screen_dimentions)
pygame.display.set_caption("VIDEO 3 - POO")

# load images 
# sun_img = pygame.image.load(configs.get("screen").get("images").get("sky"))
sun_img = pygame.image.load("img/sun.png")
bg_img = pygame.image.load("img/sky.png")

player = Player(configs.get("player1"))
world = World(configs.get("screen"))

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

    player.update(screen, configs.get("screen").get("screen_height"))

    world.draw_grid(screen)

    pygame.display.update()

pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/PYGAME_PRACTICAS/4.juego_tipo_mario/video3/video03.1.version_final
# python main.py