import os
import pygame 

def draw_grid(screen, screen_width, screen_height, tile_size):
	for line in range(0, 6):
		pygame.draw.line(surface=screen, color=(255, 255, 255), start_pos=(0, line * tile_size), end_pos=(screen_width, line * tile_size), width=1)
		pygame.draw.line(surface=screen, color=(255, 255, 255), start_pos=(line * tile_size, 0), end_pos=(line * tile_size, screen_height), width=1)

def limpiar_consola():
    """  
    limpia la consola
    """
    # os.system('cls' if os.name == 'nt' else 'clear')
    if os.name in ["ce", "nt", "dos"]: # windows
      os.system("cls")
    else: # linux o mac
      os.system("clear")