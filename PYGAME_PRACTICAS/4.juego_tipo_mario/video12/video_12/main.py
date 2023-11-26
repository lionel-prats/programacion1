import pygame 
from pygame.locals import * 
from pygame import mixer # mixer para sonidos v11
import pickle
from os import path


# mixer para sonidos v11
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 1000
screen_height  = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("VIDEO 12 - PROFESOR")

# define font
font = pygame.font.SysFont("Bauhaus 93", 70) # <pygame.font.Font object at 0x0000016AE72CE550> 
font_score = pygame.font.SysFont("Bauhaus 93", 30) # <pygame.font.Font object at 0x000001B8BEE8E4C0> 
# los numeros del final varian cada vez que ejecuto main.py (tendra que ver con el espacio en memoria donde se aloja?)


# define game variables 
tile_size = 50
game_over = 0
main_menu = True
level = 3
max_levels = 7
score = 0 # monedas capturadas

# define colours 
white = (255, 255, 255)
blue = (0, 0, 255)

# load images 
sun_img = pygame.image.load("img/sun.png")
bg_img = pygame.image.load("img/sky.png")
restart_img = pygame.image.load("img/restart_btn.png")
start_img = pygame.image.load("img/start_btn.png")
exit_img = pygame.image.load("img/exit_btn.png")

# load sounds v11
# pygame.mixer.music.load("img/music.wav")
# pygame.mixer.music.play(-1, 0.0, 5000) # 5000 -> volumen musica de fondo in crescendo durante 5 segs hasta llegar al 100% del volumen seteado
# pygame.mixer.music.set_volume(0.1)
coin_fx = pygame.mixer.Sound("img/coin.wav")
coin_fx.set_volume(0)
jump_fx = pygame.mixer.Sound("img/jump.wav")
jump_fx.set_volume(0)
game_over_fx = pygame.mixer.Sound("img/game_over.wav")
game_over_fx.set_volume(0)


def draw_text(text, font, text_col, x, y):
    # img = font.render(text, antialias=True, text_col)
    img = font.render(text, True, text_col) # surface de tipo Font <Surface(41x34x32 SW)>
    # print(img.get_rect().height)
    # print(img.get_rect())
    screen.blit(img, (x,y))

def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(surface=screen, color=(255, 255, 255), start_pos=(0, line * tile_size), end_pos=(screen_width, line * tile_size), width=1) # lineas paralelas al eje x de la pantalla
		pygame.draw.line(surface=screen, color=(255, 255, 255), start_pos=(line * tile_size, 0), end_pos=(line * tile_size, screen_height), width=1) # lineas paralelas al eje y de la pantalla

# function to reset level
def reset_level(level):
    player.reset(100, screen_height - 50) # reseteo los atributos del platyer para que se blitee en la posicion inicial luego de pasar de nivel y ya en el nuevo escenario
    # player.reset(850, 50)
    blob_group.empty() # empty() -> metodo de la clase Group() que elimina todos los sprites de un objeto Group
    lava_group.empty()
    exit_group.empty()
    if path.exists(f"level{level}_data"): # load in level data and create world
        pickle_in = open(f"level{level}_data", "rb") # read binary
        world_data = pickle.load(pickle_in)
        pickle_in.close()
    world = World(world_data) # nueva instancia de World con el mapa del nivel que corresponda
    return world

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        """  
        verifica si el usuario hace click sobre el boton restart cuando el player pierde una vida\n
        retorna True en caso de click, False en caso contrario
        """
        
        action =  False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # collidepoint() -> metodo de la clase Rect que nos indica si el mouse pasa por encima de un objeto Rect
        # check mouseover and clicked condition
        if self.rect.collidepoint(pos):
            # pygame.mouse.get_pressed() -> (bool, bool, bool) -> tupla que nos indica si alguno de los 3 botones del mouse esta presionado
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        # draw button
        screen.blit(self.image, self.rect)

        return action

