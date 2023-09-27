# python -m pygame.examples.aliens

import pygame

# Se inicializa pygame
pygame.init() 

# Se crea una ventana
pantalla = pygame.display.set_mode([500, 500]) 

ejecutar_juego = True

while ejecutar_juego:
   
    lista_eventos = pygame.event.get()
    
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            ejecutar_juego = False

    # Se pinta el fondo de la ventana
    pantalla.fill((255, 255, 255))

    # pygame.draw.circle(screen, (R, G, B), (x_coord, y_coord), radio)
    pygame.draw.circle(pantalla, (250, 250, 0), (250, 250), 75)


    pygame.display.flip()

# Fin
pygame.quit()