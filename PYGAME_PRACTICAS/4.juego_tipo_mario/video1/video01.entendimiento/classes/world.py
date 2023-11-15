import pygame 

class World():
    def __init__(self, data, tile_size):
        
        self.tile_list = []
        """  
        [
            (<Surface(200x200x32 SW)>, <rect(0, 0, 200, 200)>),       -> dirt
            (<Surface(200x200x32 SW)>, <rect(200, 0, 200, 200)>),     -> dirt
            (<Surface(200x200x32 SW)>, <rect(400, 0, 200, 200)>),     -> dirt
            (<Surface(200x200x32 SW)>, <rect(600, 0, 200, 200)>),     -> dirt
            (<Surface(200x200x32 SW)>, <rect(800, 0, 200, 200)>),     -> dirt
            (<Surface(200x200x32 SW)>, <rect(0, 200, 200, 200)>),     -> dirt
            (<Surface(200x200x32 SW)>, <rect(800, 200, 200, 200)>),   -> dirt
            (<Surface(200x200x32 SW)>, <rect(0, 400, 200, 200)>),     -> dirt
            (<Surface(200x200x32 SW)>, <rect(800, 400, 200, 200)>),   -> dirt
            (<Surface(200x200x32 SW)>, <rect(0, 600, 200, 200)>),     -> dirt
            (<Surface(200x200x32 SW)>, <rect(800, 600, 200, 200)>),   -> dirt
            (<Surface(200x200x32 SW)>, <rect(0, 800, 200, 200)>),     -> dirt
            (<Surface(200x200x32 SW)>, <rect(200, 800, 200, 200)>),   -> grass
            (<Surface(200x200x32 SW)>, <rect(400, 800, 200, 200)>),   -> grass
            (<Surface(200x200x32 SW)>, <rect(600, 800, 200, 200)>),   -> grass
            (<Surface(200x200x32 SW)>, <rect(800, 800, 200, 200)>),   -> dirt
        ]
        """

        #load images 
        dirt_img = pygame.image.load("img/dirt.png") 
        grass_img = pygame.image.load("img/grass.png") 
        
        row_count = 0
        for row in data: 
            col_count = 0
            for tile in row: 
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect() # <rect(0, 0, 200, 200)>
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

    def draw(self, screen):
        for tile in self.tile_list:
             screen.blit(tile[0], tile[1])