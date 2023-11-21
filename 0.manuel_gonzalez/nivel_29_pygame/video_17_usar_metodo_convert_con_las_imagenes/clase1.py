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

# DOCUMENTACION METODO CONVERT
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert

# Ventana
ventana = pygame.display.set_mode((ANCHO, ALTO)) # objeto de tipo superficie <Surface(1280x720x32 SW)>
pygame.display.set_caption("VIDEO 17 CLASE 1")
reloj = pygame.time.Clock()

# fuente
fuente = pygame.font.SysFont("arial", 20)

# imagenes
fondo = pygame.image.load("images/fondo_espacio_exterior.png").convert() # objeto de tipo superficie <Surface(1280x720x24 SW)>
asteroide_1a = pygame.image.load("images/asteroide_1a.png").convert() 
asteroide_1a.set_colorkey(BLANCO)

asteroide_2a = pygame.image.load("images/asteroide_2a.png").convert_alpha() 

nave_arriba = pygame.image.load("images/nave_arriba.png").convert() 
nave_arriba = pygame.transform.scale(nave_arriba, (40, 40))
nave_arriba.set_colorkey(BLANCO)

# variables para manejar el control del tiempo transcurido
transcurrido = 0


jugando = True
while jugando:

    # reloj.tick(60)

    transcurrido += reloj.tick()
    print(transcurrido)
    
    fps = reloj.get_fps()

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
    ventana.blit(asteroide_1a, (350,200))
    ventana.blit(asteroide_2a, (1050,400))
    ventana.blit(nave_arriba, (500,550))
        
    fps_por_segundo = fuente.render(f"FPS: {str(fps)}", True, BLANCO)
    ventana.blit(fps_por_segundo, (20,20))

    pygame.display.update()


# Salir
pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_17_usar_metodo_convert_con_las_imagenes
# python clase1.py
