import pygame
import copy
import random
import math

# Inicializar
pygame.init()

# Medidas
ANCHO = 1280
ALTO = 720

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
MARRON = (77, 38, 0)
AZUL = (0, 0, 255)
GRIS = (184, 184, 184)

# Ventana

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("VIDEO 27 CLASE 1")

reloj = pygame.time.Clock()

imagen_fondo = pygame.image.load("fondo_mapa2.png").convert()

monstruo1_der = pygame.image.load("mon_der1.png").convert_alpha()
monstruo2_der = pygame.image.load("mon_der2.png").convert_alpha()
monstruo1_izq = pygame.image.load("mon_izq1.png").convert_alpha()
monstruo2_izq = pygame.image.load("mon_izq2.png").convert_alpha()
monstruo1_arr = pygame.image.load("mon_arr1.png").convert_alpha()
monstruo2_arr = pygame.image.load("mon_arr2.png").convert_alpha()
monstruo1_baj = pygame.image.load("mon_baj1.png").convert_alpha()
monstruo2_baj = pygame.image.load("mon_baj2.png").convert_alpha()
monstruo0_par = pygame.image.load("mon_par0.png").convert_alpha()

monstruo_imagen = monstruo0_par

jugador0_par = pygame.image.load("par_0.png").convert_alpha()
jugador1_der = pygame.image.load("der_1.png").convert_alpha()
jugador2_der = pygame.image.load("der_2.png").convert_alpha()
jugador3_der = pygame.image.load("der_3.png").convert_alpha()
jugador4_der = pygame.image.load("der_4.png").convert_alpha()
jugador1_izq = pygame.image.load("izq_1.png").convert_alpha()
jugador2_izq = pygame.image.load("izq_2.png").convert_alpha()
jugador3_izq = pygame.image.load("izq_3.png").convert_alpha()
jugador4_izq = pygame.image.load("izq_4.png").convert_alpha()
jugador1_arr = pygame.image.load("arr_1.png").convert_alpha()
jugador2_arr = pygame.image.load("arr_2.png").convert_alpha()
jugador3_arr = pygame.image.load("arr_3.png").convert_alpha()
jugador4_arr = pygame.image.load("arr_4.png").convert_alpha()
jugador1_baj = pygame.image.load("baj_1.png").convert_alpha()
jugador2_baj = pygame.image.load("baj_2.png").convert_alpha()
jugador3_baj = pygame.image.load("baj_3.png").convert_alpha()
jugador4_baj = pygame.image.load("baj_4.png").convert_alpha()

jugador_imagen = jugador0_par

# Funciones

def avistamiento(a, b, distancia):
    if (math.sqrt(((b.x - a.x)**2) + ((b.y - a.y)**2))) < distancia:
        return True
    else:
        return False

# Datos

jugador_rectangulo = jugador_imagen.get_rect()
jugador_rectangulo.x = 100
jugador_rectangulo.y = 300
jugador_vel_x = 0
jugador_vel_y = 0
frames_jugador = 0

monstruo_rectangulo = monstruo_imagen.get_rect()
monstruo_rectangulo.x = 600
monstruo_rectangulo.y = 300
frames_monstruo = 0

# Bucle principal

