import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ancho, alto = 1200, 800
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Movimiento Diagonal")

# Configuración de la superficie
ancho_superficie, alto_superficie = 100, 100
superficie = pygame.Surface((ancho_superficie, alto_superficie))
superficie.fill((255, 0, 0))  # Rellenar con un color (rojo en este caso)

# Posición inicial aleatoria
x, y = random.randint(0, 700), random.randint(0, 700)

# x, y = 672, 672

# Dirección inicial
direccion_x, direccion_y = 10, -10  # Iniciar en diagonal arriba a la derecha

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar posición de la superficie
    x += direccion_x
    y += direccion_y

    # Verificar si alcanza el borde en el eje x
    if x + ancho_superficie > ancho or x < 0:
        direccion_x *= -1  # Invertir dirección en el eje x

    # Verificar si alcanza el borde en el eje y
    if y + alto_superficie > alto or y < 0:
        direccion_y *= -1  # Invertir dirección en el eje y

    # Limpiar pantalla
    pantalla.fill((0, 0, 0))

    # Dibujar superficie en las coordenadas actuales
    pantalla.blit(superficie, (x, y))

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.Clock().tick(60)
