import pygame 

class Font():
    def __init__(self, font, size):
        self.surface_text = pygame.font.SysFont(font, size)

    # def draw_text(self, screen, text, font, text_col, x, y):
    #     # img = font.render(text, antialias=True, text_col)
    #     img = font.render(text, True, text_col) # surface de tipo Font <Surface(41x34x32 SW)>
    #     # print(img.get_rect().height)
    #     # print(img.get_rect())
    #     screen.blit(img, (x,y))