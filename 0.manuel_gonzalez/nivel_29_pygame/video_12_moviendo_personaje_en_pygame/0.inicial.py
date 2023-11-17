import pygame

# Inicializar
pygame.init()

# Medidas
ANCHO = 1280
ALTO = 720

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
NARANJA = (255, 128, 0)

# Ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

# Datos
aste_pos_x = 100
aste_pos_y = 100

nave_pos_x = 600
nave_pos_y = 500

# Bucle principal

jugando = True

while jugando:

    reloj.tick(60)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jugando = False
                
               
    # Lógica
    aste_pos_x += 5
    if aste_pos_x > ANCHO:
        aste_pos_x = -60

    # Dibujos
    ventana.fill(NEGRO)

    pygame.draw.rect(ventana, NARANJA, (aste_pos_x, aste_pos_y, 60, 60))

    pygame.draw.rect(ventana, VERDE, (nave_pos_x, nave_pos_y, 60, 60))


    # Actualizar
    pygame.display.update()



# Salir
pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_12_moviendo_personaje_en_pygame
# python 1000.final.py

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_12_moviendo_personaje_en_pygame
# python 1000.final.py