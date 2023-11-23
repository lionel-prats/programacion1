import pygame as pg

from models.constantes import (
    ALTO_VENTANA, ANCHO_VENTANA, FPS
)
from models.player.main_player import Jugador
from stage import Stage

screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pg.init()
clock = pg.time.Clock()

back_img = pg.image.load('./assets/img/background/goku_house.png')
back_img = pg.transform.scale(back_img, (ANCHO_VENTANA, ALTO_VENTANA))

juego_ejecutandose = True
stage_number = 1
stage = None
bkg_1 = './assets/img/background/goku_house.png'
bkg_2 = './assets/img/background/cell_arena.jpg'

vegeta = Jugador(50, 350, frame_rate=70, speed_walk=20, speed_run=40)

while juego_ejecutandose:
    # actualizo el background de mi stage
    match stage_number:
        case 1:
            background = bkg_1
        case 2:
            background = bkg_2
        case 3:
            background = bkg_1
    
    # si no instancie ningun stage AUN o ya gane el stage (checkeando la condicion de victoria), instancio el siguiente
    if not stage or stage.stage_passed():
        stage = Stage(screen, vegeta, background, ANCHO_VENTANA, ALTO_VENTANA, f'stage_{stage_number}', 300)
        stage_number += 1 # incremento en 1 el stage para cuando tenga que volver a instanciar el nuevo

    # Para despues de tener los 3 niveles:
    # si gane todos los niveles
    # actualizo la BD con el nombre del jugador y su puntaje


    lista_eventos = pg.event.get()
    for event in lista_eventos:
        match event.type:
            case pg.QUIT:
                print('Estoy CERRANDO el JUEGO')
                juego_ejecutandose = False
                break
    
    lista_teclas_presionadas = pg.key.get_pressed()
    screen.blit(stage.bkg_img, stage.bkg_img.get_rect())
    delta_ms = clock.tick(FPS)
    stage.run(delta_ms, lista_teclas_presionadas)
    pg.display.update()

pg.quit()
