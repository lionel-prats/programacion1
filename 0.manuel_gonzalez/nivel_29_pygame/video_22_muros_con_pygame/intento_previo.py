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
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)
VIOLETA = (138, 43, 226)

# Ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("VIDEO 22 - CLASE 0")
rect_ventana = ventana.get_rect()

reloj = pygame.time.Clock()

# Datos

# objeto de la clase Rect
naveObjectoRec = pygame.Rect(700, 500, 50, 50)
naveObjectoRec.center = (ventana.get_width()/2, 600) 
nave_vel_x = 0
nave_vel_y = 0

# rocas
roca_top_left = pygame.Rect(150, 0, 100,400)
roca_top_right = pygame.Rect(rect_ventana.width-250, 0, 100, 400)
roca_bottom_right = pygame.Rect(450, rect_ventana.height-400, 100, 400)
roca_bottom_left = pygame.Rect(rect_ventana.width-550, rect_ventana.height-400, 100, 400)

# lista_muros = [(roca_top_left, ROJO), (roca_top_right, AZUL), (roca_bottom_right, AMARILLO), (roca_bottom_left, VIOLETA)]
lista_muros = [(roca_top_left, VERDE), (roca_top_right, VERDE), (roca_bottom_right, VERDE), (roca_bottom_left, VERDE)]

print(rect_ventana.x - 250)


def colision(objeto1, objeto2):
    if objeto1.colliderect(objeto2):
        return True
    else:
        return False

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
                nave_vel_x = 10
            if event.key == pygame.K_LEFT:
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

    # actualizamos posicion en x e y del objeto Rect
    naveObjectoRec.x += nave_vel_x
    naveObjectoRec.y += nave_vel_y
    
    # objeto clase Rect - controlamos que no se salga de la pantalla
    if naveObjectoRec.x > ANCHO - naveObjectoRec.width:
        naveObjectoRec.x = ANCHO - naveObjectoRec.width
    if naveObjectoRec.x < 0:
        naveObjectoRec.x = 0
    if naveObjectoRec.y > ALTO - naveObjectoRec.height:
        naveObjectoRec.y = ALTO - naveObjectoRec.height
    if naveObjectoRec.y < 0:
        naveObjectoRec.y = 0

    # valido si hay colision entre la nave y alguno de los muros (si la hay modifico la coordenada que corresponda de la nave para que haga tope)
    for muro in lista_muros:
        if colision(naveObjectoRec, muro[0]):
            naveObjectoRec.x -= nave_vel_x
            naveObjectoRec.y -= nave_vel_y

    # Dibujos
    ventana.fill(NEGRO)

    # dibujo los 4 muros
    for muro in lista_muros:
        pygame.draw.rect(ventana, muro[1], muro[0])

    # pygame.draw.rect(ventana, VERDE, naveObjectoRec)
    pygame.draw.rect(ventana, AZUL, naveObjectoRec)

    # Actualizar
    pygame.display.update()


# Salir
pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_22_muros_con_pygame
# python intento_previo.py