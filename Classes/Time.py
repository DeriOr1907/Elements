import pygame
from Constants import *

class Time:

    def __init__(self, time, location, color, root):
        self.time = time
        self.location = location
        self.color = color
        self.height = 100
        self.width = 300
        self.image = pygame.transform.scale(pygame.image.load(root), (self.width, self.height))

    def display_time(self):
        screen.blit(self.image, self.location)