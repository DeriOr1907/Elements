import pygame
from Constants import *
from Classes.Character import *


def gem():
    sound = pygame.mixer.Sound("Sounds/Gem Sound.mp3")
    pygame.mixer.Sound.play(sound)


class Diamond:

    def __init__(self, root, color, location):
        self.location = location
        self.color = color
        self.height = 30
        self.width = 30
        self.image = pygame.transform.scale(pygame.image.load(root), (self.width, self.height))

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

    def display_diamond(self):
        screen.blit(self.image, self.location)

    def collect(self, ch):
        loc = (self.location[0]+15, self.location[1]+15)
        if ch.top_right()[1] <= loc[1] <= ch.right_bottom()[1]:
            if ch.top_right()[0] >= loc[0] >= ch.left_bottom()[0]:
                if ch.color == self.color:
                    gem()
                    return False
        return True