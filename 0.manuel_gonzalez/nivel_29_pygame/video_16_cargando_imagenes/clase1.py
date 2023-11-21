import pygame

# Inicializar
pygame.init()

# Medidas
ANCHO = 1280
ALTO = 720

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
NARANJA = (255, 128, 0)
VERDE = (0, 255, 0)

# Ventana
ventana = pygame.display.set_mode((ANCHO, ALTO)) # objeto de tipo superficie <Surface(1280x720x32 SW)>
pygame.display.set_caption("VIDEO 16 CLASE 1")
reloj = pygame.time.Clock()

# imagenes
fondo = pygame.image.load("images/fondo_espacio_exterior.png") # objeto de tipo superficie <Surface(1280x720x24 SW)>
asteroide_1a = pygame.image.load("images/asteroide_1a.png") 
asteroide_1a.set_colorkey(BLANCO)

asteroide_2a = pygame.image.load("images/asteroide_2a.png") 

nave_arriba = pygame.image.load("images/nave_arriba.png") 
nave_arriba = pygame.transform.scale(nave_arriba, (40, 40))
nave_arriba.set_colorkey(BLANCO)


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
            
   
    # imagenes
    ventana.fill(VERDE)
    ventana.blit(fondo, (0,0))
    ventana.blit(asteroide_1a, (200,200))
    ventana.blit(asteroide_2a, (400,400))
    ventana.blit(nave_arriba, (500,550))
        
    

    pygame.display.update()


# Salir
pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_16_cargando_imagenes
# python clase1.py