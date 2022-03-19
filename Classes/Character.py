from main import screen
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
