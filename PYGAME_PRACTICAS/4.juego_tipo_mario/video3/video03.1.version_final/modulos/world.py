import pygame 

class World():
    def __init__(self, data, tile_size):
        
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
                     
                col_count += 1
            row_count += 1

    def draw_grid(screen, screen_width, screen_height, tile_size):
        for line in range(0, int(screen_width/tile_size)):
            pygame.draw.line(surface=screen, color=(255, 255, 255), start_pos=(0, line * tile_size), end_pos=(screen_width, line * tile_size), width=1)
            pygame.draw.line(surface=screen, color=(255, 255, 255), start_pos=(line * tile_size, 0), end_pos=(line * tile_size, screen_height), width=1)
          
    def draw(self, screen):
        for tile in self.tile_list:
             screen.blit(tile[0], tile[1])