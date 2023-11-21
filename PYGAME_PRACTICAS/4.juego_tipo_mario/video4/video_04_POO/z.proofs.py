import pygame 
from auxiliar import *

limpiar_consola()

pygame.init()

screen = pygame.display.set_mode((400,400))


run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == \
            pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False

    key = pygame.key.get_pressed() 
    if key[pygame.K_UP] and key[pygame.K_RIGHT]:
        if key[pygame.K_SPACE]:  
            print("saltando diagonal top right")
    if key[pygame.K_UP] and key[pygame.K_LEFT]:
        if key[pygame.K_SPACE]:
            print("saltando diagonal top left")
    if key[pygame.K_SPACE]:
            print("SPACE")
    screen.fill((0,0,0))

    pygame.display.update()

pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/PYGAME_PRACTICAS/4.juego_tipo_mario/video3/video03.1.version_final
# python z.proofs.py