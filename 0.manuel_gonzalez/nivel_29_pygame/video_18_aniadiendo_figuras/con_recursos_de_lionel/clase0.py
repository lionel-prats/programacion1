import pygame
import random

# Inicializar
pygame.init()

# Medidas
ANCHO = 1280
ALTO = 720

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)


# Funciones
# detectar colision, parametros necesarios: 
# objeto1: x1(coor x)ancho, alto, x e y
# enemy: ancho, alto, x e y
def colision(x1, y1, a1, b1, x2, y2, a2, b2, ex=0):
    """  
    detectar colision, parametros necesarios: 
    objeto1: x1(coor x)ancho, alto, x e y
    enemy: ancho, alto, x e y
    Objeto 1: x1 (coord x), y1 (coord y), a1 (ancho), b1 (alto)
    Objeto 2: x2 (coord x), y2 (coord y), a2 (ancho), b2 (alto)
    ex = espacio extra de superpsicion entre los 2 objetos para que se produzca la colision
    """
    if x1 + a1 > x2 + ex and \
       x1 + ex < x2 + a2 and \
       y1 + b1 > y2 + ex and \
       y1 + ex < y2 + b2:
        return True
    else:
        return False


# Ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("VIDEO 18 CLASE 0")

reloj = pygame.time.Clock()
fuente = pygame.font.SysFont("arial black", 20)


# Carga imágenes

fondo = pygame.image.load("images/fondo_espacio_exterior.png").convert()

# nave
nave_arr = pygame.image.load("images/nave_arriba.png").convert()
nave_arr = pygame.transform.scale(nave_arr, (32, 32))
nave_arr.set_colorkey(BLANCO)
nave_der = pygame.transform.rotate(nave_arr, 270)
nave_der.set_colorkey(BLANCO)
nave_abj = pygame.transform.rotate(nave_arr, 180)
nave_abj.set_colorkey(BLANCO)
nave_izq = pygame.transform.rotate(nave_arr, 90)
nave_izq.set_colorkey(BLANCO)
# nave_abj = pygame.image.load("images/nave_abajo.png").convert_alpha()
# nave_izq = pygame.image.load("images/nave_izquierda.png").convert_alpha()
# nave_der = pygame.image.load("images/nave_derecha.png").convert_alpha()

# asteroide 1
aste_1a = pygame.image.load("images/asteroide_1a.png").convert()
aste_1a.set_colorkey(BLANCO)
aste_1b = pygame.image.load("images/asteroide_1b.png").convert()
aste_1b.set_colorkey(BLANCO)
aste_1c = pygame.image.load("images/asteroide_1c.png").convert()
aste_1c.set_colorkey(BLANCO)
aste_1d = pygame.image.load("images/asteroide_1d.png").convert()
aste_1d.set_colorkey(BLANCO)
# 4 listas para 4 versiones del asteroide 1
aste_1 = [aste_1a, aste_1b, aste_1c, aste_1d]
aste_3 = [aste_1b, aste_1c, aste_1d, aste_1a]
aste_4 = [aste_1c, aste_1d, aste_1a, aste_1b]
aste_5 = [aste_1d, aste_1a, aste_1b, aste_1c]

# aste_2a = pygame.image.load("images/asteroide_2a.png").convert_alpha()
# aste_2b = pygame.image.load("images/asteroide_2b.png").convert_alpha()
# aste_2c = pygame.image.load("images/asteroide_2c.png").convert_alpha()
# aste_2d = pygame.image.load("images/asteroide_2d.png").convert_alpha()

# 4 versiones del asteroide 2
# aste_2 = [aste_2a, aste_2b, aste_2c, aste_2d]
# aste_6 = [aste_2b, aste_2c, aste_2d, aste_2a]
# aste_7 = [aste_2c, aste_2d, aste_2a, aste_2b]
# aste_8 = [aste_2d, aste_2a, aste_2b, aste_2c]

asteroides_grandes = []
# asteroides_pequenios = []

for i in range(10):
    x = random.randint(0, ANCHO)
    y = random.randint(50, ALTO-120)
    v = random.randint(1, 3)
    f = random.choice([aste_1, aste_3, aste_4, aste_5])
    a = [f, x, y, v]
    asteroides_grandes.append(a)
    
# for i in range(10):
#     x = random.randint(0, ANCHO)
#     y = random.randint(50, ALTO-120)
#     v = random.randint(1, 4)
#     f = random.choice([aste_2, aste_6, aste_7, aste_8])
#     a = [f, x, y, v]
#     asteroides_pequenios.append(a)

# asteroides = asteroides_grandes + asteroides_pequenios


# Datos
vidas = 3
nivel = 1

nave_pos_x = 600
nave_pos_y = 670
nave_vel_x = 0
nave_vel_y = 0
direccion = "arriba"

