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
r1_x = 100
r1_y = 100

r2_x = 150
r2_y = -50


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
    r1_x -= 1
    if r1_x < -50:
        r1_x = ANCHO

    r2_x += 1
    r2_y += 1
    if r2_x > ANCHO:
        r2_x = -50
    if r2_y > ALTO:
        r2_y = -50

    # Dibujos
    ventana.fill(NEGRO)
    pygame.draw.rect(ventana, VERDE, (r1_x, r1_y, 50, 50))
    pygame.draw.rect(ventana, AZUL, (r2_x, r2_y, 50, 50))

    # Actualizar
    pygame.display.update()

    pygame.time.delay(5)



# Salir
pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_08_mas_movimiento_de_figuras
# python clase.py