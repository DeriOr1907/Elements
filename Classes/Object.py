import pygame
from Constants import screen


class Object:
    def __init__(self, width, height, pos_x, pos_y, color):
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color

    def top_left(self):
        x = (self.pos_x, self.pos_y)
        return x

    def top_right(self):
        x = (self.pos_x + self.width, self.pos_y)
        return x

    def right_bottom(self):
        x = (self.pos_x + self.width, self.pos_y + self.height)
        return x

    def left_bottom(self):
        x = (self.pos_x, self.pos_y + self.height)
        return x

    def display_obstacle(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.pos_x, self.pos_y, self.width, self.height))
