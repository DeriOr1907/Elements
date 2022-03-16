class Character:
    def __init__(self,Location,Gender,Color,Img,):
        self.Location = Location
        self.Gender = Gender
        self.Color = Color
        self.Direction = 0 # -1 is left 0 is straight 1 is right
        self.IMG = Img
        self.Alive =True
