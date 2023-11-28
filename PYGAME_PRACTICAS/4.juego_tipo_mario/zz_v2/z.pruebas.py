import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
blanco = (255, 255, 255)
negro = (0, 0, 0)

# Crear la ventana
ancho, alto = 800, 400
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Elemento en Plataforma")

# Definir la clase del sprite
class MiSprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y, ancho, alto, velocidad):
        super().__init__()
        self.image = pygame.Surface((ancho, alto))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad = velocidad

    def update(self):
        # Mover el sprite solo a lo largo de la plataforma
        self.rect.x += self.velocidad

        # Cambiar dirección al llegar a los bordes de la plataforma
        if self.rect.left < 250 or self.rect.right > 750:  # Limitar a los bordes de la plataforma
            self.velocidad *= -1

# Crear grupo de sprites
grupo_sprites = pygame.sprite.Group()

# Dibujar la plataforma
plataforma = pygame.Surface((500, 50))
plataforma.fill(blanco)
rect_plataforma = plataforma.get_rect(center=(ancho // 2, alto - 25))

# Crear sprite y agregarlo al grupo
elemento = MiSprite(blanco, 250, alto - 75, 50, 50, 3)  # Iniciar en la posición inicial dentro de la plataforma
grupo_sprites.add(elemento)

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar todos los sprites en el grupo
    grupo_sprites.update()

    # Limpiar la pantalla
    ventana.fill(negro)

    # Dibujar la plataforma en la pantalla
    ventana.blit(plataforma, rect_plataforma)

    # Dibujar los sprites en la pantalla
    grupo_sprites.draw(ventana)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    pygame.time.Clock().tick(60)