frames_asteroides = 0

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
                nave_vel_x = 2
            if event.key == pygame.K_LEFT:
                direccion = "izquierda"
                nave_vel_x = -2
            if event.key == pygame.K_DOWN:
                direccion = "abajo"
                nave_vel_y = 2
            if event.key == pygame.K_UP:
                direccion = "arriba"
                nave_vel_y = -2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                nave_vel_x = 0
            if event.key == pygame.K_LEFT:
                nave_vel_x = 0
            if event.key == pygame.K_DOWN:
                nave_vel_y = 0
            if event.key == pygame.K_UP:
                nave_vel_y = 0

    # Lógica
    # incremento la posicion en x de cada uno de los 10 asteroides por cada iteracion del bucle principal
    # asteroides_grandes = [ [                aste_3   , coord X, coord Y, vel], [          aste_2         , coord X, coord Y, vel] ... total 10]
    # asteroides_grandes = [ [[4 im desord asteroide 1], 387    , 211    , 3  ], [[4 im desord asteroide 1], 257    , 121    , 2]   ... total 10]
    # a = [[4 im desord asteroide 1], 387, 211, 3]
    for a in asteroides_grandes:
        a[1] += a[3] # coord X += vel
        if a[1] > ANCHO:
            a[1] = -64

    # for a in asteroides_pequenios:
    #     a[1] += a[3]
    #     if a[1] > ANCHO:
    #         a[1] = -32


    nave_pos_x += nave_vel_x
    nave_pos_y += nave_vel_y

    # limites en x para la nave
    if nave_pos_x > ANCHO - 32:
        nave_pos_x = ANCHO - 32
    if nave_pos_x < 0:
        nave_pos_x = 0
    
    # limite en y por el borde inferior para la nave
    if nave_pos_y > ALTO - 32:
        nave_pos_y = ALTO - 32

    # la nave paso el borde superior de la pantalla, ganó!
    if nave_pos_y < 10:
        jugando = False
        
    # verificando si hay colision entre la nave y alguno de los 10 asteroides grandes (si lo hay sale del juego)
    for a in asteroides_grandes: 
        # colision(x1, y1, a1, b1, x2, y2, a2, b2, ex=0)
        # a = [[4 im desord asteroide 1], 387, 211, 3]
        if colision(a[1], a[2], 64, 64, nave_pos_x, nave_pos_y, 32, 32, 15):
            jugando = False

    # for a in asteroides_pequenios:
    #     if colision(a[1], a[2], 32, 32, nave_pos_x, nave_pos_y, 32, 32, 15):
    #         jugando = False


    # Imágenes
    
    ventana.blit(fondo, (0,0))

    texto1 = fuente.render("Nivel: " + str(nivel), True, BLANCO)
    texto2 = fuente.render("Vidas: " + str(vidas), True, BLANCO)
    ventana.blit(texto1, (20,10))
    ventana.blit(texto2, (1150, 10))


    # frames_asteroides += 1
    # if frames_asteroides >= 41:
    #     frames_asteroides = 1
        
    frames_asteroides += 1
    if frames_asteroides >= 241:
        frames_asteroides = 1

    # a = [[aste_1c, aste_1d, aste_1a, aste_1b], 387, 211, 3]
    if frames_asteroides < 61:
        for a in asteroides_grandes:
            ventana.blit(a[0][0], (a[1], a[2]))
    elif frames_asteroides < 121:
        for a in asteroides_grandes:
            ventana.blit(a[0][1], (a[1], a[2]))
    elif frames_asteroides < 181:
        for a in asteroides_grandes:
            ventana.blit(a[0][2], (a[1], a[2]))
    elif frames_asteroides < 241:
        for a in asteroides_grandes:
            ventana.blit(a[0][3], (a[1], a[2]))

    # if frames_asteroides < 11:
    #     for a in asteroides:
    #         ventana.blit(a[0][0], (a[1], a[2]))
    # elif frames_asteroides < 21:
    #     for a in asteroides:
    #         ventana.blit(a[0][1], (a[1], a[2]))
    # elif frames_asteroides < 31:
    #     for a in asteroides:
    #         ventana.blit(a[0][2], (a[1], a[2]))
    # elif frames_asteroides < 41:
    #     for a in asteroides:
    #         ventana.blit(a[0][3], (a[1], a[2]))

    if direccion == "arriba":    
        ventana.blit(nave_arr, (nave_pos_x, nave_pos_y))
    elif direccion == "abajo":    
        ventana.blit(nave_abj, (nave_pos_x, nave_pos_y))
    elif direccion == "izquierda":    
        ventana.blit(nave_izq, (nave_pos_x, nave_pos_y))
    elif direccion == "derecha":    
        ventana.blit(nave_der, (nave_pos_x, nave_pos_y))


    pygame.display.update()


pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_18_aniadiendo_figuras/con_recursos_de_lionel
# python clase0.py
