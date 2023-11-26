import pygame 
# from modules.enemies.enemy import Enemy
from modules.enemies.blob import Blob
from modules.enemies.lava import Lava
from modules.exit import Exit
from modules.coin import Coin
from modules.font import Font
from modules.platform import Platform

class World():

    # def __init__(self, data, tile_size):
    def __init__(
            self, 
            screen_configs, 
            enemy_configs, 
            enemy_sprite_group, 
            exit_configs, 
            exit_group, 
            coin_group, 
            platform_group, 
            current_level):
        
        self.screen_configs = screen_configs
        self.tile_list = []

        #load images 
        dirt_img = pygame.image.load(self.screen_configs.get("images").get("dirt")) 
        grass_img = pygame.image.load(self.screen_configs.get("images").get("grass")) 
        
        # agrego al coin_group una coin para que se blitee en el score, arriba a la izquierda en la pantalla
        score_coin = Coin(25, 28, 45)
        coin_group.add(score_coin) 
        
        row_count = 0
        # for row in self.screen_configs.get("world_data"): 
        for row in self.screen_configs.get("levels").get(str(current_level)): 
            col_count = 0
            for tile in row: 
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (self.screen_configs.get("tile_size"), self.screen_configs.get("tile_size")))
                    img_rect = img.get_rect() 
                    img_rect.x = col_count * img_rect.width
                    img_rect.y = row_count * img_rect.height
                    tile = (img, img_rect) 
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (self.screen_configs.get("tile_size"), self.screen_configs.get("tile_size")))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * img_rect.width
                    img_rect.y = row_count * img_rect.height
                    tile = (img, img_rect) 
                    self.tile_list.append(tile)
                
                
                if tile == "blob":
                    enemy_path_image = enemy_configs.get("blob").get("path_image")
                    enemy_height_image = enemy_configs.get("blob").get("height_image")
                    compensation_y = self.screen_configs.get("tile_size") - enemy_height_image
                    # enemy = Enemy(enemy_path_image, 
                    #              col_count * self.screen_configs.get("tile_size"), 
                    #              row_count * self.screen_configs.get("tile_size") + compensation_y)
                    
                    enemy = Blob(enemy_path_image, 
                                 col_count * self.screen_configs.get("tile_size"), 
                                 row_count * self.screen_configs.get("tile_size") + compensation_y)

                    enemy_sprite_group.add(enemy)

                if tile == 4: # plataformas con movimiento en eje X v12

                    coord_x = col_count * self.screen_configs.get("tile_size")
                    coord_y = row_count * self.screen_configs.get("tile_size")
                    tile_size = self.screen_configs.get("tile_size")

                    platform = Platform(coord_x, coord_y, tile_size, 1, 0)
                    platform_group.add(platform)

                if tile == 5: # plataformas con movimiento en eje Y v12

                    coord_x = col_count * self.screen_configs.get("tile_size")
                    coord_y = row_count * self.screen_configs.get("tile_size")
                    tile_size = self.screen_configs.get("tile_size")

                    platform = Platform(coord_x, coord_y, tile_size, 0, 1)
                    platform_group.add(platform)


                if tile == "lava":

                    enemy_path_image = enemy_configs.get("lava").get("path_image")
                    enemy_height_image = enemy_configs.get("lava").get("height_image")
                    coord_x = col_count * self.screen_configs.get("tile_size")
                    coord_y = row_count * self.screen_configs.get("tile_size") + (self.screen_configs.get("tile_size") // 2)
                    lava = Lava(enemy_path_image, 
                                coord_x, 
                                coord_y,
                                self.screen_configs.get("tile_size")
                                )
                    enemy_sprite_group.add(lava)
                
                if tile == 7:
                    coord_x = col_count * self.screen_configs.get("tile_size") + (self.screen_configs.get("tile_size")//2)
                    coord_y = row_count * self.screen_configs.get("tile_size") +  (self.screen_configs.get("tile_size")//2)
                    coin = Coin(coord_x, coord_y, self.screen_configs.get("tile_size"))
                    coin_group.add(coin)


                if tile == 8:
                    exit_path_image = exit_configs.get("path_image")
                    coord_x = col_count * self.screen_configs.get("tile_size")
                    coord_y = row_count * self.screen_configs.get("tile_size") - (self.screen_configs.get("tile_size") // 2)
                    exit = Exit(exit_path_image, coord_x, coord_y, self.screen_configs.get("tile_size"))
                    exit_group.add(exit)
                    # exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size // 2))
                    # exit_group.add(exit)
                    
                col_count += 1
            row_count += 1

    def draw_backgroung(self, screen):
        screen.blit(pygame.image.load(self.screen_configs.get("images").get("sky")) , (0,0))
        screen.blit(pygame.image.load(self.screen_configs.get("images").get("sun")) , (100,100))
        
    def draw_grid(self, screen):
        for line in range(0, int(self.screen_configs.get("screen_width")/self.screen_configs.get("tile_size"))):
            pygame.draw.line(surface=screen, color=(255, 255, 255), start_pos=(0, line * self.screen_configs.get("tile_size")), end_pos=(self.screen_configs.get("screen_width"), line * self.screen_configs.get("tile_size")), width=1)
            pygame.draw.line(surface=screen, color=(255, 255, 255), start_pos=(line * self.screen_configs.get("tile_size"), 0), end_pos=(line * self.screen_configs.get("tile_size"), self.screen_configs.get("screen_height")), width=1)
          
    def draw(self, screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

    # function to reset level
    # @staticmethod
    def reset_level(
            self, 
            screen_configs, 
            enemy_configs, 
            enemy_sprite_group, 
            exit_configs, 
            exit_group, 
            coin_group, 
            platform_group, 
            current_level):
        
        world = World(
                    screen_configs, 
                    enemy_configs, 
                    enemy_sprite_group, 
                    exit_configs, 
                    exit_group, 
                    coin_group, 
                    platform_group, 
                    current_level) # nueva instancia de World con el mapa del nivel que corresponda
        
        return world
    


        # player.reset(100, screen_height - 50) # reseteo los atributos del platyer para que se blitee en la posicion inicial luego de pasar de nivel y ya en el nuevo escenario
        # # player.reset(850, 50)
        # blob_group.empty() # empty() -> metodo de la clase Group() que elimina todos los sprites de un objeto Group
        # lava_group.empty()
        # exit_group.empty()
        # if path.exists(f"level{level}_data"): # load in level data and create world
        #     pickle_in = open(f"level{level}_data", "rb") # read binary
        #     world_data = pickle.load(pickle_in)
        #     pickle_in.close()
        # world = World(world_data) # nueva instancia de World con el mapa del nivel que corresponda
        # return world

    
    def draw_text(self, screen, text_info: tuple):

        tipo_texto_a_imprimir = text_info[0] # score|game_over|you_win

        informacion_texto = self.screen_configs.get("texts").get(text_info[0])


        if tipo_texto_a_imprimir == "score":
            score = text_info[1] 
            texto_a_imprimir = informacion_texto.get('text').format(str(score))
        else:
            texto_a_imprimir = informacion_texto.get('text')


        tipo_fuente = informacion_texto.get('font')
        tamanio_fuente = informacion_texto.get('size')
        color = eval(informacion_texto.get('color'))
        x = informacion_texto.get('coord_x')
        y = informacion_texto.get('coord_y')

        # print(informacion_texto)
        


        instancia_Font = Font(tipo_fuente, tamanio_fuente)
        superficie = instancia_Font.surface_text
        # print(font_score_surface)



        # antialias = True
        img = superficie.render(texto_a_imprimir, True, color) 
        
        screen.blit(img, (x,y))

    @staticmethod
    def inicializar_sonidos():
        pygame.mixer.music.load("img/music.wav")
        pygame.mixer.music.play(-1, 0.0, 5000) 
        # param 5000 -> volumen musica de fondo in crescendo durante 5 segs hasta llegar al 100% del volumen seteado
        pygame.mixer.music.set_volume(0.025)
    
        coin_fx = pygame.mixer.Sound("img/coin.wav")
        coin_fx.set_volume(0.05)
        jump_fx = pygame.mixer.Sound("img/jump.wav")
        jump_fx.set_volume(0.05)
        game_over_fx = pygame.mixer.Sound("img/game_over.wav")
        game_over_fx.set_volume(0.05)
        return (coin_fx, jump_fx, game_over_fx)