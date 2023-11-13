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


def blitear_figura(figura, posicion_en_x, posicion_en_y, direccion):
    mover_hacia(direccion)
    pantalla.blit(figura, (posicion_en_x, posicion_en_y))


def actualizar_direcciones():
    if pos_cuadradoX + ancho_cuadrado >= ancho_pantalla or pos_cuadradoX <= 0:
        direccion_eje_x *= -1     

    if pos_cuadradoY + alto_cuadrado >= alto_pantalla or pos_cuadradoY <= 0:
        direccion_eje_y *= -1

def mover_hacia(direccion):
    global pos_cuadradoX, pos_cuadradoY
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
    
direccion = "bl"
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # mover_hacia(direccion=direccion)

    if pos_cuadradoX + ancho_cuadrado >= ancho_pantalla or pos_cuadradoX <= 0:
        direccion_eje_x *= -1     

    if pos_cuadradoY + alto_cuadrado >= alto_pantalla or pos_cuadradoY <= 0:
        direccion_eje_y *= -1
        

    pantalla.fill((0, 0, 0))

    blitear_figura(cuadrado, pos_cuadradoX, pos_cuadradoY, direccion)

    pygame.display.flip()

    pygame.time.Clock().tick(60)
