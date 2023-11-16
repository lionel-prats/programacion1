import pygame 
import random

class Enemy():
    def __init__(self, coordinates: tuple, color: tuple):
        self.current_coordinates = []
        for coord in coordinates:
            self.current_coordinates.append(coord)
        self.color = color
        self.to_right = True
        if self.current_coordinates[0] > 400:
            self.to_right = False
         
    def __control(self, movement, screen_rect):
        match movement:
            case "from_right_to_left":
                self.__from_right_to_left(screen_rect.width)
            case "to_left":
                self.__to_left(screen_rect.width)
            case "diagonal":
                self.__diagonal(screen_rect)
    
    def __from_right_to_left(self, screen_width):
        # print(screen_width)
        if self.to_right:
            self.current_coordinates[0] += 1
            if self.current_coordinates[0] == screen_width - self.current_coordinates[2]:
                self.to_right = False
        else:
            self.current_coordinates[0] -= 1
            if self.current_coordinates[0] == 0:
                self.to_right = True
    
    def __to_left(self, screen_width):
        self.current_coordinates[0] -= 1
        if self.current_coordinates[0] < 0:
            self.current_coordinates[0] = screen_width - self.current_coordinates[2]
    
    def __diagonal(self, screen_rect):
        self.current_coordinates[0] += 1
        self.current_coordinates[1] += 1
        if self.current_coordinates[0] >= screen_rect.width or self.current_coordinates[1] >= screen_rect.height:
            random_x = random.randint(0, screen_rect.width - self.current_coordinates[2])
            if random_x == 0:
                random_y = random.randint(0, screen_rect.height - self.current_coordinates[3])
            else:
                random_y = 0
            self.current_coordinates[0] = random_x
            self.current_coordinates[1] = random_y
        
    def update(self, screen, movement):
        self.__control(movement, screen.get_rect())
        pygame.draw.rect(screen, self.color, self.current_coordinates)
