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

# pos_cuadradoX, pos_cuadradoY = random.randint(0, 700), random.randint(0, 700)
pos_cuadradoX, pos_cuadradoY = 1020, 45

# velocidad = random.randrange(15, 25)
# velocidad_eje_x, velocidad_eje_y = velocidad, -velocidad
velocidad_eje_x, velocidad_eje_y = 1, -1

direccion = "tr"
#lionel
def mover_hacia(direccion):
    global pos_cuadradoX, pos_cuadradoY
    if direccion == "tr":
        pos_cuadradoX += velocidad_eje_x
        pos_cuadradoY += velocidad_eje_y
    elif direccion == "br":
        pos_cuadradoX += velocidad_eje_x
        pos_cuadradoY -= velocidad_eje_y
    elif direccion == "bl":
        pos_cuadradoX -= velocidad_eje_x
        pos_cuadradoY -= velocidad_eje_y
    elif direccion == "tl":
        pos_cuadradoX -= velocidad_eje_x
        pos_cuadradoY += velocidad_eje_y
    


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.epos_cuadradoXit()

    mover_hacia(direccion=direccion)

    if pos_cuadradoX + ancho_cuadrado > ancho_pantalla or pos_cuadradoX <= 0:
        velocidad_eje_x *= -1 

    if pos_cuadradoY + alto_cuadrado > alto_pantalla or pos_cuadradoY <= 0:
        velocidad_eje_y *= -1

    pantalla.fill((0, 0, 0))

    print(pos_cuadradoX, pos_cuadradoY)
    pantalla.blit(cuadrado, (pos_cuadradoX, pos_cuadradoY))

    pygame.display.flip()

    pygame.time.Clock().tick(30)
