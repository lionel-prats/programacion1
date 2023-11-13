import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Movimiento Diagonal")

# Configuración de la superficie
surface_width, surface_height = 128, 128
surface = pygame.Surface((surface_width, surface_height))
surface.fill((255, 0, 0))  # Rellenar con un color (rojo en este caso)

# Coordenadas iniciales
x, y = 0, 672
speed = 2  # Velocidad de movimiento

# Dirección inicial (diagonal superior izquierda)
direction = "up-left"

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar coordenadas según la dirección
    if direction == "up-left":
        x += speed
        y -= speed
    else:  # direction == "down-right"
        x -= speed
        y += speed

    # Cambiar dirección cuando la superficie alcanza el borde
    if x > width - surface_width or y < 0:
        direction = "down-right"
    elif x < 0 or y > height - surface_height:
        direction = "up-left"

    # Limpiar pantalla
    screen.fill((0, 0, 0))

    # Dibujar superficie en las coordenadas actuales
    screen.blit(surface, (x, y))

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.Clock().tick(60)
