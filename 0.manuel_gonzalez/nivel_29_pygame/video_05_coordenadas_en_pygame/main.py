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
    pygame.draw.rect(screen, GREEN, ((WIDTH-100)/2, (HEIGHT-100)/2, 100, 100)) # llamamos a la funcion rect() del modulo draw de la libreria pygame

    # actualizar
    pygame.display.update()

pygame.quit()