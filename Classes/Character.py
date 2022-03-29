from Constants import screen, gravity
from Classes.Object import *
class Character:
    def __init__(self,Location, Color, Img):
        self.Location = Location
        self.color = Color
        self.direction = 0 # 0 is forward, 1 is right and 2 is left
        self.images = Img
        self.alive = True
        self.moving_right = False
        self.moving_left = False
        self.jumping = False
        self.jumpV = 0

    def display_character(self):
        if not self.jumping:
            self.jumpV = 0
        if self.jumping:
            if self.jumpV >= -10:
                self.jumpV = self.jumpV-0.5
        if self.moving_right:
            self.direction = 1
            if self.able_to_move_right():
                self.Location = (self.Location[0] + 2, self.Location[1])
        if self.moving_left:
            self.direction = 2
            if self.able_to_move_left():
                self.Location = (self.Location[0] - 2, self.Location[1])
        if self.alive:
            self.Location = (self.Location[0], self.Location[1] + gravity - self.jumpV)
            screen.blit(self.images[self.direction], self.Location)
        self.direction = 0

    def start_jump(self):
        if not self.jumping:
            self.jumpV = 14
            self.jumping = True


    def move_right(self):
        self.moving_right = True

    def stop_moving_right(self):
        self.moving_right = False

    def stop_moving_left(self):
        self.moving_left = False

    def move_left(self):
        self.moving_left = True

    def able_to_move_right(self, objects):
        uploc = (self.Location[0]+40,self.Location[1])
        for obj in objects:
            if True:
                pass
        return True

    def able_to_move_left(self, objects):
        return True




