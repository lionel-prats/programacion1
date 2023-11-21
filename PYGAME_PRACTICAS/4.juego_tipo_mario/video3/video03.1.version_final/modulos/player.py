import pygame 

class Player():
    def __init__(self, player_configs: dict):
        self.player_configs = player_configs
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0 # frames counter
        for num in range(1,5):
            img_right = pygame.image.load(f"img/guy{num}.png")
            img_right = pygame.transform.scale(img_right, (self.player_configs.get("rect_width"), self.player_configs.get("rect_height")))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]     
        self.rect = self.image.get_rect()
        self.rect.x = player_configs.get("coord_x") # 100
        self.rect.y = player_configs.get("coord_y") # 870
        self.vel_y = 0
        self.jumped = False
        self.direction = 0

        print((self.image)) 

    def update(self, screen, screen_height):
        
        dx = 0
        dy = 0

        walk_cooldown = self.player_configs.get("animation").get("walk_cooldown") # 5
        
        key = pygame.key.get_pressed() # get kypresses

        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = self.player_configs.get("animation").get("vel_y") # -15
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= self.player_configs.get("animation").get("dx") # 5
            self.counter += 1
            self.direction = -1
        if key[pygame.K_RIGHT]:
            dx += self.player_configs.get("animation").get("dx") # 5
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
        self.vel_y += 1 # -14|-13|-12...9|10|10|10
        if self.vel_y > 10:
            self.vel_y = 10

        dy += self.vel_y
        
        # update rect player coordinates
        self.rect.x += dx # +/-5 or 0
        self.rect.y += dy 
        
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            # dy = 0    

        # print(self.vel_y, self.rect.y)
        # self.rect.y when start the game vvv
        # self.vel_y=1 self.rect.y=871
        # self.vel_y=2 self.rect.y=873
        # self.vel_y=3 self.rect.y=876
        # self.vel_y=4 self.rect.y=880
        # self.vel_y=5 self.rect.y=885
        # self.vel_y=6 self.rect.y=891
        # self.vel_y=7 self.rect.y=898
        # self.vel_y=8 self.rect.y=906
        # self.vel_y=9 self.rect.y=915
        # self.vel_y=10 self.rect.y=920...
        
        # self.rect.y when player jump vvv
        # self.vel_y=-14 self.rect.y=906 UP
        # self.vel_y=-13 self.rect.y=893 UP
        # self.vel_y=-12 self.rect.y=881 UP
        # self.vel_y=-11 self.rect.y=870 UP
        # self.vel_y=-10 self.rect.y=860 UP
        # self.vel_y=-9 self.rect.y=851 UP
        # self.vel_y=-8 self.rect.y=843 UP
        # self.vel_y=-7 self.rect.y=836 UP
        # self.vel_y=-6 self.rect.y=830 UP
        # self.vel_y=-5 self.rect.y=825 UP
        # self.vel_y=-4 self.rect.y=821 UP
        # self.vel_y=-3 self.rect.y=818 UP
        # self.vel_y=-2 self.rect.y=816 UP
        # self.vel_y=-1 self.rect.y=815 UP
        # self.vel_y=0 self.rect.y=815 -
        # self.vel_y=1 self.rect.y=816 DOWN
        # self.vel_y=2 self.rect.y=818 DOWN
        # self.vel_y=3 self.rect.y=821 DOWN
        # self.vel_y=4 self.rect.y=825 DOWN
        # self.vel_y=5 self.rect.y=830 DOWN
        # self.vel_y=6 self.rect.y=836 DOWN
        # self.vel_y=7 self.rect.y=843 DOWN
        # self.vel_y=8 self.rect.y=851 DOWN
        # self.vel_y=9 self.rect.y=860 DOWN
        # self.vel_y=10 self.rect.y=870 DOWN
        # self.vel_y=10 self.rect.y=880 DOWN
        # self.vel_y=10 self.rect.y=890 DOWN
        # self.vel_y=10 self.rect.y=900 DOWN
        # self.vel_y=10 self.rect.y=910 DOWN
        # self.vel_y=10 self.rect.y=920...

        screen.blit(self.image, self.rect) # draw player onto screen