import pygame
from Constants import screen

class Star:
    def __init__(self, root, size,location, gr):
        self.location = location
        self.size = 0
        self.maxsize = size
        self.root = root
        self.grow = gr
        self.image = pygame.transform.scale(pygame.image.load(self.root), (self.size, self.size))

    def display_star(self):
        if self.size < self.maxsize:
            self.image = pygame.transform.scale(pygame.image.load(self.root), (self.size, self.size))
            screen.blit(self.image, self.location)
            self.size += self.grow
        else:
            screen.blit(self.image, self.location)
