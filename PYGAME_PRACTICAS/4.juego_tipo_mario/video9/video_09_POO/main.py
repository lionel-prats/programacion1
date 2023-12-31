import pygame 
from pygame.locals import * 
from auxiliar import *
from variables import *

from modules.player import Player
from modules.world import World
from modules.button import Button


limpiar_consola()

pygame.init()

configs = open_configs()

clock = pygame.time.Clock()

screen_dimentions = (configs.get("screen").get("screen_width"), configs.get("screen").get("screen_height"))
screen = pygame.display.set_mode(screen_dimentions)
pygame.display.set_caption("VIDEO 9 - POO")

# game variables
game_over = 0
main_menu = True
current_level = 1
max_levels = 3

# load images 
# sun_img = pygame.image.load(configs.get("screen").get("images").get("sky"))
sun_img = pygame.image.load("img/sun.png")
bg_img = pygame.image.load("img/sky.png")

player = Player(configs.get("player1"))

# blob, lava, etc
enemies_group = pygame.sprite.Group()

# exit, coins, etc
utilities_group = pygame.sprite.Group()

world = World(configs.get("screen"), 
              configs.get("enemies"), 
              enemy_sprite_group=enemies_group,
              utilities_configs=configs.get("utilities"),
              utilities_group=utilities_group,
              current_level=current_level)


# create buttons 
restart_button = Button(configs.get("buttons").get("restart"))
start_button = Button(configs.get("buttons").get("start"))
exit_button = Button(configs.get("buttons").get("exit"))

run = True
while run:

    print(current_level)
    
    clock.tick(configs.get("fps"))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == \
            pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False

    screen.blit(bg_img, (0,0))
    screen.blit(sun_img, (100,100))
    # world.draw_backgroung(screen)
    
    

    if main_menu == True:
        if start_button.draw(screen):
            main_menu = False
        if exit_button.draw(screen):
            run = False
    else:
        world.draw(screen)

        if game_over == 0:
            enemies_group.update()
            
        # .draw -> metodo de la clase Group para blitear los elementos de un objeto de tipo Group (sprites)
        enemies_group.draw(screen)
        utilities_group.draw(screen)

        # check for collision between player and enemies
        if pygame.sprite.spritecollide(player, enemies_group, False):
            game_over = -1

        # check for collision between player and exit
        if pygame.sprite.spritecollide(player, utilities_group, False):
            game_over = 1
           

        
        # if player has died
        if game_over == -1:
            if restart_button.draw(screen):
                player.reset(configs.get("player1"))
                game_over = 0

        # if player has completed the level
        if game_over == 1: # el player llego a la puerta y paso de nivel
            # reset game and go to the next level
            current_level += 1
            if current_level <= max_levels:
                # reset level
                enemies_group.empty()
                utilities_group.empty()
                player.reset(configs.get("player1"))
                # world_data = []
                world = world.reset_level(
                    configs.get("screen"), 
                    configs.get("enemies"), 
                    enemy_sprite_group=enemies_group,
                    utilities_configs=configs.get("utilities"),
                    utilities_group=utilities_group,
                    current_level=current_level) # en la variable que guarda el objeto World, cargo una nueva instancia de World cada vez que el player supera un nivel
                game_over = 0 # habilito que se siga moviendo el player y los enemigos
            else: 
                # restart game 
                
                if restart_button.draw(screen):
                    enemies_group.empty()
                    utilities_group.empty()
                    player.reset(configs.get("player1"))

                    current_level = 1
                    # world_data = []
                    world = world.reset_level(
                    configs.get("screen"), 
                    configs.get("enemies"), 
                    enemy_sprite_group=enemies_group,
                    utilities_configs=configs.get("utilities"),
                    utilities_group=utilities_group,
                    current_level=current_level)
                    game_over = 0 # habilito que se siga moviendo el player y los enemigos
                    print(game_over)
                    # enemies_group.empty()
                    # utilities_group.empty()

        
        # print(current_level)

        player.update(screen, configs.get("screen").get("screen_height"), tile_list = world.tile_list, game_over=game_over)


        world.draw_grid(screen)

    pygame.display.update()

pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/PYGAME_PRACTICAS/4.juego_tipo_mario/video9/video_09_POO
# python main.py