"""  
display = modulo 
surface = objeto

"""


import pygame
pygame.init() #Se inicializa pygame
# from pygame.locals import K_x
from pygame.locals import *

screen = pygame.display.set_mode([500, 500]) #Se crea una ventana
# Título de la ventana
pygame.display.set_caption("Age of Empires VII") 

pressed_keys = pygame.key.get_pressed()
print(pressed_keys)
print("----------------------------------------------")

tick = pygame.USEREVENT + 0
pygame.time.set_timer(tick, 3000)

font = pygame.font.SysFont("Arial Narrow", 80)
font2 = pygame.font.SysFont("Arial Narrow", 40)
text = font.render("BOCA", True, (255, 255, 0), (0, 0, 255))
text2 = font2.render("RIVER", True, (225, 0, 0), (0, 0, 255))

rectangulo = pygame.Rect((90, 400), (200, 200))

imagen_bart = pygame.image.load("04.png")
rect_bart = imagen_bart.get_rect()
print(rect_bart)
rect_bart.centerx = 425 # centro imagen eje x
rect_bart.centery = 97 # centro imagen eje y
print(rect_bart)
print(rect_bart.width, rect_bart.height) # 200 200

# OTRA FORMA DE SETEAR LA UBICACION DE LA IMAGEN
# rect_bart = imagen_bart.get_rect( center = (425,97) )
# print(rect_bart)




running = True
while running:
   # Se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                print("Se presiono la tecla o")

        if event.type == tick:
            print("se ejecuto el evento tick")
            if True in pressed_keys:
                print(pressed_keys)
                if pressed_keys[K_x]:
                    print("Se presiono la tecla X")

    screen.fill((0, 60, 0))# Se pinta el fondo de la ventana
    # Se dibuja un círculo azul en el centro
    pygame.draw.circle(screen, (255, 0, 0), (150, 100), 100)
    pygame.draw.circle(screen, (0, 0, 255), (100, 100), 100)
    pygame.draw.rect(screen, (255, 255, 0), ((500-60)/2, (500-60)/2, 60, 60))
    pygame.draw.circle(screen, (0, 255, 0), (400, 400), 100)

    text.blit(text2, (30,10))
    screen.blit(text, (158,128))

    

    pygame.draw.rect(screen, (255, 255, 0), rectangulo)

    screen.blit(imagen_bart, rect_bart) # superficie que quiero fundir y en donde

    pygame.display.flip()# Muestra los cambios en  la pantalla
    # pygame.display.update()# Muestra los cambios en  la pantalla
pygame.quit() # Fin