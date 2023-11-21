import pygame

# Inicializar
pygame.init()

# Medidas
ANCHO = 1280
ALTO = 720

# Colores
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
MARRON = (150, 70, 10)
BLANCO = (255, 255, 255)

# Funciones

def dibujar_muro(superficie, rectangulo):
    pygame.draw.rect(superficie, MARRON, rectangulo)

def dibujar_personaje(superficie, rectangulo):
    pygame.draw.rect(superficie, AZUL, rectangulo)

def construir_mapa(mapa):
    muros = []
    x = 0
    y = 0
    for fila in mapa:
        for muro in fila:
            if muro == "X":
                muros.append(pygame.Rect(x,y,80,80))
            x += 80
        x = 0
        y += 80
    return muros

def dibujar_mapa(superficie, muros):
    for muro in muros:
        dibujar_muro(superficie, muro)

def dibujar_grilla():
	for linea in range(1, 9):
		pygame.draw.line(surface=ventana, color=BLANCO, start_pos=(0, linea * 80), end_pos=(ANCHO, linea * 80), width=1) # lineas paralelas al eje x de la pantalla
	for linea in range(1, 16):
		pygame.draw.line(surface=ventana, color=BLANCO, start_pos=(linea * 80, 0), end_pos=(linea * 80, ALTO), width=1) # lineas paralelas al eje y de la pantalla


# Ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
ventana_rect = ventana.get_rect() 
pygame.display.set_caption("VIDEO 23 CLASE 1")

reloj = pygame.time.Clock()


# mapas 
#baldosas: ancho = 1280/16 (80px) | alto = 720/9 (80px)
mapa = [
    "XXXXXXXXXXXXXXXX",
    "X              X",
    "X XXXXXX XXXXX X",
    "X X            X",
    "X XXXX XXXXXXX X",
    "X X    X       X",
    "X XX XXXXX XXX X",
    "X              X",
    "XXXXXXXXXXXXXXXX"
    ]

# Datos
mapa_muros = construir_mapa(mapa)
personaje = pygame.Rect(655, 415, 50, 50)
personaje_vel_x = 0
personaje_vel_y = 0


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
                direccion = "derecha"
                personaje_vel_x = 10
                # personaje_vel_y = 0
            if event.key == pygame.K_LEFT:
                direccion = "izquierda"
                personaje_vel_x = -10
                # personaje_vel_y = 0
            if event.key == pygame.K_DOWN:
                direccion = "abajo"
                personaje_vel_y = 10
                # personaje_vel_x = 0
            if event.key == pygame.K_UP:
                direccion = "arriba"
                personaje_vel_y = -10
                # personaje_vel_x = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                personaje_vel_x = 0
            if event.key == pygame.K_LEFT:
                personaje_vel_x = 0
            if event.key == pygame.K_DOWN:
                personaje_vel_y = 0
            if event.key == pygame.K_UP:
                personaje_vel_y = 0        


    # Lógica

    personaje.x += personaje_vel_x
    personaje.y += personaje_vel_y

    if personaje.x > ANCHO - personaje.width:
        personaje.x = ANCHO - personaje.width
    if personaje.x < 0:
        personaje.x = 0
    if personaje.y > ALTO - personaje.height:
        personaje.y = ALTO - personaje.height
    if personaje.y < 0:
        personaje.y = 0

    for muro in mapa_muros:
    # for muro in muros:
        if personaje.colliderect(muro):
            personaje.x -= personaje_vel_x
            personaje.y -= personaje_vel_y

    # Dibujos

    ventana.fill(NEGRO)

    dibujar_mapa(ventana, muros=mapa_muros)
    dibujar_grilla()

    # for muro in muros:
    #     dibujar_muro(ventana, muro)

    dibujar_personaje(ventana, personaje)

    # Actualizar
    pygame.display.update()


# Salir
pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_23_mapas
# python clase1.py