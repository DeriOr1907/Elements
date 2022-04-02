import pygame
from Constants import screen

class Lava:
    def __init__(self,root, color, location):
        self.root = root
        self.location = location
        self.color = color
        self.height = 20
        self.width = 100


    def display_lava(self):
        image = pygame.transform.scale(pygame.image.load(self.root), (self.width, self.height))
        screen.blit(image,self.location)