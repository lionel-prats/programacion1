import pygame
import sys


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # Llama al constructor de la clase padre (pygame.sprite.Sprite)
        # self.image = pygame.Surface((100, 100))
        # self.image.fill((255, 255, 255))
        self.image = pygame.image.load('player_ship.png') # Carga la imagen del jugador desde el archivo 'player_ship.png'
        self.rect = self.image.get_rect(center=(screen_width/2, screen_height/2)) # Obtiene un objeto Rect asociado a la imagen y lo coloca en el centro de la pantalla

    def update(self):
        self.rect.center = pygame.mouse.get_pos() # Actualiza la posición del rectángulo del jugador al seguir la posición del ratón

    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]) # Crea y devuelve un objeto de la clase Bullet en la posición actual del ratón


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        # self.image = pygame.Surface((50, 10))
        # self.image.fill((255, 0, 0))
        self.image = pygame.image.load('player_laser.png')
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
    
    def update(self):
        self.rect.x += 10

        if self.rect.x >= screen_width + 100:
            self.kill()

# Basics
pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.mouse.set_visible(False)

# Player
player = Player()
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
    screen.fill((30,30,30))
    bullet_group.draw(screen) # Dibujar todos los Sprites en la pantalla
    player_group.draw(screen)
    player_group.update() # Group(player.update()) # Actualizar todos los Sprites en el grupo
    bullet_group.update()
    pygame.display.flip()
    clock.tick(60)