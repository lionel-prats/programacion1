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

# player1 = Player(x=0, y=0, speed_walk=4, speed_run=8, gravity=460, jump=5)
player1 = Player(x=0, y=0, speed_walk=4, speed_run=8, gravity=8, jump=16)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT:
                player1.control("walk_r", x=5, y=0)
            if event.key == pygame.K_LEFT:
                player1.control("walk_l", x=-5, y=0)
            if event.key == pygame.K_SPACE:
                player1.control("jump_r")

        
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_RIGHT:
                player1.control("stay_r", x=0, y=0)
            if event.key == pygame.K_LEFT:
                player1.control("stay_l", x=0, y=0)
            if event.key == pygame.K_SPACE:
                player1.control("stay_r", x=0, y=0)

    screen.blit(imagen_fondo, imagen_fondo.get_rect())

    player1.update()
    player1.draw(screen)
    # player update -- verificar como el player interactua con todo el nivel
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel
    
    pygame.display.flip()

    
    delta_ms = clock.tick(FPS) 








# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.davila/19-pygame-creando-un-juego/
# python main.py