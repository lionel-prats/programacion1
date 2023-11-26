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

screen_dimentions = (configs.get("screen").get("screen_width"), 
                     configs.get("screen").get("screen_height"))

screen = pygame.display.set_mode(screen_dimentions)
pygame.display.set_caption("POO - Version Final")

# define game variables
game_over = 0
main_menu = True
current_level = 1
max_levels = 2
score = 0 

background_image_path, background_image_coord_x, background_image_coord_y = \
    data_image_parsed(configs.get("screen").get("images").get("background_image"))
background_surface = pygame.image.load(background_image_path)

sun_img_path, sun_img_coord_x, sun_img_coord_y = \
    data_image_parsed(configs.get("screen").get("images").get("sun"))
sun_surface = pygame.image.load(sun_img_path)

player = Player(configs.get("player1"))

enemies_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

world = World(configs.get("screen"), configs.get("enemies"), enemy_sprite_group=enemies_group,
              exit_configs=configs.get("exit"), exit_group=exit_group, coin_group=coin_group,
              platform_group=platform_group, current_level=current_level)

# create buttons 
restart_button = Button(configs.get("buttons").get("restart"))
start_button = Button(configs.get("buttons").get("start"))
exit_button = Button(configs.get("buttons").get("exit"))

coin_fx, jump_fx, game_over_fx = World.inicializar_sonidos()

run = True

while run:
    
    clock.tick(configs.get("fps"))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == \
            pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False

    screen.blit(background_surface, (background_image_coord_x, background_image_coord_y))
    screen.blit(sun_surface, (sun_img_coord_x, sun_img_coord_y))
    
    if main_menu == True:
        if start_button.draw(screen):
            main_menu = False
        if exit_button.draw(screen):
            run = False
    else:

        world.draw(screen)

        # group.draw() -> metodo de la clase Group para blitear los elementos de un objeto de tipo Group (sprites)
        platform_group.draw(screen)
        enemies_group.draw(screen)
        coin_group.draw(screen)
        exit_group.draw(screen)

        if game_over == 0: # playing

            platform_group.update()
            enemies_group.update()

            # check for collision between player and enemies (blobs, lava)
            if pygame.sprite.spritecollide(player, enemies_group, False):
                game_over = -1
                game_over_fx.play()

            # check if a coin has been collected
            # True elimina de la pantalla el sprite colisionado
            if pygame.sprite.spritecollide(player, coin_group, True): 
                score += 1
                coin_fx.play()

            # check for collision between player and exit
            if pygame.sprite.spritecollide(player, exit_group, False):
                game_over = 1
        
        # update score
        world.draw_text(screen, ("score", score, coin_group))

        if game_over == -1: # player has died

            world.draw_text(screen, ("game_over",))
            
            if restart_button.draw(screen): # restart button is pressed
                
                player.reset(configs.get("player1"))
                game_over = 0
                score = 0 
                
                enemies_group.empty()
                exit_group.empty()
                platform_group.empty()

                world = world.reset_level(
                    configs.get("screen"), 
                    configs.get("enemies"), 
                    enemy_sprite_group=enemies_group,
                    exit_configs=configs.get("exit"),
                    exit_group=exit_group,
                    coin_group=coin_group,
                    platform_group=platform_group,
                    current_level=current_level
                )

        # if player has completed the level (el player llego a la puerta y paso de nivel)
        if game_over == 1: 
            # reset game and go to the next level
            current_level += 1
            if current_level <= max_levels:
                
                # next level
                enemies_group.empty()
                exit_group.empty()
                platform_group.empty()

                player.reset(configs.get("player1"))

                # en la variable que guarda el objeto World, cargo una nueva instancia de World cada vez que el player supera un nivel
                world = world.reset_level(
                    configs.get("screen"), 
                    configs.get("enemies"), 
                    enemy_sprite_group=enemies_group,
                    exit_configs=configs.get("exit"),
                    exit_group=exit_group,
                    coin_group=coin_group,                    
                    platform_group=platform_group,
                    current_level=current_level
                ) 

                game_over = 0 # habilito que se siga moviendo el player y los enemigos
            
            else: 
                world.draw_text(screen, ("you_win",))

                # restart game (level 1)
                if restart_button.draw(screen):

                    enemies_group.empty()
                    exit_group.empty()
                    platform_group.empty()

                    player.reset(configs.get("player1"))

                    current_level = 1
                    
                    world = world.reset_level(
                        configs.get("screen"), 
                        configs.get("enemies"), 
                        enemy_sprite_group=enemies_group,
                        exit_configs=configs.get("exit"),
                        exit_group=exit_group,
                        coin_group=coin_group,
                        platform_group=platform_group,
                        current_level=current_level
                    )
                    game_over = 0 # habilito que se siga moviendo el player y los enemigos
                    score = 0 

        player.update(
                screen, 
                configs.get("screen").get("screen_height"), 
                tile_list = world.tile_list, 
                game_over=game_over,
                jump_fx=jump_fx,
                platform_group=platform_group
            )

        world.draw_grid(screen)

    pygame.display.update()
    
pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/PYGAME_PRACTICAS/4.juego_tipo_mario/z_POO_version_final
# python main.py