class Player():
    def __init__(self, x, y):
        self.reset(x, y)
        
    def update(self, game_over):
        dx = 0
        dy = 0
        walk_cooldown = 5
        
        if game_over == 0:

            key = pygame.key.get_pressed() # get kypresses

            if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
                jump_fx.play() # v11
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
        
            # check for collision with tiles
            self.in_air = True
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
                        self.in_air = False
                        
            # check for collision with enemies 
            if pygame.sprite.spritecollide(self, blob_group, False):
                game_over = -1
                game_over_fx.play() # v11
            
            # check for collision with lava 
            if pygame.sprite.spritecollide(self, lava_group, False):
                game_over = -1
                game_over_fx.play() # v11
            
            # check for collision with exit
            if pygame.sprite.spritecollide(self, exit_group, False):
                game_over = 1

            # update player coordinates
            self.rect.x += dx 
            self.rect.y += dy 

            # if self.rect.bottom > screen_height:
            #     self.rect.bottom = screen_height
            #     dy = 0

        # el player perdio la vida, animacion del fantasma subiendo
        if game_over == -1:
            self.image = self.dead_image
            draw_text("GAME OVER!", font, blue, (screen_width//2)-200, (screen_height//2))
            # draw_text("GAME OVER", font, blue, (screen_width - 359) / 2, (screen_height - 80) / 2)
            if self.rect.y > 200:
                self.rect.y -= 5

        screen.blit(self.image, self.rect) # draw player onto screen
        pygame.draw.rect(screen, (255,0,0), self.rect, 2)

        return game_over

    def reset(self, x, y):
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
        self.dead_image = pygame.image.load("img/ghost.png")
        self.image = self.images_right[self.index]    
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True


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
                if tile == 4: # plataformas con movimiento en eje X v12
                    platform = Platform(col_count * tile_size, row_count * tile_size, 1, 0)
                    platform_group.add(platform)
                if tile == 5: # plataformas con movimiento en eje Y v12
                    platform = Platform(col_count * tile_size, row_count * tile_size, 0, 1)
                    platform_group.add(platform)
                if tile == 6:
                    lava = Lava(col_count * tile_size, row_count * tile_size + (tile_size // 2))
                    lava_group.add(lava)
                if tile == 7:
                    coin = Coin(col_count * tile_size + (tile_size//2), row_count * tile_size +  (tile_size//2))
                    coin_group.add(coin)
                if tile == 8:
                    exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size // 2))
                    exit_group.add(exit)

                     
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
        if abs(self.move_counter) > 50: # 50f tor, 100f tol, 100f tor, 100f tol
            self.move_direction *= -1
            self.move_counter *= -1

# v12
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, move_x, move_y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/platform.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size//2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_counter = 0
        self.move_direction = 1
        self.move_x = move_x
        self.move_y = move_y


    def update(self):
        
        self.rect.x += self.move_direction * self.move_x # si self.move_x == 1 se movera sobre el eje X, si 0 no lo hara 
        self.rect.y += self.move_direction * self.move_y # si self.move_y == 1 se movera sobre el eje Y, si 0 no lo hara
        self.move_counter += 1 

        if abs(self.move_counter) > 50: # 50f tor, 100f tol, 100f tor, 100f tol
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
        self.counter = 0

    def update(self):
        self.counter += 1
        if self.counter > 15:
            self.image = pygame.transform.flip(self.image, True, False)
            self.counter = 0

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/coin.png')
        self.image = pygame.transform.scale(img, (tile_size//2, tile_size//2))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/exit.png')
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
        self.rect = self.image.get_rect()
        # print(self.rect)
        self.rect.x = x
        self.rect.y = y

player = Player(100, screen_height - 50)
# player = Player(350, 50)

blob_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group() # v12
lava_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()

# create a dummy coin for showing the score 
score_coin = Coin(tile_size // 2, tile_size // 2) # (25,25) -> para que quede centrada en el tile 0,0, ya que la clase Coin le aplica a coin.png un transform de 25x25
coin_group.add(score_coin) 

# load in level data and create world
if path.exists(f"level{level}_data"):
    pickle_in = open(f"level{level}_data", "rb") # read binary
    world_data = pickle.load(pickle_in)
    pickle_in.close()

world = World(world_data)

# create button 
restart_button = Button(screen_width//2 - 50, screen_height//2 + 100, restart_img)
start_button = Button(screen_width//2 - 350, screen_height//2, start_img)
exit_button = Button(screen_width//2 + 150, screen_height//2, exit_img)

run = True
while run:
    # print("on loop")

    clock.tick(fps)

    screen.blit(bg_img, (0,0))
    screen.blit(sun_img, (100,100))
    
    if main_menu == True:
        if start_button.draw():
            main_menu = False
        if exit_button.draw():
            run = False
    else:
        world.draw()

        # si el player pierde la vida paralizo a los blobs (porque game_over se setea en -1 al momento de perder la vida)
        if game_over == 0: # el player esta en juego
            # .update -> metodo de la clase Group que busca y ejecuta el metodo update() de los sprites que tenga dentro
            blob_group.update()
            platform_group.update()
            lava_group.update()

            # si hay colision entre el player y alguna coin, elimino la coin e incremento score en 1 
            #update score
            #check if a coin has been collected
            if pygame.sprite.spritecollide(player, coin_group, True): # True elimina de la pantalla el sprite colisionado
                score += 1
                coin_fx.play() # v11
            draw_text("X " + str(score), font_score, white, tile_size-10, 10)
        
        # .draw -> metodo de la clase Group para blitear los elementos de un objeto de tipo Group (sprite)
        blob_group.draw(screen)
        
        platform_group.draw(screen) # v12
        
        coin_group.draw(screen) # dibujo todas las coins cargadas en coin_group
        
        lava_group.draw(screen)

        exit_group.draw(screen)
        
        pygame.draw.rect(screen, (255,0,0), (550,500,50,50), 2)

        game_over = player.update(game_over)

        # draw_grid()

        # if player has died
        if game_over == -1:
            if restart_button.draw():
                # player.reset(100, screen_height - 50)
                world_data = []
                world = reset_level(level) # en la variable que guarda el objeto World, cargo una nueva instancia de World cada vez que el player supera un nivel
                game_over = 0 # habilito que se siga moviendo el player y los enemigos
                score = 0 

        # if player has completed the level
        if game_over == 1: # el player llego a la puerta y paso de nivel
            # reset game and go to the next level
            level += 1
            if level <= max_levels:
                # reset level
                world_data = []
                world = reset_level(level) # en la variable que guarda el objeto World, cargo una nueva instancia de World cada vez que el player supera un nivel
                game_over = 0 # habilito que se siga moviendo el player y los enemigos
            else: 
                draw_text("YOU WIN!", font, blue, (screen_width//2) - 140, screen_height//2)
                # restart game 
                if restart_button.draw():
                    level = 0
                    world_data = []
                    world = reset_level(level)
                    game_over = 0 # habilito que se siga moviendo el player y los enemigos
                    score = 0 

    # print(level)
    # print(game_over)
    # print(score)
    # print(lava_group)
    # print(screen.get_rect().center)


    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == \
            pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False

    draw_grid()
    
    pygame.display.update()

pygame.quit()


# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/PYGAME_PRACTICAS/4.juego_tipo_mario/video12/video_12
# python main.py
# python level_editor.py
