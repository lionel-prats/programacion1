import pygame 

pygame.init()

screen = pygame.display.set_mode((800,600))

screen.fill((255,0,0))

pygame.display.update() # llamamos a la funcion update(), del modulo display, de la libreria pygame

pygame.time.delay(2000)

pygame.quit()