import pygame
import sys
import random
import os

class Auxiliar:
    @staticmethod
    def limpiar_consola():
        if os.name in ["ce", "nt", "dos"]:  # windows
            os.system("cls")
        else:  # linux o mac
            os.system("clear")

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound('shoot.mp3')

    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.direction_x = random.choice([-1, 1])  # Dirección aleatoria en el eje x
        self.direction_y = random.choice([-1, 1])  # Dirección aleatoria en el eje y

    def update(self):
        # Mueve el objetivo en cada fotograma
        self.rect.x += self.direction_x * random.randint(1, 35)
        self.rect.y += self.direction_y * random.randint(1, 35)

        # Asegura que el objetivo permanezca dentro de la pantalla
        self.rect.x = max(0, min(self.rect.x, screen_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, screen_height - self.rect.height))

        # Cambia la dirección en el eje x de manera aleatoria
        if random.randint(1, 100) == 1:
            self.direction_x *= -1

        # Cambia la dirección en el eje y de manera aleatoria
        if random.randint(1, 100) == 1:
            self.direction_y *= -1

Auxiliar.limpiar_consola()

pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load('BG.png')
pygame.mouse.set_visible(False)

crosshair = Crosshair('crosshair.png')
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

target_group = pygame.sprite.Group()
for target in range(10):
    new_target = Target('target.png', random.randrange(0, screen_width), random.randrange(0, screen_height))
    target_group.add(new_target)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

    screen.blit(background, (0, 0))

    target_group.update()  # Actualiza la posición de los objetivos
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()

    pygame.display.flip()
    clock.tick(60)
