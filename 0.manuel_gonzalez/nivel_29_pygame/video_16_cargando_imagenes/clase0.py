import pygame

# Inicializar
pygame.init()

# Medidas
ANCHO = 1280
ALTO = 720

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
NARANJA = (255, 128, 0)
VERDE = (0, 255, 0)


# Ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("VIDEO 16 CLASE 0")

reloj = pygame.time.Clock()

# Datos

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
            
   
    # imagenes
    ventana.fill(NEGRO)
        
    pygame.draw.rect(ventana, NARANJA, (200,200,60,60))

    pygame.draw.rect(ventana, VERDE, (600,500,60,60))

    pygame.display.update()


# Salir
pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_16_cargando_imagenes
# python clase0.py