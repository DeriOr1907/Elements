from Constants import screen
from Classes.Object import *
gravity = 2.5


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
        self.gravity = 1

    def display_character(self, objects):
        if self.gravity != 0:
            self.jumping = True
        if self.gravity <= 15:
            self.gravity = self.gravity+0.5
        if self.moving_right:
            self.direction = 1
            if self.able_to_move_right(objects):
                self.Location = (self.Location[0] + 2.5, self.Location[1])
        if self.moving_left:
            self.direction = 2
            if self.able_to_move_left(objects):
                self.Location = (self.Location[0] - 2.5, self.Location[1])
        if self.alive:
            self.able_to_move_up(objects)
            if self.able_to_move_down(objects):
                self.Location = (self.Location[0], self.Location[1] + self.gravity)
            if not self.able_to_move_down(objects):
                self.gravity = 0
            if self.direction == 0:
                screen.blit(self.images[self.direction], (self.Location[0],self.Location[1]-8))
            else:
                screen.blit(self.images[self.direction], self.Location)
        self.direction = 0

    def start_jump(self):
        self.Location = (self.Location[0],self.Location[1]-5)
        if not self.jumping:
            self.gravity = -11.5
            self.jumping = True


    def move_right(self):
        self.moving_right = True

    def stop_moving_right(self):
        self.moving_right = False

    def stop_moving_left(self):
        self.moving_left = False

    def move_left(self):
        self.moving_left = True

    def able_to_move_left(self, objects):
        uploc = (self.Location[0], self.Location[1])
        downloc = (self.Location[0], self.Location[1]+45)
        for obj in objects:
            if obj.top_right()[1] <= uploc[1] <= obj.right_bottom()[1]:
                if obj.top_right()[0] >= uploc[0] >= obj.right_bottom()[0]:
                    return False
            if obj.top_right()[1] <= downloc[1] <= obj.right_bottom()[1]:
                if obj.top_right()[0] >= downloc[0] >= obj.right_bottom()[0]:
                    return False
        return True

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

    def able_to_move_up(self,objects):
        loc = (self.Location[0]+2,self.Location[1])
        for obj in objects:
            if obj.top_left()[1] <= loc[1] <= obj.left_bottom()[1]:
                if obj.top_left()[0] <= loc[0] <= obj.top_right()[0]:
                    self.gravity = 0.5
                    self.Location = (self.Location[0], obj.left_bottom()[1]+0.5)
            if obj.top_left()[1] <= loc[1] <= obj.left_bottom()[1]:
                if obj.top_left()[0] <= loc[0]+32 <= obj.top_right()[0]:
                    self.gravity = 0.5
                    self.Location = (self.Location[0], obj.left_bottom()[1]+0.5)

    def able_to_move_down(self, objects):
        down_loc = (self.Location[0]+3, self.Location[1]+47)
        for obj in objects:
            if obj.top_left()[1] <= down_loc[1] <= obj.left_bottom()[1]:
                if obj.top_left()[0] <= down_loc[0] <= obj.top_right()[0]:
                    self.jumping = False
                    self.gravity = 2.5
                    self.Location = (self.Location[0], obj.top_left()[1]-45)
                    return False
            if obj.top_left()[1] <= down_loc[1] <= obj.left_bottom()[1]:
                if obj.top_left()[0] <= down_loc[0]+32 <= obj.top_right()[0]:
                    self.jumping = False
                    self.gravity = 2.5
                    self.Location = (self.Location[0], obj.top_left()[1]-45)
                    return False
        return True





