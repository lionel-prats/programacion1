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
pygame.display.set_caption("VIDEO 19 - CLASE 1")

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

historia = [
            "                      MISIÓN A JUPITER",
            "     Tras meses de viaje en misión a Júpiter ya sólo se",
            "    interponen en tu camino tres cinturones de asteroides",
            "  que te dificultan el paso y amenazan con no dejarte pasar.",
            "   Intenta traspasarlos para conseguir finalizar tu misión.",
            "",
            "                Pulsa 'ENTER' para empezar"
            ]

historia_perdido = [
                "    No has conseguido llegar a Júpiter. Los cinturones",
                "   de asteroides han destruido tu nave. Pero has tenido",
                "   suerte y te han recogido unos chatarreros del espacio.",
                "  ¿Quieres volverlo a intentar a borde de una nueva nave?",
                "",
                "              Pulsa 's' para volverlo a intentar",
                "              Pulsa 'n' para salir del juego"]

historia_ganado = [
    "  Has conseguido llegar a Júpiter y completar tu misión.",
    "  Los cinturones de asteroides no han conseguido pararte.",
    "       Te has convertido en un héroe del espacio.",
    "       ¿Quieres embarcarte en una nueva misión?",
    "", 
    "              Pulsa 's' para volver a jugar",
    "              Pulsa 'n' para salir del juego"]
    
