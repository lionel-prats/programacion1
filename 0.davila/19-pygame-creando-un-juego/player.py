# import pygame
from auxiliar import Auxiliar
from constantes import *

Auxiliar.limpiar_consola()

class Player:
    def __init__(self, x, y, speed_walk, speed_run, gravity, jump) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "caracters/stink/walk.png", 15, 1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "caracters/stink/walk.png", 15, 1, flip=True)[:12]
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "caracters/stink/idle.png", 16, 1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "caracters/stink/idle.png", 16, 1, flip=True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "caracters/stink/jump.png", 33, 1)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "caracters/stink/jump.png", 33, 1, flip=True)
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = x
        self.move_y = y
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = gravity
        self.jump = jump

        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()

        self.is_jump = False

    def control(self, accion, x=0, y=0):
        self.move_y = y
        if accion == "walk_r":
            self.animation = self.walk_r
            self.move_x = self.speed_walk
        elif accion == "walk_l":
            # self.move_y = -self.jump
            # self.animation = self.jump
            self.animation = self.walk_l
            self.move_x = -self.speed_walk
        elif accion == "jump_r":
            self.move_y = -self.jump
            self.move_x = self.speed_run
            self.animation = self.jump_r
            self.is_jump = True
        elif accion == "jump_l":
            self.move_y = -self.jump
            self.move_x = self.speed_run
            self.animation = self.jump_l
            self.is_jump = True
        elif accion == "stay_r":
            self.animation = self.stay_r
            self.move_x = 0
            self.is_jump = False
        elif accion == "stay_l":
            self.animation = self.stay_l
            self.move_x = 0
            self.is_jump = False
        self.frame = 0

        print(self.rect)

    def update(self):
        # self.frame += 1
        # if self.frame == (len(self.animation)):
        #     self.frame = 0

        if self.frame < (len(self.animation) - 1):
            self.frame += 1
        else:
            self.frame = 0
            if self.is_jump == True:
                self.is_jump = False
                self.move_y = 0

        self.rect.x += self.move_x
        self.rect.y += self.move_y
 
        # if self.rect.y < self.gravity:  
        #     self.rect.y += self.gravity
        
        if self.rect.y < 500:  
            self.rect.y += self.gravity


    def draw(self, screen):
        # print(self.rect)
        self.image = self.animation[self.frame]
        # self.rect = self.image.get_rect()
        screen.blit(self.image, self.rect)