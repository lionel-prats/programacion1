import pygame
import sys
import random

class Crosshair(pygame.sprite.Sprite):
    __score = 0
    __cantidad_disparos = 0
    def __init__(self, picture_path):
        super().__init__()
        # Carga la imagen de la mira desde un archivo
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()  # Obtiene el rectángulo que rodea la imagen
        # Carga el sonido de disparo desde un archivo
        self.gunshot = pygame.mixer.Sound('shoot.mp3')

    def shoot(self):
        cantidad_anterior_objetivos = len(target_group) 

        self.gunshot.play()  # Reproduce el sonido de disparo
        pygame.sprite.spritecollide(crosshair, target_group, True)
        
        cantidad_actual_objetivos = len(target_group) 

        self.__score += (cantidad_anterior_objetivos - cantidad_actual_objetivos) * 100

        if cantidad_anterior_objetivos > cantidad_actual_objetivos:
            print(f"Puntaje actual: {self.get_score()}")
        if cantidad_actual_objetivos == 0:
            win = True
            print("\n¡Ganaste!\n")
            # pygame.quit()  
            # sys.exit()

    def get_score(self):
        return self.__score

    def update(self):
        # Actualiza la posición de la mira para seguir el cursor del mouse
        self.rect.center = pygame.mouse.get_pos()

    def get_cantidad_disparos(self):
        self.__cantidad_disparos += 1
        return self.__cantidad_disparos

class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        # Carga la imagen del objetivo desde un archivo
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()  # Obtiene el rectángulo que rodea la imagen
        # Establece la posición inicial del objetivo
        self.rect.center = [pos_x, pos_y]

    def mover_target(self):
        x = random.randrange(-100, 100)
        y = random.randrange(-100, 100)

        nueva_coordenada_x = self.rect.x + x
        nueva_coordenada_y = self.rect.y + y
        
        if nueva_coordenada_x >= 0 and nueva_coordenada_x <= 600:
            self.rect.x = nueva_coordenada_x
        if nueva_coordenada_y >= 0 and nueva_coordenada_y <= 600:
            self.rect.y = nueva_coordenada_y


# Configuración general del juego
pygame.init()
clock = pygame.time.Clock()

# Configuración de la pantalla del juego
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Fondo del juego
# Carga la imagen de fondo desde un archivo
background = pygame.image.load('BG.png')
pygame.mouse.set_visible(False)  # Oculta el cursor del mouse

# Mira del jugador
crosshair = Crosshair('crosshair.png')  # Crea una instancia de la mira
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)  # Agrega la mira al grupo

# Objetivos
cantidad_objetivos = 10
target_group = pygame.sprite.Group()
for target in range(cantidad_objetivos):
    new_target = Target('target.png', random.randrange(
        0, screen_width), random.randrange(0, screen_height))
    target_group.add(new_target)  # Agrega objetivos al grupo

# contador_cuenta_regresiva = 3 
contador_cuenta_regresiva = 20 

texto_cuenta_regresiva = f"Te quedan {contador_cuenta_regresiva} segundos"
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

win = False
print(f"Puntaje actual: {crosshair.get_score()}")

mensaje_ganaste = "¡Ganaste!"

contador_disparos = crosshair.get_cantidad_disparos()

# Bucle principal del juego
while True:

    if not len(target_group):
        screen.blit(font.render(mensaje_ganaste, True, (0, 0, 0)), (screen_width / 2 - 80, screen_height / 2 - 100))
        
    for event in pygame.event.get():
        if len(target_group) and event.type == pygame.USEREVENT: 
            if contador_cuenta_regresiva > 0:
                contador_cuenta_regresiva -= 1
            if contador_cuenta_regresiva > 0:
                texto_cuenta_regresiva = f"Te quedan {contador_cuenta_regresiva} segundos"
            else:
                texto_cuenta_regresiva = "¡GAME OVER!"
        
        if event.type == pygame.QUIT:
            pygame.quit()  # Sale del juego si se cierra la ventana
            sys.exit()
        if contador_cuenta_regresiva > 0 and not win and len(target_group) and event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()  # Llama al método shoot() cuando se hace clic
    
    if contador_cuenta_regresiva > 0 and not win:
        pass
        if len(target_group):
            list(target_group)[random.randrange(0, len(target_group))].mover_target()

    screen.blit(font.render(texto_cuenta_regresiva, True, (0, 0, 0)), (32, 48))
    
    pygame.display.flip()  # Actualiza la pantalla
    screen.blit(background, (0, 0))  # Dibuja el fondo en la pantalla

    target_group.draw(screen)  # Dibuja los objetivos en la pantalla
    crosshair_group.draw(screen)  # Dibuja la mira en la pantalla

    crosshair_group.update()  # Actualiza la posición de la mira
    clock.tick(60)  # Controla la velocidad del juego a 60 cuadros por segundo

