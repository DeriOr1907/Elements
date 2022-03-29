import pygame


class Object(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


object = Object(35, 75, 100, 100, (255, 255, 255))
object_group = pygame.sprite.Group()
object_group.add(object)






