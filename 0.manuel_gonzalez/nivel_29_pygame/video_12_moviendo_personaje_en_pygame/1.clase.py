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
aste_vel_x = 5

nave_pos_x = 600
nave_pos_y = 500
nave_vel_x = 0
nave_vel_y = 0

# Bucle principal

jugando = True

while jugando:

    reloj.tick(60)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        if event.type == pygame.KEYDOWN:
            print("keydown")
            if event.key == pygame.K_ESCAPE:
                jugando = False
            """  
            para lograr un movimiento fluido vamos a simular las leyes fisicas del movimiento 
            espacio = vellocidad/tiempo
            espacio_final = espacio_inicial + velocidad/tiempo
            en este caso la velocidad sera frames/segundo
            cada frame, un cuerpo se movera una cantidad de pixeles
            """
            if event.key == pygame.K_RIGHT:
                print("derecha")
                nave_vel_x = 10
            if event.key == pygame.K_LEFT:
                print("izquierda")
                nave_vel_x = -10
            if event.key == pygame.K_DOWN:
                nave_vel_y = 10
            if event.key == pygame.K_UP:
                nave_vel_y = -10
            
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
    aste_pos_x += aste_vel_x
    if aste_pos_x > ANCHO:
        aste_pos_x = -60

    nave_pos_x += nave_vel_x
    nave_pos_y += nave_vel_y

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