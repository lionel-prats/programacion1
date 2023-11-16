import pygame 

pygame.init()

WIDTH = 1280
HEIGHT = 720

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.FULLSCREEN)

run = True

while run:
    
    # capturo todos los eventos que ocurren en la ventana
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False


    screen.fill((BLACK))
    pygame.display.update() # llamamos a la funcion update(), del modulo display, de la libreria pygame

# pygame.time.delay(2000)

pygame.quit()