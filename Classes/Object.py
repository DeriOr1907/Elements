import pygame
from Constants import screen


class Object:
    def __init__(self, width, height, pos_x, pos_y, color):
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color

    def display_obstacle(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.pos_x,self.pos_y,self.width,self.height))
