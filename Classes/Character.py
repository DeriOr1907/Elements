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

    def display_character(self,objects):
        if not self.jumping:
            self.jumpV = 0
        if self.jumpV >= -7:
            self.jumpV = self.jumpV-0.5
        if self.moving_right:
            self.direction = 1
            if self.able_to_move_right(objects):
                self.Location = (self.Location[0] + 2.5, self.Location[1])
        if self.moving_left:
            self.direction = 2
            if self.able_to_move_left(objects):
                self.Location = (self.Location[0] - 2.5, self.Location[1])
        if self.alive:
            if self.able_to_move_down(objects):
                self.Location = (self.Location[0], self.Location[1] + gravity)
                self.Location = (self.Location[0], self.Location[1] - self.jumpV)

            screen.blit(self.images[self.direction], self.Location)
        self.direction = 0

    def start_jump(self):
        self.Location = (self.Location[0],self.Location[1]-5)
        if not self.jumping:
            self.jumpV = 15
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
        uploc = (self.Location[0]+40, self.Location[1])
        downloc = (self.Location[0]+40, self.Location[1]+45)
        for obj in objects:
            if obj.top_left()[1] <= uploc[1] <= obj.left_bottom()[1]:
                if obj.top_left()[0] >= uploc[0] >= obj.left_bottom()[0]:
                    return False
            if obj.top_left()[1] <= downloc[1] <= obj.left_bottom()[1]:
                if obj.top_left()[0] >= downloc[0] >= obj.left_bottom()[0]:
                    return False
        return True

    def able_to_move_down(self, objects):
        down_loc = (self.Location[0]-2, self.Location[1]+47)
        for obj in objects:
            if obj.top_left()[1] <= down_loc[1] <= obj.left_bottom()[1]:
                if obj.top_left()[0] <= down_loc[0] <= obj.top_right()[0]:
                    self.jumping = False
                    return False
            if obj.top_left()[1] <= down_loc[1] <= obj.left_bottom()[1]:
                if obj.top_left()[0] <= down_loc[0]+30 <= obj.top_right()[0]:
                    self.jumping = False
                    return False
        self.jumpV -= 0.5
        return True

    def able_to_move_left(self, objects):
        return True




