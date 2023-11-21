import pygame 
from pygame.locals import * 

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 1000
screen_height  = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("VIDEO 6 - PROFESOR")

# define game variables 
tile_size = 50

# load images 
sun_img = pygame.image.load("img/sun.png")
bg_img = pygame.image.load("img/sky.png")

def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(surface=screen, color=(255, 255, 255), start_pos=(0, line * tile_size), end_pos=(screen_width, line * tile_size), width=1) # lineas paralelas al eje x de la pantalla
		pygame.draw.line(surface=screen, color=(255, 255, 255), start_pos=(line * tile_size, 0), end_pos=(line * tile_size, screen_height), width=1) # lineas paralelas al eje y de la pantalla

class Player():
    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1,5):
            img_right = pygame.image.load(f"img/guy{num}.png")
            img_right = pygame.transform.scale(img_right, (40,80))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]    
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        
    def update(self):
        
        dx = 0
        dy = 0
        walk_cooldown = 5

        key = pygame.key.get_pressed() # get kypresses

        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -15 
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= 5
            self.counter += 1
            self.direction = -1
        if key[pygame.K_RIGHT]:
            dx += 5
            self.counter += 1
            self.direction = 1
        if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
            self.counter = 0
            self.index = 0
            if self.direction == 1: # player moving to the right
                self.image = self.images_right[self.index]
            if self.direction == -1: # player moving to the right
                self.image = self.images_left[self.index]

        # handle animation
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right) - 1:
                self.index = 0
            if self.direction == 1: # player moving to the right
                self.image = self.images_right[self.index]
            if self.direction == -1: # player moving to the right
                self.image = self.images_left[self.index]
            # self.image = self.images_right[self.index]


        # add gravity 
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y # -14|-13|-12...9|10|10|10

        # print(world.tile_list[54][1].colliderect(self.rect))
       
        # check for collision
        for tile in world.tile_list: 

            # check for collision in x direction 
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height): # dx = +/-5 or 0
                dx = 0

            # if tile[1].colliderect(self.rect): 
            # tile == (<Surface(50x50x24 SW)>, <rect(400, 900, 50, 50)>)
            # check for collision in y direction 
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height): 
                
                # hay colision entre el player y alguno de los tiles
                # check if below the ground i.e jumping 
                # self.vel_y toma valores entre de entr -14 y 1 (durante la curva de un salto), y de entre 0 y 10 con  el player en reposo
                if self.vel_y < 0: # el player esta durante la curva de un salto, entonces la colision es entre rl bottom del tile y el top del player
                    dy = tile[1].bottom - self.rect.top # 0
                    self.vel_y = 0
                # check if above the ground i.e falling
                elif self.vel_y >= 0: # el player esta en reposo, entonces la colision es entre el bottom del player y el top del tile
                    dy = tile[1].top - self.rect.bottom # 0
                    self.vel_y = 0

        # update player coordinates
        self.rect.x += dx 
        self.rect.y += dy 

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            dy = 0

        screen.blit(self.image, self.rect) # draw player onto screen
        pygame.draw.rect(screen, (255,0,0), self.rect, 2)

class World():
    def __init__(self, data):
        
        self.tile_list = []

        #load images 
        dirt_img = pygame.image.load("img/dirt.png") 
        grass_img = pygame.image.load("img/grass.png") 
        
        row_count = 0
        for row in data: 
            col_count = 0
            for tile in row: 
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    blob = Enemy(col_count * tile_size, row_count * tile_size + 15)
                    blob_group.add(blob)
                if tile == 6:
                    pass

                     
                col_count += 1
            row_count += 1
        

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, (255,255,255), tile[1], 2)

# class Enemy():
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/blob.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        
        self.rect.x += self.move_direction

        # bloque para el movimiento de los enemigos
        # se moveran a derecha e izquierda durante +/-50 pixeles de su ubicacion original
        # self.move_counter ira de -51 a 50, luego de 50 vuelve a -51, en loop infinito
        # durante este tiempo los enemigos se iran moviendo en un sentido
        # cuando self.move_counter se reinicia en -51, los enemigos cambian de direccion
        # sib abs() aparentemente funciona igual
        self.move_counter += 1 
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1

class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/lava.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2)) # // parte entera del cociente de la division
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # self.move_direction = 1
        # self.move_counter = 0


world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1], 
[1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1], 
[1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

player = Player(100, screen_height - 50)
# player = Player(350, 50)

blob_group = pygame.sprite.Group()



world = World(world_data)

run = True
while run:
    # print(player.rect)

    clock.tick(fps)

    screen.blit(bg_img, (0,0))
    screen.blit(sun_img, (100,100))
    
    world.draw()

    # .draw -> metodo de la clase Group para blitear los elementos de un objeto de tipo Group (sprite)
    # .update -> metodo de la clase Group que busca y ejecuta el metodo update() de los sprites que tenga dentro
    blob_group.update()
    blob_group.draw(screen)
    pygame.draw.rect(screen, (255,0,0), (550,500,50,50), 2)

    player.update()
    # draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == \
            pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False

    
    
    pygame.display.update()

pygame.quit()


# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/PYGAME_PRACTICAS/4.juego_tipo_mario/video6/video_06
# python con_comentarios.py
