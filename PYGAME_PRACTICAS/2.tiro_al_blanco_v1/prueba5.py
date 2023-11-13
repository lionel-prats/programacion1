import pygame
import sys
import random

pygame.init()

ancho_pantalla, alto_pantalla = 220, 180
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Movimiento Diagonal")

ancho_cuadrado, alto_cuadrado = 100, 100
cuadrado = pygame.Surface((ancho_cuadrado, alto_cuadrado))
cuadrado.fill((255, 0, 0))  

pos_cuadradoX, pos_cuadradoY = 95, 50

direccion_eje_x, direccion_eje_y = 1, -1

direccion = "tr"
#lionel
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
    


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.epos_cuadradoXit()

    mover_hacia(direccion=direccion)

    print(f"{pos_cuadradoX}+{ancho_cuadrado} ({pos_cuadradoX + ancho_cuadrado}) >= {ancho_pantalla} || {pos_cuadradoX} <= {0}?", "")
    if pos_cuadradoX + ancho_cuadrado >= ancho_pantalla or pos_cuadradoX <= 0:
        direccion_eje_x *= -1 
        print(f"SI!, entonces direccion_eje_x = {direccion_eje_x}")
    else:
        print("NO!")

    print(f"{pos_cuadradoY}+{alto_cuadrado} ({pos_cuadradoY + alto_cuadrado}) >= {alto_pantalla} || {pos_cuadradoY} <= {0}?", "")
    if pos_cuadradoY + alto_cuadrado >= alto_pantalla or pos_cuadradoY <= 0:
        direccion_eje_y *= -1
        print(f"SI!, entonces direccion_eje_y = {direccion_eje_y}")
    else:
        print("NO!")
    print("----------------")

    pantalla.fill((0, 0, 0))

    pantalla.blit(cuadrado, (pos_cuadradoX, pos_cuadradoY))

    pygame.display.flip()

    pygame.time.Clock().tick(60)
