import pygame
import sys
import random

pygame.init()

# pantalla
ancho_pantalla, alto_pantalla = 1200, 800
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Movimiento Diagonal")

direcciones_iniciales_posibles = ("tr", "br", "bl", "tl")
cuadrado = []
ancho_cuadrado = []
alto_cuadrado = []
pos_cuadradoX = []
pos_cuadradoY = []
direccion_eje_x = []
direccion_eje_y = []
direccion = []
cantidad_cuadrados = 10

multiplos_de_5_positivos = [i for i in range(5, 21, 5)] 
multiplos_de_5_negativos = [i for i in range(-20, -4, 5)]
random.shuffle(multiplos_de_5_positivos)
random.shuffle(multiplos_de_5_negativos)
print(multiplos_de_5_positivos)
print(multiplos_de_5_negativos)

for i in range(cantidad_cuadrados):
    ancho_random, alto_random = 100, 100
    ancho_cuadrado.append(ancho_random)
    alto_cuadrado.append(alto_random)
    cuadrado_surface = pygame.Surface((ancho_random, alto_random)) 
    cuadrado_surface.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    cuadrado.append(cuadrado_surface)
    ancho_cuadrado.append(100)
    alto_cuadrado.append(100)
    pos_cuadradoX.append(random.randint(0, 700))
    pos_cuadradoY.append(random.randint(0, 700))
    direccion_eje_x.append(random.choice(multiplos_de_5_positivos))
    direccion_eje_y.append(random.choice(multiplos_de_5_negativos))
    # direccion_eje_x.append(random.randint(5, 15))
    # direccion_eje_y.append(random.randint(-15, -5))
    direccion.append(direcciones_iniciales_posibles[random.randint(0, 3)])

def blitear_figura(figura, posicion_en_x, posicion_en_y, direccion, direccion_eje_x, direccion_eje_y, alto_cuadrado, ancho_cuadrado, i):
    mover_hacia(direccion, i)
    actualizar_direcciones(i)
    pantalla.blit(figura, (posicion_en_x, posicion_en_y))

def actualizar_direcciones(i):
    if pos_cuadradoX[i] + ancho_cuadrado[i] >= ancho_pantalla or pos_cuadradoX[i] <= 0:
        direccion_eje_x[i] *= -1     
    if pos_cuadradoY[i] + alto_cuadrado[i] >= alto_pantalla or pos_cuadradoY[i] <= 0:
        direccion_eje_y[i] *= -1

def mover_hacia(direccion, i):
    if direccion == "tr":
        pos_cuadradoX[i] += direccion_eje_x[i]
        pos_cuadradoY[i] += direccion_eje_y[i]
    elif direccion == "br":
        pos_cuadradoX[i] += direccion_eje_x[i]
        pos_cuadradoY[i] -= direccion_eje_y[i]
    elif direccion == "bl":
        pos_cuadradoX[i] -= direccion_eje_x[i]
        pos_cuadradoY[i] -= direccion_eje_y[i]
    elif direccion == "tl":
        pos_cuadradoX[i] -= direccion_eje_x[i]
        pos_cuadradoY[i] += direccion_eje_y[i]

while True:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill((0, 0, 0))

    for i in range(cantidad_cuadrados):
        blitear_figura(cuadrado[i], pos_cuadradoX[i], pos_cuadradoY[i], direccion[i], direccion_eje_x[i], direccion_eje_y[i], alto_cuadrado[i], ancho_cuadrado[i], i)

    pygame.display.flip()

    pygame.time.Clock().tick(60)


# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/PYGAME_PRACTICAS/2.tiro_al_blanco_v1/
# python prueba8.py