import pygame
import copy

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


# Mapa


mapa1 = [
    "         F      ",
    " F            F ",
    "   AFAAF        ",
    "   AAAFA   MM   ",
    "   F       MM  F",
    "           MM   ",
    "           MM   ",
    " F    P         ",
    "              F "
    ]


mapa2 = [
    "    P         F ",
    "         AAFA   ",
    " F       FAAA   ",
    "         AFAA   ",
    "     F          ",
    "F  SSSS         ",
    "   SSSS     F   ",
    "                ",
    "       F      F "
    ]


# Funciones

def construir_mapa(superficie, mapa):
    limites = []
    frutas = []
    puertas = []
    x = 0
    y = 0
    for linea in mapa:
        for baldosa in linea:
            if baldosa == "M":
                limites.append([baldosa_muro, pygame.Rect(x, y, 80, 80)])
            elif baldosa == "S":
                limites.append([baldosa_agua, pygame.Rect(x, y, 80, 80)])
            elif baldosa == "A":
                limites.append([baldosa_arbol, pygame.Rect(x, y, 80, 80)])
            elif baldosa == "F":
                frutas.append([baldosa_manzana, pygame.Rect(x, y, 80, 80)])
            elif baldosa == "P":
                puertas.append([baldosa_puerta, pygame.Rect(x, y, 80, 80)])
            x += 80
        x = 0
        y += 80
    return limites, frutas, puertas # tupla de listas


# Ventana

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("VIDEO 26 CLASE 1")

reloj = pygame.time.Clock()

imagen_fondo = pygame.image.load("fondo_mapa.png").convert()

baldosa_muro = pygame.image.load("baldosa_muro.png").convert()
baldosa_agua = pygame.image.load("baldosa_agua.png").convert()
baldosa_arbol = pygame.image.load("baldosa_arbol.png").convert_alpha()
baldosa_puerta = pygame.image.load("baldosa_puerta.png").convert_alpha()
baldosa_manzana = pygame.image.load("baldosa_manzana.png").convert_alpha()

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

# Datos

habitacion1 = construir_mapa(ventana, mapa1) # tupla de listas (lista_limites, lista_frutas, lista_puertas) lista_limites = [[surface arbol, rect arbol], [surface muro, rect muro], [surface agua, rect agua]]
habitacion2 = construir_mapa(ventana, mapa2) # tupla de listas (lista_limites, lista_frutas, lista_puertas) 

habitacion = habitacion1

jugador_rectangulo = jugador_imagen.get_rect()
# print(jugador_rectangulo)
jugador_rectangulo.x = 100
jugador_rectangulo.y = 300
# print(jugador_rectangulo)
jugador_vel_x = 0
jugador_vel_y = 0
frames_jugador = 0

# Bucle principal

jugando = True
while jugando:

    reloj.tick(60)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # por cada iteracion reseteamos las variables que usamos para simular moviemiento del player
    moviendose_derecha = False
    moviendose_izquierda = False
    moviendose_arriba = False
    moviendose_abajo = False

    # por cada iteracion reseteamos en 0 las variables de movimiento en x y en y del player
    jugador_vel_x = 0
    jugador_vel_y = 0

    pulsado = pygame.key.get_pressed() # get_pressed() recoge el estado de cada una de las teclas del teclado (True si esta pulsada, False si no lo esta)

    if pulsado[pygame.K_LEFT] and not pulsado[pygame.K_RIGHT]:
        jugador_vel_x = -3
        moviendose_izquierda = True
    if pulsado[pygame.K_RIGHT] and not pulsado[pygame.K_LEFT]:
        jugador_vel_x = 3
        moviendose_derecha = True
    if pulsado[pygame.K_UP] and not pulsado[pygame.K_DOWN]:
        jugador_vel_y = -3
        moviendose_arriba = True
    if pulsado[pygame.K_DOWN] and not pulsado[pygame.K_UP]:
        jugador_vel_y = 3
        moviendose_abajo = True

    # Lógica

    jugador_rectangulo.x += jugador_vel_x
    jugador_rectangulo.y += jugador_vel_y

    # nos aseguramos que el jugador no se salga de la pantalla
    if jugador_rectangulo.x > ANCHO - 60:
        jugador_rectangulo.x = ANCHO - 60
    if jugador_rectangulo.x < 0:
        jugador_rectangulo.x = 0
    if jugador_rectangulo.y > ALTO - 60:
        jugador_rectangulo.y = ALTO - 60
    if jugador_rectangulo.y < 0:
        jugador_rectangulo.y = 0

    # aplico logica de muros
    # habitacion = (lista_limites, lista_frutas, lista_puertas) 
    # habitacion[0] = [[surface arbol, rect arbol], [surface muro, rect muro], [surface agua, rect agua]]
    for limite in habitacion[0]:
        if jugador_rectangulo.colliderect(limite[1]):
            jugador_rectangulo.x -= jugador_vel_x
            jugador_rectangulo.y -= jugador_vel_y

    # aplico logica de comer manzanas y que dezaparezcan
    # habitacion[1] = [[surface manzana, rect manzana], [surface manzana, rect manzana], [surface manzana, rect manzana]]
    # iteramos la copia de la lista de manzanas para evitar errores (explicacion en video_24/clase1.py)
    for fruta in copy.copy(habitacion[1]): 
        if jugador_rectangulo.collidepoint(fruta[1].centerx, fruta[1].centery):
            habitacion[1].remove(fruta)

    # habitacion[2] = [[surface puerta, rect puerta]]
    # habitacion1 = tupla de listas (lista_limites, lista_frutas, lista_puertas) de mapa1
    # habitacion2 = tupla de listas (lista_limites, lista_frutas, lista_puertas) de mapa2
    for puerta in habitacion[2]:
        if jugador_rectangulo.collidepoint(puerta[1].centerx, puerta[1].centery):
            if habitacion == habitacion1:
                habitacion = habitacion2
                jugador_rectangulo.x = 400
                jugador_rectangulo.y = 60
            else:
                habitacion = habitacion1
                jugador_rectangulo.x = 560
                jugador_rectangulo.y = 620
                
    # Dibujos

    ventana.blit(imagen_fondo, (0,0))

    # dibujamos todos los objetos del mapa sobre el fondo de la pantalla
    # habitacion = tupla de listas (lista_limites, lista_frutas, lista_puertas)
    for elemento in habitacion:
        # elemento = [[surface arbol, rect arbol], [surface muro, rect muro], [surface agua, rect agua]]
        # elemento = [[surface manzana, rect manzana], [surface manzana, rect manzana], [surface manzana, rect manzana]]
        # elemento = [[surface puerta, rect puerta]]
        for baldosa in elemento:
            ventana.blit(baldosa[0], baldosa[1])

    # simulacion del jugador corriendo hacia las distintas direcciones (renderizacion de sprites segun contador de frames)
    if moviendose_derecha: # el usuario esta pulsando flecha derecha PERO NO flecha izquierda
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

    elif moviendose_izquierda: # el usuario esta pulsando flecha izquierda PERO NO flecha derecha
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

    elif moviendose_arriba: # el usuario esta pulsando flecha arriba PERO NO flecha abajo
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

    elif moviendose_abajo: # el usuario esta pulsando flecha abajo PERO NO flecha arriba
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
           
    else: # el usuario NO esta moviendo al jugador
        jugador_imagen = jugador0_par
        ventana.blit(jugador_imagen, jugador_rectangulo)
  

    # Actualizar
    pygame.display.update()


# Salir
pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_26_habitaciones
# python clase1.py