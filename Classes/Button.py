from Constants import screen
class Button:
    def __init__(self,image,Location,height,width):
        self.image = image
        self.Location = Location
        self.height = height
        self.width = width


    def display_button(self):
        screen.blit(self.image, self.Location)