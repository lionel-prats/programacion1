import pygame

# Inicializar
pygame.init()

# Medidas
ANCHO = 800
ALTO = 600

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))

# Datos
pos_x = 100
pos_y = 100


# Bucle principal

jugando = True

while jugando:

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jugando = False

    # Lógica
    pos_x += 1
    if pos_x > ANCHO:
        pos_x = -50

    # Dibujos
    ventana.fill(NEGRO)
    pygame.draw.rect(ventana, VERDE, (pos_x, pos_y, 50, 50))

    # Actualizar
    pygame.display.update()

    pygame.time.delay(5)



# Salir
pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_07_movimiento_en_pygame
# python clase.py