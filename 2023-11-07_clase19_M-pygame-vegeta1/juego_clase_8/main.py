""" 
Alumno: Lionel Prats 
DNI: 31367577
División: 1H
Nro. legajo: 115678
Pygame
"""

import pygame # importo libreria pygame
from data_jugadores import lista_diccionarios_jugadores
from utils import *

# inicializo pygame 
pygame.init() 

# constantes
ANCHO_CONTENEDOR = 800
ALTO_CONTENEDOR = 600

# creo y seteo las dimensiones de la pantalla
pantalla = pygame.display.set_mode((ANCHO_CONTENEDOR, ALTO_CONTENEDOR)) 
# cargo el background-image de la pantalla en una variable
pantalla_background_image = pygame.image.load(r'assets\img\fondo.png')

# cargo la imagen de la tabla en una variable
tabla_puntajes = pygame.image.load(r'assets\img\tabla_puntajes.png')
# obtengo el ancho de la imagen (en px)
tabla_puntajes_ancho = tabla_puntajes.get_width()
# print(11 // 2) # 5 -> cociente de la division
# tupla con las coordenadas de la imagen de la tabla -> (coordenada_x, coordenada_y)
tabla_puntajes_coordenadas = ( (ANCHO_CONTENEDOR - tabla_puntajes_ancho) // 2, 10)

# cargamos la fuente del titulo
titulo_objeto = pygame.font.Font(r'assets\fonts\Halimount.otf', 50)
titulo_string = titulo_objeto.render("Puntajes", True, (255, 255, 255))
# obtengo el ancho del titulo (en px)
titulo_ancho = titulo_string.get_width()
titulo_coordenadas = ((ANCHO_CONTENEDOR - titulo_ancho) // 2, 35)

# Cargamos la fuente para los textos de la tabla
tabla_render = pygame.font.Font(r'assets\fonts\Halimount.otf', 35)

# --------------------------------

# lista de tuplas con los posiciones, nombres y puntajes para renderizar vvv
# [("1.", (260,135)), ("celest", (300,135)), ("0100", (460,135)), ("2.", (260,185)), ("ivan", (300,185)), ("0090", (460,185))]
lista_puestos_objetos = []

y = 135

for jugador in lista_diccionarios_jugadores:
    # El color del texto del nombre del primer jugador va a ser blanco
    if not len(lista_puestos_objetos):
        color_txt = (255, 255, 255)
    else:
        color_txt = (109, 30, 3)

    posicion_objeto = tabla_render.render(str(jugador["nro"]), True, (255, 76, 114))
    nombre_jugador_objeto = tabla_render.render(formatear_nombre_jugador(str(jugador["nombre"])), True, color_txt)
    puntaje_objeto = tabla_render.render(formatear_puntaje(str(jugador["puntaje"])), True, color_txt)

    lista_puestos_objetos.append((posicion_objeto, (260, y)))
    lista_puestos_objetos.append((nombre_jugador_objeto, (300, y)))
    lista_puestos_objetos.append((puntaje_objeto, (460, y)))

    y += 50

# Creamos el texto del boton
boton_objeto_font_family = pygame.font.Font(r'assets\fonts\Halimount.otf', 30)
boton_objeto = boton_objeto_font_family.render("Jugar de nuevo", True, (255,255,255))
boton_objeto_ancho = boton_objeto.get_width()
boton_objeto_coordenadas = ((ANCHO_CONTENEDOR - boton_objeto_ancho) // 2, 515)

# --------------------------------

ejecutar_juego = True

while ejecutar_juego:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            ejecutar_juego = False

    # renderizamos los objetos en pantalla
    pantalla.blit(pantalla_background_image, (0, 0)) 
    pantalla.blit(tabla_puntajes, tabla_puntajes_coordenadas)
    pantalla.blit(titulo_string, titulo_coordenadas)
    pantalla.blits(lista_puestos_objetos)
    pantalla.blit(boton_objeto, boton_objeto_coordenadas)

    # confirmamos la impresion
    pygame.display.flip() 

pygame.quit() # Fin