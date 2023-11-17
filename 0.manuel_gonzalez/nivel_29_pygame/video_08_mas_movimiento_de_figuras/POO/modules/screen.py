import pygame 

class Screen:
    def __init__(self, width, height, bg_color) -> None:
        self.width = width
        self.height = height
        self.bg_color = bg_color

        pygame.init()
        pygame.display.set_mode((self.width, self.height))