import pygame 

pygame.init()

WIDTH = 1280
HEIGHT = 720

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

screen = pygame.display.set_mode((WIDTH,HEIGHT))

run = True

while run:
    
    # capturo todos los eventos que ocurren en la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    # dibujos
    screen.fill((BLACK))
    pygame.draw.rect(screen, WHITE, (1170, 10, 100, 100)) # llamamos a la funcion rect() del modulo draw de la libreria pygame
    pygame.draw.rect(screen, BLUE, (1170, 610, 100, 100)) 
    pygame.draw.rect(screen, WHITE, (10, 610, 100, 100)) 
    pygame.draw.rect(screen, RED, (10, 10, 100, 100)) 

    pygame.draw.circle(screen, GREEN, (640,360), 50)

    pygame.draw.line(screen, BLUE, (0,720), (1280,0), 5)

    pygame.draw.polygon(screen, RED, ((300,300),
                                      (350,300),
                                      (350,250),
                                      (400,250),
                                      (400,300),
                                      (450,300),
                                      (450,350),
                                      (300,350)), 5)


    # actualizar
    pygame.display.update()

pygame.quit()