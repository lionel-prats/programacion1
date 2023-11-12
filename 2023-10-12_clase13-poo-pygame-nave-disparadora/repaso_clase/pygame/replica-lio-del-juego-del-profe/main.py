import pygame
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 

        # atributo de Player/cargo la imagen de la nave
        self.image = pygame.image.load('player_ship.png') 

        # atributo de Player / obtengo el rectangulo de la nave y la posiciona en el centro de la pantalla/ventana -> (400, 400)
        self.rect = self.image.get_rect( center = ( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 ) ) 
       
    def update(self):
        """  
        reposiciona self.rect (la nave) segun la posicion del puntero del mouse
        """
        self.rect.center = pygame.mouse.get_pos() # pygame.mouse.get_pos() == (154, 711)

    def create_bullet(self):
        """ 
        crea un objeto instancia de la clase Bullet
        se le pasan al constructor de Bullet las coordenadas "x" e "y" del mouse
        """
        return Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]) 

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('player_laser.png')
        self.rect = self.image.get_rect(center=(pos_x, pos_y)) # obtengo el rectangulo del proyectil y lo posiciono en la pantalla/ventana
    
    def update(self):

        # incremento en 10 pixeles la coordenada x del proyectil 
        self.rect.x += 10

        # borro de memoriael objeto proyectil 100 pixeles a la derecha del borde derecho de la pantalla
        if self.rect.x >= SCREEN_WIDTH + 100:
            self.kill()

pygame.init()
clock = pygame.time.Clock() # 

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800 # ancho y alto de la pantalla/ventana
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # objeto pantalla/ventana (?)
pygame.mouse.set_visible(False) # oculto el puntero del mouse fusionado con la nave

# Nave
player = Player() # <Player Sprite(in 0 groups)>
player_group = pygame.sprite.Group() # <class 'pygame.sprite.Group'> | <Group(0 sprites)>
player_group.add(player) # <Group(1 sprites)>

# Proyectil
bullet_group = pygame.sprite.Group() # <class 'pygame.sprite.Group'> | <Group(0 sprites)>

contador = 0
while True:
    for event in pygame.event.get():
        # evento click en la x superior derecha de la pantalla/ventana para salir del programa
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit() 
        
        # evento click del usuario en alguna parte de la pantalla/ventana
        if event.type == pygame.MOUSEBUTTONDOWN:
            # creo una instancia de Bullet (proyectil) por cada click del mouse en la pantalla/ventana y la agrego al grupo de Bullets
            bullet_group.add(player.create_bullet())

    screen.fill((30,30,30)) # background-color de la ventana/pantalla
    
    player_group.draw(screen) # renderizo el grupo de naves (1 sola) en la pantalla/ventana
    bullet_group.draw(screen) # renderizo el grupo de proyectiles (en la medida que se creen) en la pantalla/ventana

    # al parecer se ejecuta Player.update, que reposiciona la nave de acuerdo al movimiento del mouse
    player_group.update()
    # al parecer se ejecuta Bullet.update para todas las instancias de Bullet en bullet_group, que reposiciona el proyectil 10 pixeles a la derecha por cada iteracion del while
    bullet_group.update()

    # renderizo todo el contenido de la pantalla/ventana
    pygame.display.flip() 
    
    # creo que tiene que ver con los FPS (frames por segundo)
    clock.tick(60)
    print(clock)
    print(f"iteracion {contador}")
    contador += 1