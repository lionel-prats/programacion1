import pygame
import sys

# Initialize Pygame
pygame.init()

# Define colors
red = (255, 0, 0)
white = (255, 255, 255)

# Create the window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Collision of Sprites in the Same Group")

# Define the sprite class
class MySprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height, velocity):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = velocity

    def update(self):
        # Move the sprite
        self.rect.x += self.velocity

        # Check collision with the window boundaries
        if self.rect.left < 0 or self.rect.right > width:
            self.velocity *= -1  # Change direction when colliding with the sides

# Create a sprite group
sprite_group = pygame.sprite.Group()

# Create sprites and add them to the group with the same velocity
sprite1 = MySprite(red, 50, 200, 50, 50, 5)
sprite2 = MySprite(white, 500, 200, 50, 50, 5)
sprite_group.add(sprite1, sprite2)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Check collisions between sprites in the group
    for sprite in sprite_group:
        sprite_group.remove(sprite)  # Remove the sprite temporarily to avoid self-collision
        if pygame.sprite.spritecollide(sprite, sprite_group, False):
            sprite.velocity *= -1  # Change direction upon collision
        sprite_group.add(sprite)  # Add the sprite back to the group

    # Update all sprites in the group
    sprite_group.update()

    # Clear the screen
    window.fill((0, 0, 0))

    # Draw the sprites on the screen
    sprite_group.draw(window)

    # Update the display
    pygame.display.flip()

    # Control the update speed
    pygame.time.Clock().tick(60)
