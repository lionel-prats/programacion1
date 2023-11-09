import pygame as pg

from models.constantes import (
    ALTO_VENTANA, ANCHO_VENTANA, FPS
)
from models.player.main_player import Jugador # importo clase Jugador

screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pg.init()
clock = pg.time.Clock()

back_img = pg.image.load('./assets/img/background/goku_house.png')
back_img = pg.transform.scale(back_img, (ANCHO_VENTANA, ALTO_VENTANA))


juego_ejecutandose = True

vegeta = Jugador(coord_x=0, coord_y=0, frame_rate=70, speed_walk=20, speed_run=40) # instancia de Jugador


while juego_ejecutandose:
    
    #print(delta_ms)
    lista_eventos = pg.event.get()
    for event in lista_eventos:
        print(event.type)
        match event.type:
            case pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    vegeta.jump(True)
            # case pg.KEYUP:
            #     if event.key == pg.K_SPACE:
            #         print('Estoy SOLTANDO el espacio')
            case pg.QUIT: # pg.QUIT == 256 (es el click sobre la "x" del borde superior derecho de la ventana)
                juego_ejecutandose = False
                break
    
    lista_teclas_presionadas = pg.key.get_pressed()
    # if lista_teclas_presionadas[pg.K_SPACE]:
    #     vegeta.jump()
    if lista_teclas_presionadas[pg.K_RIGHT] and not lista_teclas_presionadas[pg.K_LEFT]:
        vegeta.walk('Right')
    if lista_teclas_presionadas[pg.K_LEFT] and not lista_teclas_presionadas[pg.K_RIGHT]:
        vegeta.walk('Left')
    if not lista_teclas_presionadas[pg.K_RIGHT] and not lista_teclas_presionadas[pg.K_LEFT]:
        vegeta.stay()
    
    if lista_teclas_presionadas[pg.K_RIGHT] and lista_teclas_presionadas[pg.K_LSHIFT] and not lista_teclas_presionadas[pg.K_LEFT]:
        vegeta.run('Right')
    if lista_teclas_presionadas[pg.K_LEFT] and lista_teclas_presionadas[pg.K_LSHIFT] and not lista_teclas_presionadas[pg.K_RIGHT]:
        vegeta.run('Left')
    
        
    
    screen.blit(back_img, back_img.get_rect())
    delta_ms = clock.tick(FPS)
    vegeta.update(delta_ms)
    vegeta.draw(screen)
    pg.display.update()

pg.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/2023-11-07_clase19_M-pygame-vegeta1/juego_vegeta_lionel_replica_ANDA/
# python main.py