import pygame
import sys
import random

pygame.init()

ancho_pantalla, alto_pantalla = 1200, 800
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Movimiento Diagonal")

ancho_cuadrado, alto_cuadrado = 100, 100
cuadrado = pygame.Surface((ancho_cuadrado, alto_cuadrado))
cuadrado.fill((255, 0, 0))  

pos_cuadradoX, pos_cuadradoY = random.randint(0, 700), random.randint(0, 700)

direccion_eje_x, direccion_eje_y = 10, -10
direccion = "br"

def blitear_figura(figura, posicion_en_x, posicion_en_y, direccion, direccion_eje_x, direccion_eje_y, alto_cuadrado, ancho_cuadrado):
    mover_hacia(direccion, posicion_en_x, posicion_en_y, direccion_eje_x, direccion_eje_y)
    actualizar_direcciones(ancho_cuadrado, alto_cuadrado, posicion_en_x, posicion_en_y, direccion_eje_x, direccion_eje_y)
    pantalla.blit(figura, (posicion_en_x, posicion_en_y))

def actualizar_direcciones(ancho_cuadrado, alto_cuadrado, pos_cuadradoX, pos_cuadradoY, direccion_eje_x, direccion_eje_y):
    if pos_cuadradoX + ancho_cuadrado >= ancho_pantalla or pos_cuadradoX <= 0:
        direccion_eje_x *= -1     
    if pos_cuadradoY + alto_cuadrado >= alto_pantalla or pos_cuadradoY <= 0:
        direccion_eje_y *= -1

def mover_hacia(direccion, pos_cuadradoX, pos_cuadradoY, direccion_eje_x, direccion_eje_y):
    if direccion == "tr":
        pos_cuadradoX += direccion_eje_x
        pos_cuadradoY += direccion_eje_y
    elif direccion == "br":
        pos_cuadradoX += direccion_eje_x
        pos_cuadradoY -= direccion_eje_y
    elif direccion == "bl":
        pos_cuadradoX -= direccion_eje_x
        pos_cuadradoY -= direccion_eje_y
    elif direccion == "tl":
        pos_cuadradoX -= direccion_eje_x
        pos_cuadradoY += direccion_eje_y
    
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill((0, 0, 0))

    for i in range(1):
        pass
    
    blitear_figura(cuadrado, pos_cuadradoX, pos_cuadradoY, direccion, direccion_eje_x, direccion_eje_y, alto_cuadrado, ancho_cuadrado)

    pygame.display.flip()

    pygame.time.Clock().tick(60)


# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/PYGAME_PRACTICAS/2.tiro_al_blanco_v1/
# python prueba6.py