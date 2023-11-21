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

# Funciones
def nave_arriba(superficie, x, y):
    pygame.draw.rect(superficie, VERDE, (x, y, 60, 60))
    pygame.draw.rect(superficie, NEGRO, (x, y, 15, 30))
    pygame.draw.rect(superficie, NEGRO, (x+45, y, 15, 30))

def nave_abajo(superficie, x, y):
    pygame.draw.rect(superficie, VERDE, (x, y, 60, 60))
    pygame.draw.rect(superficie, NEGRO, (x, y+30, 15, 30))
    pygame.draw.rect(superficie, NEGRO, (x+45, y+30, 15, 30))

def nave_derecha(superficie, x, y):
    pygame.draw.rect(superficie, VERDE, (x, y, 60, 60))
    pygame.draw.rect(superficie, NEGRO, (x+30, y, 30, 15))
    pygame.draw.rect(superficie, NEGRO, (x+30, y+45, 30, 15))

def nave_izquierda(superficie, x, y):
    pygame.draw.rect(superficie, VERDE, (x, y, 60, 60))
    pygame.draw.rect(superficie, NEGRO, (x, y, 30, 15))
    pygame.draw.rect(superficie, NEGRO, (x, y+45, 30, 15))

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

direccion = "arriba"

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
                nave_vel_x = 10
            if event.key == pygame.K_LEFT:
                direccion = "izquierda"
                nave_vel_x = -10
            if event.key == pygame.K_DOWN:
                direccion = "abajo"
                nave_vel_y = 10
            if event.key == pygame.K_UP:
                direccion = "arriba"
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

    if direccion == "arriba":
        nave_arriba(ventana,nave_pos_x, nave_pos_y)
    elif direccion == "derecha":
        nave_derecha(ventana,nave_pos_x, nave_pos_y)
    elif direccion == "abajo":
        nave_abajo(ventana,nave_pos_x, nave_pos_y)
    else:
        nave_izquierda(ventana,nave_pos_x, nave_pos_y)

    # Actualizar
    pygame.display.update()



# Salir
pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_13_cambiando_orientacion_de_las_figuras
# python 0.inicial.py