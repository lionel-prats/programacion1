import pygame
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 100)) # tamañp jugador
        self.image.fill((255, 255, 255)) # tamañp jugador
        self.rect = self.image.get_rect(center=(screen_width/2, screen_height/2)) # tamañp jugador
    def update(self):
        self.rect.center = pygame.mouse.get_pos() # mouse al centro el jugador para poder moverlo
    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0]) 

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface((50, 10)) # tamañp proyectil
        self.image.fill((255, 0, 0)) # color proyectil
        self.rect = self.image.get_rect(center=(pos_x, pos_y)) # posicion proyectil
    def update(self):
        self.rect.x += 10
        if self.rect.x >= screen_width +100:
            self.kill()

# Basics
pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height= 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.mouse.set_visible(False) # invisivilizo el mouse

# Player
player = Player() # instancio el jugador
player_group = pygame.sprite.Group()
player_group.add(player)

# Bullet 
bullet_group = pygame.sprite.Group()

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_group.add(player.create_bullet())

    # Drawing
    screen.fill((30, 30, 30))
    bullet_group.draw(screen)
    player_group.draw(screen)
    player_group.update()
    bullet_group.update()
    pygame.display.flip()
    clock.tick(60)