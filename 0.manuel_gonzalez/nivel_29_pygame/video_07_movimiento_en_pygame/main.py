import pygame 
from enemy import Enemy

pygame.init()

#constants
WIDTH = 800
HEIGHT = 600
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
print(screen.get_rect())

square_1 = Enemy((0, 100, 50, 50), RED)
square_2 = Enemy((400, 500, 50, 50), BLUE)
square_3 = Enemy((0, 0, 50, 50), GREEN)

# main loop
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
    square_1.update(screen, "from_right_to_left")
    square_2.update(screen, "to_left")
    square_3.update(screen, "diagonal")
    
    # actualizar
    pygame.display.update()

    pygame.time.delay(3) # llamamos a la funcion delay() del modulo time de la libreria pygame

pygame.quit()

# con cada iteracion del bucle se actualiza la ventana
# cada actualizacion se va a corresponder con un frame o cuadro del juego 
# si en un juego la ventana se actualiza 60 veces por segundo diremos que va a 60 FPSs

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_07_movimiento_en_pygame
# python main.py