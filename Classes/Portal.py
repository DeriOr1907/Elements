import pygame
from Constants import screen


class Portal:
    def __init__(self, root1,root2,root3,root4,root5, location):
        self.location = location
        self.height = 70
        self.width = 40
        self.image1 = pygame.transform.scale(pygame.image.load(root1), (self.width, self.height))
        self.image2 = pygame.transform.scale(pygame.image.load(root2), (self.width, self.height))
        self.image3 = pygame.transform.scale(pygame.image.load(root3), (self.width, self.height))
        self.image4 = pygame.transform.scale(pygame.image.load(root4), (self.width, self.height))
        self.image5 = pygame.transform.scale(pygame.image.load(root5), (self.width, self.height))
        self.images = [self.image1,self.image2,self.image3,self.image4,self.image5]
        self.index = 0
        self.delay = 0

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

    def display_portal(self,ch1,ch2):
        if self.index > 4:
            self.index = 0
        screen.blit(self.images[self.index], self.location)
        if self.delay == 15:
            self.index += 1
        self.delay += 1
        if self.delay > 15:
            self.delay = 0
