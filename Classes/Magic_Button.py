import pygame
from Constants import screen
from Classes.Character import *


class Magic_Button:
    def __init__(self, root, color, location):
        self.location = location
        self.color = color
        self.height = 20
        self.width = 20
        self.image = pygame.transform.scale(pygame.image.load(root), (self.width, self.height))
        self.pressed = False

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

    def display_magic_button(self):
        screen.blit(self.image, self.location)

    def press(self,ch):
        loc = (self.location[0] + 10, self.location[1] + 10)
        if ch.top_right()[1] <= loc[1] <= ch.right_bottom()[1]:
            if ch.top_right()[0] >= loc[0] >= ch.left_bottom()[0]:
                self.pressed = True
                return True
        return False