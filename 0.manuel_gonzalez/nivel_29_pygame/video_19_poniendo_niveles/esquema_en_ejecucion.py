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
pygame.display.set_caption("VIDEO 19 - ESQUEMA EN EJECUCION")

reloj = pygame.time.Clock()
fuente1 = pygame.font.SysFont("arial black", 20)
fuente2 = pygame.font.SysFont("Segoe print", 32)

# Carga imágenes
fondo = pygame.image.load("fondo.png").convert()

nave_arr = pygame.image.load("nave_arriba.png").convert_alpha()
nave_abj = pygame.image.load("nave_abajo.png").convert_alpha()
nave_izq = pygame.image.load("nave_izquierda.png").convert_alpha()
nave_der = pygame.image.load("nave_derecha.png").convert_alpha()

aste_1a = pygame.image.load("asteroide_1a.png").convert_alpha()
aste_1b = pygame.image.load("asteroide_1b.png").convert_alpha()
aste_1c = pygame.image.load("asteroide_1c.png").convert_alpha()
aste_1d = pygame.image.load("asteroide_1d.png").convert_alpha()

aste_1 = [aste_1a, aste_1b, aste_1c, aste_1d]
aste_3 = [aste_1b, aste_1a, aste_1d, aste_1c]
aste_4 = [aste_1c, aste_1d, aste_1a, aste_1b]
aste_5 = [aste_1d, aste_1c, aste_1b, aste_1a]

aste_2a = pygame.image.load("asteroide_2a.png").convert_alpha()
aste_2b = pygame.image.load("asteroide_2b.png").convert_alpha()
aste_2c = pygame.image.load("asteroide_2c.png").convert_alpha()
aste_2d = pygame.image.load("asteroide_2d.png").convert_alpha()

aste_2 = [aste_2a, aste_2b, aste_2c, aste_2d]
aste_6 = [aste_2b, aste_2a, aste_2d, aste_2c]
aste_7 = [aste_2c, aste_2d, aste_2a, aste_2b]
aste_8 = [aste_2d, aste_2c, aste_2b, aste_2a]


instrucciones_en_inicio = [
            "- Iterando dentro del bucle en_inicio",
            "- ESC o X para salir. ENTER para entrar al bucle en_partida",
            "- el bucle principal es en_juego, pero cuando inicia, solo setea la",
            "cantidad de vidas y el nivel en 3 y 1, y luego entra al bucle en_inicio",
            "- si damos ENTER, se entra en el bucle en_partida (en cuyo ambito estaremos la mayor parte del tiempo)",
            "que setea la cantidad de asteroides segun el nivel, sus valores random de inicio y se inicializa en_final = False,", 
            "que sera la variable evaluada para entrar al ultimo while en_final. Luego de estos seteos entra", 
            "automaticamente en el bucle en_nivel",
            "",
            "while en_juego",
            "   while en_inicio",
            "   while en_partida",
            "       while en_nivel",
            "       while en_final",
            ]

instrucciones_en_nivel = [
            "BIENVENIDO! YA ESTAS JUGANDO EN EL NIVEL 1 CON 3 VIDAS!!",
            "",
            " -Iterando dentro del bucle en_nivel",
            "- ESC o X para salir.",
            "- aca de salida se juega en el nivel que venga seteado desde el bucle",
            "principal en_juego (variable num_nivel, inicialmente 1) y esta toda la logica del juego",
            "- va salir de este bucle (ademas de las opciones de salida) si la nave supera el nivel actual (num_nivel += 1)", 
            "o si colisiona con algun asteroide (num_vidas -= 1), en cuyos casos en_nivel = False",
            "- si num_vidas == 0 o num_nivel > 3 (tiene que haberse superado un nivel o haberse perdido una vida,",
            " es decir, en_nivel = False para salir del bucle actual), se pone en_final = True", 
            "con lo que al salir de en_nivel va a entrar en en_final",
            "- si se pierde vida sin llegar a 0 o supera el nivel sin superar el 3, va a salir de en_nivel", 
            "pero no va a entrar en en_final, por lo cual se vuelve a iterar el bucle en_partida que setea la cantidad", 
            "de asteroides segun el nivel, sus valores random de inicio, y se inicializa en_final = False, que sera la variable", 
            "evaluada para entrar al ultimo while en_final. Luego de estos seteos vuelve a entrar en el bucle en_nivel,",
            "pero ahora en el mismo nivel con una vida menos, o en un nivel superior",
            "",
            "while en_juego",
            "   while en_inicio",
            "   while en_partida",
            "       while en_nivel",
            "       while en_final",
            "'g' o 'p' para simular que se acabaron las vidas o se superaron los 3 niveles para entrar en en_final",
            ]

instrucciones_en_final = [
            " -Iterando dentro del bucle en_final",
            "- ESC o X para salir.",
            "- entrando a este bucle, significa que el jugador perdio todas las vidas, o supero todos los niveles",
            "- entonces solo se imprime la leyenda que corresponda segun el caso y se escucha por los eventos keydown 'n'", 
            "para salir o 's' para volver a jugar",
            "",
            "¿Volver a jugar?",
            "'n' para salir o 's' para volver a jugar (se vuelve a entrar a en_juego)",
            "",
            "if 's':",
            "   en_final = False",
            "   en_partida = False",
            "",
            "if 'n':",
            "   en_final = False",
            "   en_partida = False",
            "   en_juego = False",
            "",
            "while en_juego",
            "   while en_inicio",
            "   while en_partida",
            "       while en_nivel",
            "       while en_final",
            ]

# Bucle principal
en_juego = True
while en_juego:

    num_vidas = 3
    num_nivel = 1

    en_partida = False
    en_inicio = True
   
    while en_inicio:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == \
                pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                en_inicio = False
                en_juego = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    en_inicio = False
                    en_partida = True
                    
        ventana.fill(NEGRO)

        y = 10
        for renglon in instrucciones_en_inicio:
            texto = fuente1.render(renglon, True, BLANCO)
            ventana.blit(texto, (10, y))
            y += 30

        pygame.display.update()

    while en_partida:
        en_final = False
        
        en_nivel = True
        while en_nivel: 

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == \
                    pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    en_nivel = False
                    en_partida = False
                    en_juego = False
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_g or \
                    event.key == pygame.K_p):
                    en_nivel = False
                    en_final = True
            
            ventana.fill(NEGRO)

            y = 10
            for renglon in instrucciones_en_nivel:
                texto = fuente1.render(renglon, True, BLANCO)
                ventana.blit(texto, (10, y))
                y += 30

            pygame.display.update()
        
        while en_final:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == \
                    pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_n)):
                    en_final = False
                    en_partida = False
                    en_juego = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        en_final = False
                        en_partida = False
            
            ventana.fill(NEGRO)

            y = 10
            for renglon in instrucciones_en_final:
                texto = fuente1.render(renglon, True, BLANCO)
                ventana.blit(texto, (10, y))
                y += 30

            pygame.display.update()

pygame.quit()


# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_19_poniendo_niveles
# python esquema_en_ejecucion.py