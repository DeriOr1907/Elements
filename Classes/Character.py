from Constants import screen
from Classes.Object import *
from Classes.Lava import *
from Classes.Diamond import *

gravity = 2.5


class Character:
    def __init__(self, Location, Color, Img):
        self.Location = Location
        self.color = Color
        self.direction = 0 # 0 is forward, 1 is right and 2 is left
        self.images = Img
        self.alive = True
        self.moving_right = False
        self.moving_left = False
        self.jumping = False
        self.gravity = 0

    def display_character(self, objects, lavas, walls):
        self.lava(lavas)
        if self.gravity != 0:
            self.jumping = True
        if self.gravity <= 15:
            self.gravity = self.gravity+0.1
        if self.moving_right:
            self.direction = 1
            if self.able_to_move_right(objects) and self.able_to_move_right(walls):
                self.Location = (self.Location[0] + 1, self.Location[1])
        if self.moving_left:
            self.direction = 2
            if self.able_to_move_left(objects) and self.able_to_move_left(walls):
                self.Location = (self.Location[0] - 1, self.Location[1])
        if self.alive:
            self.able_to_move_up(objects)
            self.able_to_move_up(walls)
            if self.able_to_move_down(objects) and self.able_to_move_down(walls):
                self.Location = (self.Location[0], self.Location[1] + self.gravity)
            if not self.able_to_move_down(objects) and not self.able_to_move_down(walls):
                self.gravity = 0
            if self.direction == 0:
                screen.blit(self.images[self.direction], (self.Location[0],self.Location[1]-8))
            else:
                screen.blit(self.images[self.direction], self.Location)
        self.direction = 0

    def start_jump(self):
        self.Location = (self.Location[0],self.Location[1]-5)
        if not self.jumping:
            self.gravity = -5
            self.jumping = True

    def set_location(self,loc):
        self.Location = loc

    def move_right(self):
        self.moving_right = True

    def stop_moving_right(self):
        self.moving_right = False

    def stop_moving_left(self):
        self.moving_left = False

    def move_left(self):
        self.moving_left = True

    def top_left(self):
        return self.Location

    def top_right(self):
        x = (self.Location[0] + 40, self.Location[1])
        return x

    def right_bottom(self):
        x = (self.Location[0] + 40, self.Location[1] + 45)
        return x

    def left_bottom(self):
        x = (self.Location[0], self.Location[1] + 45)
        return x

    def door(self, doors):
        loc = (self.Location[0]+20, self.Location[1]+20)
        for d in doors:
            if d.top_right()[1] <= loc[1] <= d.right_bottom()[1]:
                if d.top_right()[0] >= loc[0] >= d.left_bottom()[0]:
                    if d.color == self.color:
                        return True

#def Gem():

    def lava(self, lavas):
        downlocleft = (self.Location[0], self.Location[1]+42)
        downlocright = (self.Location[0]+40, self.Location[1]+42)
        for l in lavas:
            if l.top_right()[1] <= downlocleft[1] <= l.right_bottom()[1]:
                if l.top_right()[0] >= downlocleft[0] >= l.left_bottom()[0]:
                    if l.color != self.color:
                        self.alive = False
            if l.top_right()[1] <= downlocright[1] <= l.right_bottom()[1]:
                if l.top_right()[0] >= downlocright[0] >= l.left_bottom()[0]:
                    if l.color != self.color:
                        self.alive = False

    def able_to_move_left(self, objects):
        uploc = (self.Location[0], self.Location[1])
        downloc = (self.Location[0], self.Location[1]+40)
        rightloc = self.Location[0]+40
        for obj in objects:
            if obj.top_right()[1] <= uploc[1] <= obj.right_bottom()[1]:
                if obj.top_right()[0] >= uploc[0] >= obj.right_bottom()[0]:
                    return False
            if obj.top_right()[1] <= downloc[1] <= obj.right_bottom()[1]:
                if obj.top_right()[0] >= downloc[0] >= obj.right_bottom()[0]:
                    return False
            if downloc[1] <= obj.top_right()[1] <= uploc[1]:
                if uploc[0] <= obj.top_right()[0] <= rightloc:
                    return False

        return True

    def able_to_move_right(self, objects):
        uploc = (self.Location[0]+40, self.Location[1])
        downloc = (self.Location[0]+40, self.Location[1]+45)
        leftloc = self.Location[0]
        for obj in objects:
            if obj.top_left()[1] <= uploc[1] <= obj.left_bottom()[1]:
                if obj.top_left()[0] >= uploc[0] >= obj.left_bottom()[0]:
                    return False
            if obj.top_left()[1] <= downloc[1] <= obj.left_bottom()[1]:
                if obj.top_left()[0] >= downloc[0] >= obj.left_bottom()[0]:
                    return False
            if downloc[1] <= obj.top_left()[1] <= uploc[1]:
                if leftloc <= obj.top_left()[0] <= uploc[0]:
                    return False
        return True

    def able_to_move_up(self,objects):
        loc = (self.Location[0]+1,self.Location[1])
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





