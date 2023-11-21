import pygame

# Inicializar
pygame.init()

# Medidas
ANCHO = 1280
ALTO = 720

# Colores
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

# Ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

# Datos

# objeto de la clase Rect
naveObjectoRec = pygame.Rect(700, 500, 50, 50)

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
            if event.key == pygame.K_ESCAPE:
                jugando = False
            if event.key == pygame.K_RIGHT:
                nave_vel_x = 5
            if event.key == pygame.K_LEFT:
                nave_vel_x = -5
            if event.key == pygame.K_DOWN:
                nave_vel_y = 5
            if event.key == pygame.K_UP:
                nave_vel_y = -5
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

    # actualizamos posicion en x e y del objeto Rect
    naveObjectoRec.x += nave_vel_x
    naveObjectoRec.y += nave_vel_y

    # actualizamos posicion en x e y del rectangulo
    nave_pos_x += nave_vel_x
    nave_pos_y += nave_vel_y

    # rectangulo - controlamos que no se salga de la pantalla
    if nave_pos_x > ANCHO - 50:
        nave_pos_x = ANCHO - 50
    if nave_pos_x < 0:
        nave_pos_x = 0
    if nave_pos_y > ALTO - 50:
        nave_pos_y = ALTO - 50
    if nave_pos_y < 0:
        nave_pos_y = 0
    
    # objeto clase Rect - controlamos que no se salga de la pantalla
    if naveObjectoRec.x > ANCHO - naveObjectoRec.width:
        naveObjectoRec.x = ANCHO - naveObjectoRec.width
    if naveObjectoRec.x < 0:
        naveObjectoRec.x = 0
    if naveObjectoRec.y > ALTO - naveObjectoRec.height:
        naveObjectoRec.y = ALTO - naveObjectoRec.height
    if naveObjectoRec.y < 0:
        naveObjectoRec.y = 0
        
    # Dibujos

    ventana.fill(NEGRO)

    pygame.draw.rect(ventana, AZUL, (nave_pos_x, nave_pos_y, 50, 50))
    pygame.draw.rect(ventana, VERDE, naveObjectoRec)

    # Actualizar
    pygame.display.update()


# Salir
pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_20_clase_rect
# python clase1.py