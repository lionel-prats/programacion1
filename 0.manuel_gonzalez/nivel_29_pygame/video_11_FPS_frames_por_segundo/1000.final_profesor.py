import pygame
import random

# Medidas

ANCHO = 800
ALTO = 600

# Colores

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Inicializar pygame

pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
fuente = pygame.font.SysFont("arial", 64)

reloj = pygame.time.Clock()

# Datos
cuadrados = []
for i in range(50):
    x = random.randint(1, 799)
    y = random.randint(1, 599) 
    c = [x, y]
    cuadrados.append(c)


frames = 0
transcurrido = 0
fps = 0
segundos = 0

# Bucle principal

jugando = True
while jugando:

    tiempo = reloj.tick()
    transcurrido += tiempo
    frames += 1

    if transcurrido >= 1000:
        fps = frames
        frames = 0
        segundos += 1
        transcurrido = 0


    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # Lógica
    for c in cuadrados:
        c[0] += 1
        c[1] += 2
        if c[0] > 800:
            c[0] = 0
        if c[1] > 600:
            c[1] = 0


    # Imagenes
    ventana.fill(NEGRO)

    for c in cuadrados:
        pygame.draw.rect(ventana, BLANCO, (c[0],c[1],10,10))

    texto = fuente.render(str(fps), True, AZUL)
    texto2 = fuente.render(str(segundos), True, AZUL)
    ventana.blit(texto, (80,100))
    ventana.blit(texto2, (600, 100))

    

    # Update
    pygame.display.update()




pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_11_FPS_frames_por_segundo
# python clase.py