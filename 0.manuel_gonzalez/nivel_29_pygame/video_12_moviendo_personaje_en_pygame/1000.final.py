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
MARRON = (180, 100, 60)


# Ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

# Datos
pr_x = 100
pr_y = 100
vr_x = 5
vr_y = 5

pn_x = 600
pn_y = 500
vn_x = 0
vn_y = 0

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
            if event.key == pygame.K_RIGHT:
                vn_x = 10
            if event.key == pygame.K_LEFT:
                vn_x = -10
            if event.key == pygame.K_DOWN:
                vn_y = 10
            if event.key == pygame.K_UP:
                vn_y = -10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                vn_x = 0
            if event.key == pygame.K_LEFT:
                vn_x = 0
            if event.key == pygame.K_DOWN:
                vn_y = 0
            if event.key == pygame.K_UP:
                vn_y = 0
                
               
    # Lógica
    pr_x += vr_x
    if pr_x > ANCHO:
        pr_x = -60

    pn_x += vn_x
    pn_y += vn_y


    # Dibujos
    ventana.fill(NEGRO)

    pygame.draw.rect(ventana, MARRON, (pr_x, pr_y, 60, 60))

    pygame.draw.rect(ventana, VERDE, (pn_x, pn_y, 60, 60))


    # Actualizar
    pygame.display.update()



# Salir
pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_12_moviendo_personaje_en_pygame
# python 1000.final.py