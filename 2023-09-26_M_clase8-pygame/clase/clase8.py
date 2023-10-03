import pygame

pygame.init() #Se inicializa pygame

screen = pygame.display.set_mode([500, 500]) #Se crea una ventana

running = True

while running:  
    
    imagen = pygame.image.load("00.png")
    imagen = pygame.image.load("00.png")
   
    # Se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))# Se pinta el fondo de la ventana
    # Se dibuja un círculo azul en el centro

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    pygame.display.flip()# Muestra los cambios en  la pantalla

pygame.quit() # Fin

print(type(imagen))
screen.blit()