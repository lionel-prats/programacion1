import pygame

# Inicializar
pygame.init()

# Medidas
ANCHO = 1280
ALTO = 720

# Colores
NEGRO = (0, 0, 0)
VERDE = (10, 150, 10)
ROJO = (255, 0, 0)
MARRON = (150, 60, 10)


# Ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))


# Datos
personaje_rect = pygame.Rect(400, 200, 50, 50)

# Bucle principal

jugando = True
while jugando:

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # Lógica

    ventana.fill(VERDE)

    pygame.draw.rect(ventana, MARRON, personaje_rect)
    
    # Actualizar
    pygame.display.update()


# Salir
pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_25_clase_surface
# python clase0.py