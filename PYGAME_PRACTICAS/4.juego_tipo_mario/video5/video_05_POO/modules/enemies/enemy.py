import pygame 

class Enemy(pygame.sprite.Sprite):
    # def __init__(self, x, y):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.image.load('img/blob.png')
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        
        self.rect.x += self.move_direction

        # bloque para el movimiento de los enemigos
        # se moveran a derecha e izquierda durante +/-50 pixeles de su ubicacion original
        # self.move_counter ira de -51 a 50, luego de 50 vuelve a -51, en loop infinito
        # durante este tiempo los enemigos se iran moviendo en un sentido
        # cuando self.move_counter se reinicia en -51, los enemigos cambian de direccion
        # sib abs() aparentemente funciona igual
        self.move_counter += 1 
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1