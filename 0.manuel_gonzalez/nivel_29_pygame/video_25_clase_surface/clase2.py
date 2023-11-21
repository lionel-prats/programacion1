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

imagen_manzana = pygame.image.load("baldosa_manzana.png").convert_alpha()



# Datos

personaje_rect = pygame.Rect(400, 200, 50, 50)


manzana_rect = imagen_manzana.get_rect()

manzana_rect.x = 100
manzana_rect.y = 100


# Bucle principal

jugando = True
while jugando:

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # Lógica

    manzana_rect.x += 1
    manzana_rect.y += 1


    ventana.fill(VERDE)

    pygame.draw.rect(ventana, MARRON, personaje_rect)
    
    ventana.blit(imagen_manzana, manzana_rect)


    # Actualizar
    pygame.display.update()


# Salir
pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_25_clase_surface
# python clase2.py