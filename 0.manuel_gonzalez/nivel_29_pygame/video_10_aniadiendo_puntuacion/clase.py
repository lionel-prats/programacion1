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

# Ventana - objeto de tipo surface
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Poniendo Texto en Pygame")

# objeto de tipo Font (fuente de texto)
# dentro el modulo font, llamamos a la clase Font para crear un objeto de esta clase
# fuente = pygame.font.Font() 

# como disponemos de muchas fuentes instaladas en el sistema operativo llamammos a la clase SysFont para crear un objeto del tipo fuente de una de las fuentes del SO
fuente1 = pygame.font.SysFont("arial black", 32)

fuente2 = pygame.font.SysFont("consolas", 24) 

# objeto de tipo surface
texto = fuente1.render("CUADRADOS", True, BLANCO, AZUL)

# Datos
puntos = 0
vueltas = 0

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                puntos += 1

    # Lógica
    
    r1_x += 1
    if r1_x > ANCHO:
        r1_x = -50
        vueltas += 1

    r2_x += 1
    r2_y += 1
    if r2_x > ANCHO:
        r2_x = -50
    if r2_y > ALTO:
        r2_y = -50

    texto_puntos = fuente2.render("Puntos: " + str(puntos), True, BLANCO)
    texto_vueltas = fuente2.render("Vueltas: " + str(vueltas), True, BLANCO)
    
    # Dibujos
    ventana.fill(NEGRO)

    
    ventana.blit(texto, (260, 20))
    ventana.blit(texto_puntos, (30, 20))
    ventana.blit(texto_vueltas, (640, 20))

    pygame.draw.rect(ventana, VERDE, (r1_x, r1_y, 50, 50))
    # pygame.draw.rect(ventana, AZUL, (r2_x, r2_y, 50, 50))

    # Actualizar
    pygame.display.update()

    pygame.time.delay(5)



# Salir
pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_10_aniadiendo_puntuacion
# python clase.py