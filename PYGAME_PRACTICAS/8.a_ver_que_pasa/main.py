import pygame 
from auxiliar import *

limpiar_consola()

configs = open_configs()

pygame.init()

clock = pygame.time.Clock()

screen_dimentions = (configs.get("screen").get("screen_width"), 
                     configs.get("screen").get("screen_height"))

screen = pygame.display.set_mode(screen_dimentions)
pygame.display.set_caption("A ver que pasa")


run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == \
            pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False
            
    screen.fill((0,0,0))

    pygame.display.update()

pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/PYGAME_PRACTICAS/8.a_ver_que_pasa
# python main.py