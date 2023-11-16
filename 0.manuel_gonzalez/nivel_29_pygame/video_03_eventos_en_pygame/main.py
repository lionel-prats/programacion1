import pygame 

pygame.init()

WIDTH = 800
HEIGHT = 600

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

screen = pygame.display.set_mode((WIDTH,HEIGHT))

run = True

# print(dir(pygame))

while run:
    
    # capturo todos los eventos que ocurren en la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                run = False

    screen.fill((BLACK))
    pygame.display.update() # llamamos a la funcion update(), del modulo display, de la libreria pygame

# pygame.time.delay(2000)

pygame.quit()