# Bucle principal
en_juego = True
while en_juego:
    print("en_juego")
    num_vidas = 3
    num_nivel = 1

    en_partida = False
    en_inicio = True
    
    while en_inicio:
        print("en_inicio")
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
        
        y = 80
        for frase in historia:
            texto = fuente2.render(frase, True, BLANCO)
            ventana.blit(texto, (150, y))
            y += 80

        pygame.display.update()

    while en_partida:
        print("en_partida")
        en_final = False
        
        num_aste_grandes = num_nivel * 5
        num_aste_pequenios = num_nivel * 10

        asteroides_grandes = []
        asteroides_pequenios = []

        for i in range(num_aste_grandes):
            f = random.choice([aste_1, aste_3, aste_4, aste_5])
            x = random.randint(0, ANCHO)
            y = random.randint(50, ALTO-120)
            v = random.randint(1, 3)
            asteroide_con_data = [f, x, y, v]
            asteroides_grandes.append(asteroide_con_data)
            
        for i in range(num_aste_pequenios):
            f = random.choice([aste_2, aste_6, aste_7, aste_8])
            x = random.randint(0, ANCHO)
            y = random.randint(50, ALTO-120)
            v = random.randint(1, 4)
            asteroide_con_data = [f, x, y, v]
            asteroides_pequenios.append(asteroide_con_data)

        # fusiono en una nueva lista, lista de asteroides_grandes y lista de asteroides_chicos
        asteroides = asteroides_grandes + asteroides_pequenios

        # posicion inicial de la nave + seteo de direccion para que cuando inicia se blitee la nave mirando hacia arriba
        nave_pos_x = 600
        nave_pos_y = 670
        nave_vel_x = 0
        nave_vel_y = 0
        direccion = "arriba"

        frames_asteroides = 0

        en_nivel = True
        while en_nivel:     
            print("en_nivel")

            reloj.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == \
                    pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    en_nivel = False
                    en_partida = False
                    en_juego = False

                if event.type == pygame.KEYDOWN:
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

            # herramientas de desarrollo para simular ganar o perder el juego
            # if event.type == pygame.KEYDOWN and (event.key == pygame.K_g or \
            #     event.key == pygame.K_p):
            #     en_nivel = False
            #     en_final = True

            # ---------- Lógica ----------

            # actualizo las posiciones en x de los asteroides grandes previo al blit
            for a in asteroides_grandes:
                a[1] += a[3]
                if a[1] > ANCHO:
                    a[1] = -64

            # actualizo las posiciones en x de los asteroides chicos previo al blit
            for a in asteroides_pequenios:
                a[1] += a[3]
                if a[1] > ANCHO:
                    a[1] = -32
            
            # actualizo la posiciones en x e y de la nave previo al blit fijando limites respecto a la ventana
            nave_pos_x += nave_vel_x
            nave_pos_y += nave_vel_y
            if nave_pos_x > ANCHO - 32:
                nave_pos_x = ANCHO - 32
            if nave_pos_x < 0:
                nave_pos_x = 0
            if nave_pos_y > ALTO - 32:
                nave_pos_y = ALTO - 32
            
            # valido si la nave supero el nivel en juego
            if nave_pos_y < 10:
                en_nivel = False
                num_nivel += 1
                
            # valido si la nave colisiono con alguno de los asteroides grandes
            for a in asteroides_grandes:
                if colision(a[1], a[2], 64, 64, nave_pos_x, nave_pos_y, 32, 32, ex=0):
                    en_nivel = False
                    num_vidas -= 1

            # valido si la nave colisiono con alguno de los asteroides chicos
            for a in asteroides_pequenios:
                if colision(a[1], a[2], 32, 32, nave_pos_x, nave_pos_y, 32, 32, ex=0):
                    en_nivel = False
                    num_vidas -= 1

            # el jugador perdio las 3 vidas
            # ganado la usamos para saber que historia final mostrar
            if num_vidas == 0:
                ganando = False
                en_final = True

            # el jugador supero los 3 niveles
            # ganado la usamos para saber que historia final mostrar
            if num_nivel > 3:
                ganando = True
                en_final = True

            # ---------- Imagenes ----------

            ventana.blit(fondo, (0,0))

            texto1 = fuente1.render("Nivel: " + str(num_nivel), True, BLANCO)
            texto2 = fuente1.render("Vidas: " + str(num_vidas), True, BLANCO)
            ventana.blit(texto1, (20,10))
            ventana.blit(texto2, (1150, 10))


            frames_asteroides += 1
            if frames_asteroides >= 41:
                frames_asteroides = 1
            
            # bliteo la imagen de cada uno de los 20 asteroides (0° 90° 180° 270°) segun el conteo de frames
            # la posicion en x se actualiza arriba, en la parte de logica de este bucle
            if frames_asteroides < 11:
                for a in asteroides:
                    ventana.blit(a[0][0], (a[1], a[2]))
                    pygame.draw.rect(ventana, BLANCO, (a[1], a[2], 32, 32), 2)
            elif frames_asteroides < 21:
                for a in asteroides:
                    ventana.blit(a[0][1], (a[1], a[2]))
                    pygame.draw.rect(ventana, BLANCO, (a[1], a[2], 32, 32), 2)
            elif frames_asteroides < 31:
                for a in asteroides:
                    ventana.blit(a[0][2], (a[1], a[2]))
                    pygame.draw.rect(ventana, BLANCO, (a[1], a[2], 32, 32), 2)
            elif frames_asteroides < 41:
                for a in asteroides:
                    ventana.blit(a[0][3], (a[1], a[2]))
                    pygame.draw.rect(ventana, BLANCO, (a[1], a[2], 32, 32), 2)
            
            # bliteo de la nave en la posicion y direccion de imagen que corresponda segun los keydown y keyup
            if direccion == "arriba":    
                ventana.blit(nave_arr, (nave_pos_x, nave_pos_y))
            elif direccion == "abajo":    
                ventana.blit(nave_abj, (nave_pos_x, nave_pos_y))
            elif direccion == "izquierda":    
                ventana.blit(nave_izq, (nave_pos_x, nave_pos_y))
            elif direccion == "derecha":    
                ventana.blit(nave_der, (nave_pos_x, nave_pos_y))
            pygame.draw.rect(ventana, BLANCO, (nave_pos_x, nave_pos_y, 32, 32), 2)

            pygame.display.update()
            
        while en_final:
            print("en_final")
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

            if ganando:
                historia_final = historia_ganado
            else:
                historia_final = historia_perdido

            y = 80
            for frase in historia_final:
                texto = fuente2.render(frase, True, BLANCO)
                ventana.blit(texto, (150, y))
                y += 80

            pygame.display.update()

pygame.quit()


# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_19_poniendo_niveles
# python clase1.py