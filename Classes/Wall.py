import pygame
from Constants import screen

class Wall:
    def __init__(self, root, color,height, width, location):
        self.location = location
        self.color = color
        self.height = height
        self.width = width
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

    def display_wall(self):
        screen.blit(self.image, self.location)

    def able_to_display(self,boy,girl):
        characters = [boy, girl]
        for ch in characters:
            if ch.top_left()[0] <= self.location[0] + self.width <= ch.top_right()[0]:
                if self.location[1] <= ch.top_left()[1] + 15 <= self.location[1] + self.height:
                    return False
            if ch.top_left()[0] <= self.location[0] <= ch.top_right()[0]:
                if self.location[1] <= ch.top_left()[1] + 15 <= self.location[1] + self.height:
                    return False
        return True
