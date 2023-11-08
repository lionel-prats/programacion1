import pygame as pg
from models.constantes import (ANCHO_VENTANA, ALTO_VENTANA, FPS)
from models.player.main_player import Jugador


screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA)) 
pg.init() 

clock = pg.time.Clock()
back_img = pg.image.load('./assets/img/background/goku_house.jpg')

back_img = pg.transform.scale(back_img, (ANCHO_VENTANA, ALTO_VENTANA)) # ajusto el tamaño de la imagen al tamaño del screen


juego_ejecutandose = True

vegeta = Jugador(0, 0, frame_rate = 70, speed_walk = 20, speed_run = 40)

while juego_ejecutandose:

    # delta_ms = clock.tick(FPS)
    # print(delta_ms)

    lista_eventos = pg.event.get()
    
    for event in lista_eventos:
        match event.type:
            # case pg.KEYDOWN: # evento "tecla apretada"
            #     if event.key == pg.K_SPACE: # K_SPACE constante con un valor numerico unico para identificar la barra espaciadora
            #         print("estoy apretando el espacio")
            # case pg.KEYUP: # evento "tecla soltada"
            #     if event.key == pg.K_SPACE: # K_SPACE constante con un valor numerico unico para identificar la barra espaciadora
            #         print("estoy soltando el espacio")
            
                    # print("estoy soltando el espacio")
            case pg.QUIT: 
                print("estoy cerrando el juego")
                juego_ejecutandose = False
                break # salgo de la iteracion del for

    lista_teclas_presionadas = pg.key.get_pressed()
    # if lista_teclas_presionadas[pg.K_e]:
    #     if delta_ms == 16:
    #         print("estoy manteniendo apretado la tecla E")

    if lista_teclas_presionadas[pg.K_RIGHT] and not lista_teclas_presionadas[pg.K_LEFT]:
        vegeta.walk("Right") 
    if lista_teclas_presionadas[pg.K_LEFT] and not lista_teclas_presionadas[pg.K_RIGHT]:
        vegeta.walk("Left") 
    if not lista_teclas_presionadas[pg.K_RIGHT] and not lista_teclas_presionadas[pg.K_LEFT]:
        vegeta.stay() 
    
    
    
    
    screen.blit(back_img, back_img.get_rect()) 
    delta_ms = clock.tick(FPS)
    # print(delta_ms)
    vegeta.update(delta_ms)
    pg.display.update()

pg.quit()

    #     if evento.type == pygame.QUIT:
    #         ejecutar_juego = False

    # # renderizamos los objetos en pantalla
    # screen.blit(screen_background_image, (0, 0)) 
    # screen.blit(tabla_puntajes, tabla_puntajes_coordenadas)
    # screen.blit(titulo_string, titulo_coordenadas)
    # screen.blits(lista_puestos_objetos)
    # screen.blit(boton_objeto, boton_objeto_coordenadas)

    # # confirmamos la impresion
    # pygame.display.flip() 