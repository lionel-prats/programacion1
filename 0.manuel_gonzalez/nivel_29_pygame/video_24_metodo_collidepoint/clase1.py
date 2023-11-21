import pygame

# Inicializar
pygame.init()

# Medidas
ANCHO = 1280
ALTO = 720

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
CLARO = (200, 165, 120)
MARRON = (120, 60, 20)

# Mapas

# mapa = [
#     "XXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXXXX",
#     "X              X",
#     "X XXXXXX XXXXX X",
#     "X XXXXXX  XXXX X",
#     "X XXX XX XXXXX X",
#     "X              X",
#     "XXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXXXX"
#     ]
mapa = [
    "XXXXXXXXXXXXXXXX",
    "XXXFXXXXXXXXXFXX",
    "X              X",
    "X XXXXXX XXXXX X",
    "X XXXFXX  FXXX X",
    "X XXX XX XXXXF X",
    "X              X",
    "XXXXXXFXXXXXXXXX",
    "XXXXXXXXXXXXXXXX"
    ]


# Funciones

def dibujar_muro(superficie, rectangulo):
    pygame.draw.rect(superficie, MARRON, rectangulo)

def dibujar_manzana(superficie, rectangulo):
    pygame.draw.rect(superficie, VERDE, rectangulo)

def dibujar_personaje(superficie, rectangulo):
    pygame.draw.rect(superficie, AZUL, rectangulo)

def construir_mapa(mapa):
    muros = []
    manzanas = []
    x = 0
    y = 0
    for fila in mapa:
        for baldosa in fila:
            if baldosa == "X":
                muros.append(pygame.Rect(x, y, 80, 80))
            if baldosa == "F":
                manzanas.append(pygame.Rect(x+20, y+20, 40, 40))
            x += 80
        x = 0
        y += 80
    return muros, manzanas


def dibujar_mapa(superficie, muros, manzanas):
    for muro in muros:
        dibujar_muro(superficie, muro)
    for manzana in manzanas:
        dibujar_manzana(superficie, manzana)
        


# Ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

# Datos

# la funcion construir_mapa retorna 2 listas, guardo una en cada variable
muros, manzanas = construir_mapa(mapa)

personaje = pygame.Rect(100, 400, 40, 40)
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
                personaje_vel_x = 10
            if event.key == pygame.K_LEFT:
                personaje_vel_x = -10
            if event.key == pygame.K_DOWN:
                personaje_vel_y = 10
            if event.key == pygame.K_UP:
                personaje_vel_y = -10
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

    for muro in muros:
        if personaje.colliderect(muro):
            personaje.x -= personaje_vel_x
            personaje.y -= personaje_vel_y

    # - busco remover elementos de la lista de manzanas si hay colision con el player
    # - itero la lista con un for y valido con colliderect
    # - si itero la lista original (manzanas), puede generar errores
    # - la solucion esta en iterar una copia de la lista -> list(manzanas)
    # for manzana in list(manzanas):
    #     if personaje.colliderect(manzana):
    #         manzanas.remove(manzana)

    # collidepoint(coordX, coordY) recibe un punto de coordenadas, y retorna un bool indicando si hubo colision entre el objeto que lo invoca y el punto x,y especificado
    for manzana in list(manzanas):
        # if personaje.collidepoint(manzana.centerx, manzana.centery):
        if personaje.collidepoint(manzana.center):
            manzanas.remove(manzana)
    
    # ejemplo para entender el metodo collidepoint() de la clase Rect
    # if personaje.collidepoint(100,250):
    #     print("COLISION TOP")
    # elif personaje.collidepoint(100,500):
    #     print("COLISION BOTTOM")
            
    # Dibujos
    ventana.fill(CLARO)

    # dibuja la lista de muros y la de manzanas (ambas son listas con objetos rect de 80x80 y con coordenadas de acuerdo a la matriz mapa)
    dibujar_mapa(ventana, muros, manzanas)
    
    dibujar_personaje(ventana, personaje)


    # Actualizar
    pygame.display.update()


# Salir
pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_24_metodo_collidepoint
# python clase1.py