import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ancho, alto = 800, 800
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Movimiento Diagonal")

# Configuración de la superficie roja
ancho_superficie_roja, alto_superficie_roja = 128, 128
superficie_roja = pygame.Surface((ancho_superficie_roja, alto_superficie_roja))
superficie_roja.fill((255, 0, 0))  # Rellenar con un color rojo

# Configuración de la superficie amarilla
ancho_superficie_amarilla, alto_superficie_amarilla = 128, 128
superficie_amarilla = pygame.Surface((ancho_superficie_amarilla, alto_superficie_amarilla))
superficie_amarilla.fill((255, 255, 0))  # Rellenar con un color amarillo

# Coordenadas iniciales para ambas superficies
x_roja, y_roja = 0, 672
# x_roja, y_roja = 200, 300
x_amarilla, y_amarilla = 0, 0

# Velocidad de movimiento para ambas superficies
velocidad = 2

# Direcciones iniciales para ambas superficies
direccion_roja = "arriba-izquierda"
direccion_amarilla = "abajo-derecha"

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar coordenadas para la superficie roja
    if direccion_roja == "arriba-izquierda":
        x_roja += velocidad
        y_roja -= velocidad
    else:  # direccion_roja == "abajo-derecha"
        x_roja -= velocidad
        y_roja += velocidad

    # Cambiar dirección para la superficie roja
    if x_roja > ancho - ancho_superficie_roja or y_roja < 0:
        direccion_roja = "abajo-derecha"
    elif x_roja < 0 or y_roja > alto - alto_superficie_roja:
        direccion_roja = "arriba-izquierda"

    # Actualizar coordenadas para la superficie amarilla
    if direccion_amarilla == "arriba-izquierda":
        x_amarilla -= velocidad
        y_amarilla -= velocidad
    else:  # direccion_amarilla == "abajo-derecha"
        x_amarilla += velocidad
        y_amarilla += velocidad

    # Cambiar dirección para la superficie amarilla
    if x_amarilla > ancho - ancho_superficie_amarilla or y_amarilla > alto - alto_superficie_amarilla:
        direccion_amarilla = "arriba-izquierda"
    elif x_amarilla < 0 or y_amarilla < 0:
        direccion_amarilla = "abajo-derecha"
        x_amarilla, y_amarilla = 0, 0  # Restablecer las coordenadas a (0, 0)

    # Limpiar pantalla
    pantalla.fill((0, 0, 0))

    # Dibujar superficies en las coordenadas actuales
    pantalla.blit(superficie_roja, (x_roja, y_roja))
    pantalla.blit(superficie_amarilla, (x_amarilla, y_amarilla))

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.Clock().tick(60)

"""  
bueno, ahora dame el siguiente codigo 

pantralla de 800 * 800 

una unica superficie de 100 * 100 

bliteada en una posicion random entre 0 y 700 de x, y 0 y 700 de y

la idea es que de saslida se mueva en diagonal arriba a la derecha, incrementando 1px por cada iteracion

la idea es que segun al borde de la pantalla que llegue primero (borde eje x o borde eje y) cambie la direccion del recorrido diagonal segun corresponda

ejemplo:

bliteo inicial en 200, 300 entonces arranca describiendo una diagonal arriba a la derecha

como va a hacer tope primero contra el eje x (es decir, y va a ser 0 antes que x 800) entonces al hacer tope la direccion tiene que pasar a ser abajo-derecha

hace tu mejor esfuerzo, no me defraudes


"""