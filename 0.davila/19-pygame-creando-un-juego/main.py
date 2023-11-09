import pygame
import sys
from constantes import *
from player import Player

# DEJE EL VIDEO EN 1 hora 52 minutos 

screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load(PATH_IMAGE + "locations/forest/all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA, ALTO_VENTANA) )

player1 = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                player1.control(x=-5)
            if event.key == pygame.K_RIGHT:
                player1.control(x=5)
        
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player1.control(x=0)


    player1.update()
    player1.draw(screen)
    # player update -- verificar como el player interactua con todo el nivel
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel
    
    pygame.display.flip()

    screen.blit(imagen_fondo, imagen_fondo.get_rect())

    delta_ms = clock.tick(FPS) 








# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.davila/19-pygame-creando-un-juego/
# python main.py