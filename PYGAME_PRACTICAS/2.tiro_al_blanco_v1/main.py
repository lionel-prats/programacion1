import pygame
import sys
import random
from classes.Auxiliar import Auxiliar as Aux

Aux.limpiar_consola()

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()  
        # self.rect.center((400, 400))
        self.gunshot = pygame.mixer.Sound('shoot.mp3')

    def shoot(self):
        self.gunshot.play()
        # print("BOOM")
        pygame.sprite.spritecollide(crosshair, target_group, True)
        # pygame.sprite.spritecollide(target_group, crosshair, True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
                           
class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()  
        self.rect.center = [pos_x, pos_y]
    
    def target_control(self, direction = "top-right"):
        match direction:
            case "bottom-right":
 
                self.rect.x += 0.1
                self.rect.y += 0.1
            case "bottom-left":
                self.rect.x -= 1
                self.rect.y -= 1
            case "top-left":
                self.rect.x -= 1
                self.rect.y += 1
            case _:
                if self.rect.x < 672:
                    # print(self.rect)
                    self.rect.x += 1
                    self.rect.y -= 1
    
    def change_direction_to(direction):
        pass

    
        
        # x = random.randrange(-100, 100)
        # y = random.randrange(-100, 100)

        # nueva_coordenada_x = self.rect.x + x
        # nueva_coordenada_y = self.rect.y + y
        
        # if nueva_coordenada_x >= 0 and nueva_coordenada_x <= 600:
        #     self.rect.x = nueva_coordenada_x
        # if nueva_coordenada_y >= 0 and nueva_coordenada_y <= 600:
        #     self.rect.y = nueva_coordenada_y

# -----------------------------------------------------------------------------------------

pygame.init()


screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.mouse.set_visible(False)

background = pygame.image.load('BG.png')

# mira
crosshair = Crosshair('crosshair.png') 


crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair) 


# blancos
target_group = pygame.sprite.Group()
for target in range(10):
    new_target = Target(
        picture_path='target.png', 
        pos_x=random.randrange(64, screen_width - 64), 
        pos_y=random.randrange(64, screen_height - 64)
    )
    target_group.add(new_target)  

target_demo = Target(
    picture_path='target.png', 
    pos_x=0, 
    pos_y=800
)
target_demoX = 0
target_demoY = 672
bornX = target_demoX
bornY = target_demoY
finalX = 0
finalY = 0

while True:


    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

    screen.blit(background, (0, 0)) 

    crosshair_group.update()

    # target_group.draw(screen)
    crosshair_group.draw(screen) 

    # list(target_group)[random.randrange(0, len(target_group))].mover_target()
    # list(target_group)[5].target_control(direction="top-right")
    

    # list(target_group)[6].mover_target(direction="bottom-right")
    # list(target_group)[7].mover_target(direction="bottom-left")
    # list(target_group)[8].mover_target(direction="top-left")


    if bornX == 0 and bornY == 672:
        finalX = 672
        finalY = 0
        if target_demoX < 672:
            target_demoX += 2
            target_demoY -= 2
        else:
            target_demoX -= 2
            target_demoY += 2

    screen.blit(target_demo.image, (target_demoX, target_demoY))
    print(target_demoX, target_demoY)

    # target_demo.target_control()


    

    pygame.display.flip() # o pygame.display.update()









# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/PYGAME_PRACTICAS/2.tiro_al_blanco_v1/
# python main.py

"""  
Tiro al blanco
1. Movimiento aleatorio de objetivos (targets)
2. Crear targets de distinto tamaño y puntaje de forma aleatoria
3. Cantidad de blancos acertados por tiempo
4. Mostrar tiempo de juego en pantalla y luego finalizar a los 30 segundos.
5. Mostrar en pantalla los puntos por target
"""