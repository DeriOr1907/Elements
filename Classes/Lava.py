import pygame
from Constants import screen

class Lava:
    def __init__(self,root, color, location):
        self.root = root
        self.location = location
        self.color = color
        self.height = 20
        self.width = 100

    def top_left(self):
        return self.location

    def top_right(self):
        x = (self.location[0] + self.width, self.location[1])
        return x

    def right_bottom(self):
        x = (self.location[0] + self.width, self.location[1] + self.height)
        return x

    def left_bottom(self):
        x = (self.location[0], self.location[1] + self.height)
        return x

    def display_lava(self):
        image = pygame.transform.scale(pygame.image.load(self.root), (self.width, self.height))
        screen.blit(image,self.location)