import pygame
from Constants import screen

class Lava:
    def __init__(self,root, color, location):
        self.root = root
        self.location = location
        self.color = color
        self.height = 20
        self.width = 50