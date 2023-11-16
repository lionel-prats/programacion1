import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

run = True

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
            
pygame.quit()