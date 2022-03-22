from Constants import screen
class Character:
    def __init__(self,Location,Color,Img):
        self.Location = Location
        self.color = Color
        self.direction = 0 # 0 is forward, 1 is right and 2 is left
        self.images = Img
        self.alive = True

    def display_character(self):
        if self.alive:
            screen.blit(self.images[self.direction], self.Location)
        self.direction = 0
    def move_right(self):
        self.direction = 1
        self.Location = (self.Location[0]+1, self.Location[1])
    def move_left(self):
        self.direction = 2
        self.Location = (self.Location[0]-1, self.Location[1])