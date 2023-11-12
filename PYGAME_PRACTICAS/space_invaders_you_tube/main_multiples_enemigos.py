import pygame
from pygame import mixer
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

# background sound
mixer.music.load("sounds/background.wav")
mixer.music.play(-1)

# caption and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("images/ufo.png")
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("images/player.png")
# playerImg = pygame.transform.rotate(playerImg, 90)
# playerImg = pygame.transform.scale(playerImg, (63,50.4))
playerX = (SCREEN_WIDTH - playerImg.get_width()) / 2 # 370
playerY = 480
playerX_change = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("images/enemy.png"))
    enemyX.append(random.randint(0, SCREEN_WIDTH - enemyImg[i].get_width()))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2.5)
    enemyY_change.append(40)

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

# Score
score_value = 0 
font = pygame.font.Font("freesansbold.ttf", size=32)
textX = 10
textY = 10

# game over text
over_font = pygame.font.Font("freesansbold.ttf", size=64)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200, 250))

def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y, i):
    screen.blit(enemyImg[i], (x, y))

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
            if event.key == pygame.K_RIGHT:
                playerX_change += 5
            if event.key == pygame.K_LEFT:
                playerX_change -= 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound("sounds/laser.wav")
                    bullet_sound.play()
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
    for i in range(num_of_enemies):
       
        # game over 
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= SCREEN_WIDTH - enemyImg[i].get_width():
            enemyX_change[i] = -2.5
            enemyY[i] += enemyY_change[i]

        # collision 
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            esplosion_sound = mixer.Sound("sounds/explosion.wav")
            esplosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - enemyImg[i].get_width())
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    # if bulletY <= 0:
    if bulletY <= 0 - bulletImg.get_height():
        bulletY = 480
        bullet_state = "ready"
        
    if bullet_state is "fire":
        fire_bullet(x=bulletX, y=bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)

    show_score(textX, textY)
    
    
    pygame.display.update()



# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/ENTREGAS/space_invaders_you_tube/
# python main_multiples_enemigos.py
# tutorial - https://www.youtube.com/watch?v=FfWpgLFMI7w