jugando = True
while jugando:

    reloj.tick(60)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    moviendose_derecha = False
    moviendose_izquierda = False
    moviendose_arriba = False
    moviendose_abajo = False

    jugador_vel_x = 0
    jugador_vel_y = 0
    
    tecla = pygame.key.get_pressed()
    
    if tecla[pygame.K_LEFT] and not tecla[pygame.K_RIGHT]:
        jugador_vel_x = -3
        moviendose_izquierda = True
    if tecla[pygame.K_RIGHT] and not tecla[pygame.K_LEFT]:
        jugador_vel_x = 3
        moviendose_derecha = True
    if tecla[pygame.K_UP] and not tecla[pygame.K_DOWN]:
        jugador_vel_y = -3
        moviendose_arriba = True
    if tecla[pygame.K_DOWN] and not tecla[pygame.K_UP]:
        jugador_vel_y = 3
        moviendose_abajo = True

    # Lógica monstruo
    
    monstruo_derecha = False
    monstruo_izquierda = False
    monstruo_abajo = False
    monstruo_arriba = False
    monstruo_parado = False

    # verificamos si el player entro en el campo de vision del monstruo, para, en caso de que si, mover al monstruo y actualizar sus imagenes
    if avistamiento(monstruo_rectangulo, jugador_rectangulo, 200): 
        # el monstruo esta a la derecha del jugador, lo movemos hacia la izquierda en el eje x
        if monstruo_rectangulo.x > jugador_rectangulo.x: 
            monstruo_rectangulo.x -= 1
            monstruo_izquierda = True
        # el monstruo esta a la izquierda del jugador, lo movemos hacia la derecha en el eje x
        elif monstruo_rectangulo.x < jugador_rectangulo.x:
            monstruo_rectangulo.x += 1
            monstruo_derecha = True  
        # el monstruo esta debajo del jugador, lo movemos hacia arriba en el eje y
        if monstruo_rectangulo.y > jugador_rectangulo.y:
            monstruo_rectangulo.y -= 1
            monstruo_arriba = True
        # el monstruo esta arriba del jugador, lo movemos hacia abajo en el eje y
        elif monstruo_rectangulo.y < jugador_rectangulo.y:
            monstruo_rectangulo.y += 1
            monstruo_abajo = True
    else:
        monstruo_parado = True

    # controlamos que el monstruo no se salga de la pantalla
    if monstruo_rectangulo.x > ANCHO - 60:
        monstruo_rectangulo.x = ANCHO - 60
    if monstruo_rectangulo.x < 0:
        monstruo_rectangulo.x = 0
    if monstruo_rectangulo.y > ALTO - 60:
        monstruo_rectangulo.y = ALTO - 60
    if monstruo_rectangulo.y < 0:
        monstruo_rectangulo.y = 0

    # Lógica personaje

    jugador_rectangulo.x += jugador_vel_x
    jugador_rectangulo.y += jugador_vel_y

    if jugador_rectangulo.x > ANCHO - 60:
        jugador_rectangulo.x = ANCHO - 60
    if jugador_rectangulo.x < 0:
        jugador_rectangulo.x = 0
    if jugador_rectangulo.y > ALTO - 60:
        jugador_rectangulo.y = ALTO - 60
    if jugador_rectangulo.y < 0:
        jugador_rectangulo.y = 0

    # Colisiones

    if monstruo_rectangulo.collidepoint(jugador_rectangulo.centerx,
                                        jugador_rectangulo.centery):
        # si hay colision entre el player y el monstruo, delat de 1 segundo y salir del programa
        pygame.time.delay(1000)
        break
                
    # Dibujos

    ventana.blit(imagen_fondo, (0,0))

    # Movimiento monstruo

    if monstruo_derecha:
        frames_monstruo += 1
        if frames_monstruo >= 21:
            frames_monstruo = 1
        if frames_monstruo < 11:
            monstruo_imagen = monstruo1_der
        elif frames_monstruo < 21:
            monstruo_imagen = monstruo2_der
            
        ventana.blit(monstruo_imagen, monstruo_rectangulo)
        
    elif monstruo_izquierda:
        frames_monstruo += 1
        if frames_monstruo >= 21:
            frames_monstruo = 1
        if frames_monstruo < 11:
            monstruo_imagen = monstruo1_izq
        elif frames_monstruo < 21:
            monstruo_imagen = monstruo2_izq
            
        ventana.blit(monstruo_imagen, monstruo_rectangulo)            

    elif monstruo_abajo:
        frames_monstruo += 1
        if frames_monstruo >= 21:
            frames_monstruo = 1
        if frames_monstruo < 11:
            monstruo_imagen = monstruo1_baj
        elif frames_monstruo < 21:
            monstruo_imagen = monstruo2_baj
            
        ventana.blit(monstruo_imagen, monstruo_rectangulo)            

    elif monstruo_arriba:
        frames_monstruo += 1
        if frames_monstruo >= 21:
            frames_monstruo = 1
        if frames_monstruo < 11:
            monstruo_imagen = monstruo1_arr
        elif frames_monstruo < 21:
            monstruo_imagen = monstruo2_arr
            
        ventana.blit(monstruo_imagen, monstruo_rectangulo)            

    elif monstruo_parado:
        monstruo_imagen = monstruo0_par

        ventana.blit(monstruo_imagen, monstruo_rectangulo) 

    # Movimiento personaje
    
    if moviendose_derecha:
        frames_jugador += 1
        if frames_jugador >= 21:
            frames_jugador = 1
        if frames_jugador < 6:
            jugador_imagen = jugador1_der
        elif frames_jugador < 11:
            jugador_imagen = jugador2_der
        elif frames_jugador < 16:
            jugador_imagen = jugador3_der
        elif frames_jugador < 21:
            jugador_imagen = jugador4_der

        ventana.blit(jugador_imagen, jugador_rectangulo)

    elif moviendose_izquierda:
        frames_jugador += 1
        if frames_jugador >= 21:
            frames_jugador = 1   
        if frames_jugador < 6:
            jugador_imagen = jugador1_izq
        elif frames_jugador < 11:
            jugador_imagen = jugador2_izq
        elif frames_jugador < 16:
            jugador_imagen = jugador3_izq
        elif frames_jugador < 21:
            jugador_imagen = jugador4_izq

        ventana.blit(jugador_imagen, jugador_rectangulo)

    elif moviendose_arriba:
        frames_jugador += 1
        if frames_jugador >= 21:
            frames_jugador = 1
        if frames_jugador < 6:
            jugador_imagen = jugador1_arr
        elif frames_jugador < 11:
            jugador_imagen = jugador2_arr
        elif frames_jugador < 16:
            jugador_imagen = jugador3_arr
        elif frames_jugador < 21:
            jugador_imagen = jugador4_arr

        ventana.blit(jugador_imagen, jugador_rectangulo)

    elif moviendose_abajo:
        frames_jugador += 1
        if frames_jugador >= 21:
            frames_jugador = 1
        if frames_jugador < 6:
            jugador_imagen = jugador1_baj
        elif frames_jugador < 11:
            jugador_imagen = jugador2_baj
        elif frames_jugador < 16:
            jugador_imagen = jugador3_baj
        elif frames_jugador < 21:
            jugador_imagen = jugador4_baj

        ventana.blit(jugador_imagen, jugador_rectangulo)
           
    else:
        jugador_imagen = jugador0_par
        ventana.blit(jugador_imagen, jugador_rectangulo)
  

    # Actualizar
    pygame.display.update()


# Salir
pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_27_persecuciones
# python clase1.py