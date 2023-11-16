import pygame 

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
        self.vel_y = 0
        self.jumped = False
        self.direction = 0

    def update(self, screen, screen_height):
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

        dy += self.vel_y

        # update player coordinates
        self.rect.x += dx 
        self.rect.y += dy 

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            dy = 0

        screen.blit(self.image, self.rect) # draw player onto screen