import pygame
import random
import math
from auxiliar import Auxiliar
from constant import *

# colorful spaceship background

Auxiliar.limpiar_consola()

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#background 
background = pygame.image.load("images/background.png")

# caption and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("images/ufo.png")
pygame.display.set_icon(icon)

score = 0 


# player
playerImg = pygame.image.load("images/player.png")
# playerImg = pygame.transform.rotate(playerImg, 90)
# playerImg = pygame.transform.scale(playerImg, (63,50.4))
playerX = (SCREEN_WIDTH - playerImg.get_width()) / 2 # 370
playerY = 480
playerX_change = 0

# enemy
enemyImg = pygame.image.load("images/enemy.png")
enemyX = random.randint(0, SCREEN_WIDTH - enemyImg.get_width())
enemyY = random.randint(50, 150)
enemyX_change = 2.5
enemyY_change = 40

# bullet
# ready - you can't see the bullet on the screen
# fire - the bullet is currently moving
bulletImg = pygame.image.load("images/bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bulletY_change = 10
bullet_state = "ready"



def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    # x + 16 - centered on x position's bullet in relation to the ship
    # y + 10 - start position of the bullet on y
    screen.blit(bulletImg, (x + 16, y +10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(bulletX - enemyX, 2) + math.pow(bulletY - enemyY, 2))
    # distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    
    # print(distance)

    # if distance < 200:
    if distance < 27:
        return True
    else:
        return False

# game loop
running = True
while running:

    # RGB = red, green, blue
    screen.fill((0,0,0))
    #background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()

        # if keystroke is pressed check wheter its right or left
        if event.type == pygame.KEYDOWN: 
            print("a keystroke is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change += 5
            if event.key == pygame.K_LEFT:
                playerX_change -= 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(x=bulletX, y=bulletY)
                    # bullet_state = "fire"

        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0

    # checking for boundaries of spaceship so it doesn't go out of bounds
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= SCREEN_WIDTH - playerImg.get_width():
        playerX = SCREEN_WIDTH - playerImg.get_width()
       
    # enemy movement
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 2.5
        enemyY += enemyY_change
    elif enemyX >= SCREEN_WIDTH - enemyImg.get_width():
        enemyX_change = -2.5
        enemyY += enemyY_change

    # bullet movement
    # if bulletY <= 0:
    if bulletY <= 0 - bulletImg.get_height():
        bulletY = 480
        bullet_state = "ready"
        
    if bullet_state is "fire":
        # fire_bullet(x=playerX, y=bulletY)
        fire_bullet(x=bulletX, y=bulletY)
        bulletY -= bulletY_change

    # collision 
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)

    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, SCREEN_WIDTH - enemyImg.get_width())
        enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    
    
    pygame.display.update()



# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/ENTREGAS/space_invaders_you_tube/
# python main_1_enemigo.py
# tutorial - https://www.youtube.com/watch?v=FfWpgLFMI7w