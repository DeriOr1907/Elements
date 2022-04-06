from Classes.Character import *
from Classes.Object import *
from Classes.Button import *
from helpers import *
from Classes.Lava import *
pygame.display.set_caption('Elements')
clock = pygame.time.Clock()
from Classes.Door import *
import time


def play_music(str):
    sound = pygame.mixer.Sound(str)
    pygame.mixer.Sound.play(sound)

def loser():
    sound = pygame.mixer.Sound("Sounds/loser.ogg")
    pygame.mixer.Sound.play(sound)

def lose_sound():
    sound = pygame.mixer.Sound("Sounds/death sound.mp3")
    pygame.mixer.Sound.play(sound)


def win_sound():
    sound = pygame.mixer.Sound("Sounds/win sound.mp3")
    pygame.mixer.Sound.play(sound)


def button_click():
    sound = pygame.mixer.Sound("Sounds/Wooden Button Click Sound Effect.mp3")
    pygame.mixer.Sound.play(sound)


def create_images_list(imgpath1, imgpath2, imgpath3):
    imags = [pygame.transform.scale(pygame.image.load(imgpath1), (36, 55)),
             pygame.transform.scale(pygame.image.load(imgpath2), (41, 45)),
             pygame.transform.scale(pygame.image.load(imgpath3), (41, 45))]
    return imags


start_background = pygame.transform.scale(pygame.image.load("Images/StartPic!!!.png"), screen_size)
Play_BUTTON = pygame.transform.scale(pygame.image.load("Images/PlayButton!!!.png"), (90, 90))
Play_BUTTON = Button(Play_BUTTON, (450, 200), 85, 85)

oneButton = pygame.transform.scale(pygame.image.load("Images/1button.png"), (70,70))
oneButton = Button(oneButton,(50 - 10, 150),70,70)
twoButton = pygame.transform.scale(pygame.image.load("Images/2button.png"), (70,70))
twoButton = Button(twoButton,(130 - 10, 150),70,70)
threeButton = pygame.transform.scale(pygame.image.load("Images/3button.png"), (70,70))
threeButton = Button(threeButton,(210 - 10, 150),70,70)
fourButton = pygame.transform.scale(pygame.image.load("Images/4button.png"), (70,70))
fourButton = Button(fourButton,(290 - 10, 150),70,70)

one_Button = pygame.transform.scale(pygame.image.load("Images/1button.png"), (70,70))
one_Button = Button(one_Button, (720-70, 150),70,70)
two_Button = pygame.transform.scale(pygame.image.load("Images/2button.png"), (70,70))
two_Button = Button(two_Button, (800-70, 150),70,70)
three_Button = pygame.transform.scale(pygame.image.load("Images/3button.png"), (70,70))
three_Button = Button(three_Button, (880-70, 150),70,70)
four_Button = pygame.transform.scale(pygame.image.load("Images/4button.png"), (70,70))
four_Button = Button(four_Button, (960-70, 150), 70, 70)

objects_color = (95, 80, 45)
o1 = Object(1050, 30, 0, 500, objects_color)
o2 = Object(20, 530, 0, 0, objects_color)
o3 = Object(20, 530, 980, 0, objects_color)
o4 = Object(1050, 25, 0, 0, objects_color)
obj1 = Object(1050, 50, 0, 515, objects_color)
obj2 = Object(25, 530, 0, 0, objects_color)
obj3 = Object(30, 530, 975, 0, objects_color)
obj4 = Object(1050, 15, 0, 0, objects_color)
obj5 = Object(130, 60, 181, 475, objects_color)
obj6 = Object(90, 50, 221, 435, objects_color)
obj7 = Object(50, 50, 261, 395, objects_color)
obj8 = Object(181, 15, 0, 330, objects_color)
obj9 = Object(70, 50, 25, 293, objects_color)
obj10 = Object(115, 15, 100, 230, objects_color)
obj11 = Object(200, 15, 0, 90, objects_color)
obj12 = Object(150, 15, 250, 130, objects_color)
obj13 = Object(15, 155, 195, 90, objects_color)
obj14 = Object(40, 15, 350, 440, objects_color)
obj15 = Object(130, 60, 689, 475, objects_color)
obj16 = Object(90, 50, 689, 435, objects_color)
obj17 = Object(50, 50, 689, 395, objects_color)
obj18 = Object(40, 15, 610, 440, objects_color)
obj19 = Object(40, 15, 480, 350, objects_color)
obj20 = Object(600, 15, 600, 280, objects_color)
obj21 = Object(250, 15, 840, 200, objects_color)
obj22 = Object(300, 15, 595, 90, objects_color)
obj23 = Object(40, 15, 440, 200, objects_color)
obj24 = Object(40, 15, 515, 150, objects_color)
obj25 = Object(23, 55, 308, 500, objects_color)
obj26 = Object(25, 55, 665, 500, objects_color)
obj27 = Object(15, 55, 904, 500, objects_color)
obj28 = Object(15, 55, 80, 500, objects_color)
obj29 = Object(50, 50, 925, 160, objects_color)
obj30 = Object(15, 15, 725, 265, objects_color)
obj31 = Object(15, 15, 625, 265, objects_color)

objects2 = [obj1, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9, obj10, obj11, obj12, obj14, obj15, obj16, obj17, obj18, obj19, obj20, obj21, obj22, obj23, obj24, obj25, obj26, obj27, obj28, obj29, obj30, obj31]

o5 = Object(220, 15, 0, 100, objects_color)
o6 = Object(200, 15, 780, 100, objects_color)
o7 = Object(425, 25, 285, 225, objects_color)
o8 = Object(300, 25, 0, 325, objects_color)
o9 = Object(300, 25, 700, 325, objects_color)
o10 = Object(300, 100, 250, 420, objects_color)
o11 = Object(60, 100, 718, 450, objects_color)
o12 = Object(80, 15, 590, 410, objects_color)

o13 = Object(50, 20, 400, 210, objects_color)
o14 = Object(50, 20, 535, 210, objects_color)

objects1 = [o1, o2, o3, o4, o5, o6, o7, o8, o9, o10, o11, o12, o13, o14]

level = 1

def level2(red,blue,pink,purple,RED,BLUE,PINK,PURPLE):
    background = pygame.transform.scale(pygame.image.load("Images/background2.jpeg"), screen_size)
    run = True
    girl_lava1 = None
    boy_lava1 = None
    girl = None
    boy = None
    lavas = None
    boy_door = None
    girl_door = None
    home_button = None
    green_lava1 = Lava("Images/green lava.PNG", "green", (580, 500))
    green_lava2 = Lava("Images/green lava.PNG", "green", (497, 500))
    green_lava3 = Lava("Images/green lava.PNG", "green", (414, 500))
    green_lava4 = Lava("Images/green lava.PNG", "green", (331, 500))
    green_lava5 = Lava("Images/green lava.PNG", "green", (640, 265))
    B = False
    retry = True
    while run:
        if retry:
            play_music("Sounds/backgroundSoundtrack2.ogg")
            if not red:
                y = create_images_list("Images/Redgirl.png", "Images/RedGRun.PNG", "Images/RedGRunLeft.PNG")
                girl = Character((35, 450), "red", y)
                girl_lava1 = Lava("Images/red lava.PNG", "red", (95, 500))
                girl_door = Door("Images/DoorGirlRed.png", "red", (30, 30))

                girl_diamond1 = Diamond("Images/DRed!.png", "red", (741, 405))
                girl_diamond2 = Diamond("Images/DRed!.png", "red", (930, 250))
                girl_diamond3 = Diamond("Images/DRed!.png", "red", (125, 200))
                girl_diamond4 = Diamond("Images/DRed!.png", "red", (445, 170))
                girl_diamond5 = Diamond("Images/DRed!.png", "red", (650, 60))
            if not blue:
                y = create_images_list("Images/Bluegirl.png", "Images/BlueGRun.PNG", "Images/BlueGRunLeft.PNG")
                girl = Character((35, 450), "blue", y)
                girl_lava1 = Lava("Images/blue lava.PNG", "blue", (95, 500))
                girl_door = Door("Images/DoorGirlBlue.png", "blue", (30, 30))

                girl_diamond1 = Diamond("Images/DBlue.png", "blue", (741, 405))
                girl_diamond2 = Diamond("Images/DBlue.png", "blue", (930, 250))
                girl_diamond3 = Diamond("Images/DBlue.png", "blue", (125, 200))
                girl_diamond4 = Diamond("Images/DBlue.png", "blue", (445, 170))
                girl_diamond5 = Diamond("Images/DBlue.png", "blue", (650, 60))
            if not pink:
                y = create_images_list("Images/Pinkgirl.png", "Images/PinkGRun.PNG", "Images/PinkGRunLeft.PNG")
                girl = Character((35, 450), "pink", y)
                girl_lava1 = Lava("Images/pink lava.PNG", "pink", (95, 500))
                girl_door = Door("Images/DoorGirlPink.png", "pink", (30, 30))

                girl_diamond1 = Diamond("Images/DPink.png", "pink", (741, 405))
                girl_diamond2 = Diamond("Images/DPink.png", "pink", (930, 250))
                girl_diamond3 = Diamond("Images/DPink.png", "pink", (125, 200))
                girl_diamond4 = Diamond("Images/DPink.png", "pink", (445, 170))
                girl_diamond5 = Diamond("Images/DPink.png", "pink", (650, 60))
            if not purple:
                y = create_images_list("Images/Purplegirl.png", "Images/PurpleGRun.PNG", "Images/PurpleGRunLeft.PNG")
                girl = Character((35, 450), "purple", y)
                girl_lava1 = Lava("Images/purple lava.PNG", "purple", (95, 500))
                girl_door = Door("Images/DoorGirlPurple.png", "purple", (30, 30))

                girl_diamond1 = Diamond("Images/DPurple.png", "purple", (741, 405))
                girl_diamond2 = Diamond("Images/DPurple.png", "purple", (930, 250))
                girl_diamond3 = Diamond("Images/DPurple.png", "purple", (125, 200))
                girl_diamond4 = Diamond("Images/DPurple.png", "purple", (445, 170))
                girl_diamond5 = Diamond("Images/DPurple.png", "purple", (650, 60))
            if not RED:
                x = create_images_list("Images/Redboy.png", "Images/RedBRun.PNG", "Images/RedBRunLeft.PNG")
                boy = Character((920, 450), "red", x)
                boy_lava1 = Lava("Images/red lava.PNG", "red", (819, 500))
                boy_door = Door("Images/DoorBoyRed.png", "red", (800, 30))

                boy_diamond1 = Diamond("Images/DRed!.png", "red", (225, 405))
                boy_diamond2 = Diamond("Images/DRed!.png", "red", (485, 320))
                boy_diamond3 = Diamond("Images/DRed!.png", "red", (160, 200))
                boy_diamond4 = Diamond("Images/DRed!.png", "red", (895, 250))
                boy_diamond5 = Diamond("Images/DRed!.png", "red", (150, 60))
            if not BLUE:
                x = create_images_list("Images/Blueboy.png", "Images/BlueBRun.PNG", "Images/BlueBRunLeft.PNG")
                boy = Character((920, 450), "blue", x)
                boy_lava1 = Lava("Images/blue lava.PNG", "blue", (819, 500))
                boy_door = Door("Images/DoorBoyBlue.png", "blue", (800, 30))

                boy_diamond1 = Diamond("Images/DBlue.png", "blue", (225, 405))
                boy_diamond2 = Diamond("Images/DBlue.png", "blue", (485, 320))
                boy_diamond3 = Diamond("Images/DBlue.png", "blue", (160, 200))
                boy_diamond4 = Diamond("Images/DBlue.png", "blue", (895, 250))
                boy_diamond5 = Diamond("Images/DBlue.png", "blue", (150, 60))
            if not PINK:
                x = create_images_list("Images/Pinkboy.png", "Images/PinkBRun.PNG", "Images/PinkBRunLeft.PNG")
                boy = Character((920, 450), "pink", x)
                boy_lava1 = Lava("Images/pink lava.PNG", "pink", (819, 500))
                boy_door = Door("Images/DoorBoyPink.png", "pink", (800, 30))

                boy_diamond1 = Diamond("Images/DPink.png", "pink", (225, 405))
                boy_diamond2 = Diamond("Images/DPink.png", "pink", (485, 320))
                boy_diamond3 = Diamond("Images/DPink.png", "pink", (160, 200))
                boy_diamond4 = Diamond("Images/DPink.png", "pink", (895, 250))
                boy_diamond5 = Diamond("Images/DPink.png", "pink", (150, 60))
            if not PURPLE:
                x = create_images_list("Images/Purpleboy.png", "Images/PurpleBRun.PNG", "Images/PurpleBRunLeft.PNG")
                boy = Character((920, 450), "purple", x)
                boy_lava1 = Lava("Images/purple lava.PNG", "purple", (819, 500))
                boy_door = Door("Images/DoorBoyPurple.png", "purple", (800, 30))

                boy_diamond1 = Diamond("Images/DPurple.png", "purple", (225, 405))
                boy_diamond2 = Diamond("Images/DPurple.png", "purple", (485, 320))
                boy_diamond3 = Diamond("Images/DPurple.png", "purple", (160, 200))
                boy_diamond4 = Diamond("Images/DPurple.png", "purple", (895, 250))
                boy_diamond5 = Diamond("Images/DPurple.png", "purple", (150, 60))

        doors = [boy_door, girl_door]
        lavas = [green_lava1, green_lava2, green_lava3, green_lava4, green_lava5, boy_lava1, girl_lava1, green_lava1]
        diamonds = [girl_diamond1, girl_diamond2, girl_diamond3, girl_diamond4, girl_diamond5, boy_diamond1, boy_diamond2, boy_diamond3, boy_diamond4, boy_diamond5]

        while boy.alive and girl.alive and run:  # Caharater1 is alive and Caracter2 is alive and Bool:
            retry = False
            screen.blit(background, (0, 0))
            for obstacle in objects2:
                obstacle.display_obstacle()
            for door in doors:
                door.display_door()
            for diamond in diamonds:
                diamond.display_diamond()
            girl.display_character(objects2, lavas)
            boy.display_character(objects2, lavas)
            if boy.door(doors) and girl.door(doors):
                run = False
            for lava in lavas:
                lava.display_lava()
            # refreshing screen:
            pygame.display.flip()
            pygame.display.update()
            clock.tick(65)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        boy.move_right()
                    if event.key == pygame.K_LEFT:
                        boy.move_left()
                    if event.key == pygame.K_UP:
                        boy.start_jump()

                    if event.key == pygame.K_d:
                        girl.move_right()
                    if event.key == pygame.K_a:
                        girl.move_left()
                    if event.key == pygame.K_w:
                        girl.start_jump()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        boy.stop_moving_right()
                    if event.key == pygame.K_LEFT:
                        boy.stop_moving_left()

                    if event.key == pygame.K_d:
                        girl.stop_moving_right()
                    if event.key == pygame.K_a:
                        girl.stop_moving_left()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            B = True
        if run:
            retry_button = pygame.transform.scale(pygame.image.load("Images/retry-icon-9.jpg"), (100, 100))
            retry_button = Button(retry_button,(450,200),100,100)
            home_button = pygame.transform.scale(pygame.image.load("Images/home.png"),(65,65))
            home_button = Button(home_button,(468,310),65,65)
            screen.blit(background, (0, 0))
            retry_button.display_button()
            home_button.display_button()
            pygame.display.flip()
            pygame.display.update()
            if B:
                pygame.mixer.stop()
                loser()
                lose_sound()
                B = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if mouse_in_button(retry_button, mouse_pos):
                        retry = True
                    if mouse_in_button(home_button,mouse_pos):
                        run = False
                        home(2)
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
    pygame.mixer.stop()
    win_sound()
    return 1

# set clock
def level1(red,blue,pink,purple,RED,BLUE,PINK,PURPLE):
    background = pygame.transform.scale(pygame.image.load("Images/background2.jpeg"), screen_size)
    run = True
    girl_lava1 = None
    boy_lava1 = None
    girl = None
    boy = None
    lavas = None
    boy_door = None
    girl_door = None
    home_button = None
    green_lava1 = Lava("Images/green lava.PNG", "green", (450, 210))
    green_lava2 = Lava("Images/green lava.PNG", "green", (550, 485))
    green_lava3 = Lava("Images/green lava.PNG", "green", (634, 485))
    B = False
    retry = True
    while run:
        if retry:
            play_music("Sounds/backgroundSoundtrack2.ogg")
            if not red:
                y = create_images_list("Images/Redgirl.png", "Images/RedGRun.PNG", "Images/RedGRunLeft.PNG")
                girl = Character((30, 60), "red", y)
                girl_door = Door("Images/DoorGirlRed.png", "red",(30, 440))

                girl_diamond1 = Diamond("Images/DRed!.png", "red", (860, 70))
                girl_diamond2 = Diamond("Images/DRed!.png", "red", (860, 295))
                girl_diamond3 = Diamond("Images/DRed!.png", "red", (860, 470))
            if not blue:
                y = create_images_list("Images/Bluegirl.png", "Images/BlueGRun.PNG", "Images/BlueGRunLeft.PNG")
                girl = Character((30, 60), "blue", y)
                girl_door = Door("Images/DoorGirlBlue.png", "blue",(30, 440))

                girl_diamond1 = Diamond("Images/DBlue.png", "blue", (860, 70))
                girl_diamond2 = Diamond("Images/DBlue.png", "blue", (860, 295))
                girl_diamond3 = Diamond("Images/DBlue.png", "blue", (860, 470))
            if not pink:
                y = create_images_list("Images/Pinkgirl.png", "Images/PinkGRun.PNG", "Images/PinkGRunLeft.PNG")
                girl = Character((30, 60), "pink", y)
                girl_door = Door("Images/DoorGirlPink.png", "pink",(30, 440))

                girl_diamond1 = Diamond("Images/DPink.png", "pink", (860, 70))
                girl_diamond2 = Diamond("Images/DPink.png", "pink", (860, 295))
                girl_diamond3 = Diamond("Images/DPink.png", "pink", (860, 470))
            if not purple:
                y = create_images_list("Images/Purplegirl.png", "Images/PurpleGRun.PNG", "Images/PurpleGRunLeft.PNG")
                girl = Character((30, 60), "purple", y)
                girl_door = Door("Images/DoorGirlPurple.png", "purple", (30, 440))

                girl_diamond1 = Diamond("Images/DPurple.png", "purple", (860, 70))
                girl_diamond2 = Diamond("Images/DPurple.png", "purple", (860, 295))
                girl_diamond3 = Diamond("Images/DPurple.png", "purple", (860, 470))

            if not RED:
                x = create_images_list("Images/Redboy.png", "Images/RedBRun.PNG", "Images/RedBRunLeft.PNG")
                boy = Character((930, 60), "red", x)
                boy_door = Door("Images/DoorBoyRed.png","red",(90, 440))

                boy_diamond1 = Diamond("Images/DRed!.png", "red", (110, 70))
                boy_diamond2 = Diamond("Images/DRed!.png", "red", (110, 295))
                boy_diamond3 = Diamond("Images/DRed!.png", "red", (900, 470))

            if not BLUE:
                x = create_images_list("Images/Blueboy.png", "Images/BlueBRun.PNG", "Images/BlueBRunLeft.PNG")
                boy = Character((930, 60), "blue", x)
                boy_door = Door("Images/DoorBoyBlue.png", "blue", (90, 440))

                boy_diamond1 = Diamond("Images/DBlue.png", "blue", (110, 70))
                boy_diamond2 = Diamond("Images/DBlue.png", "blue", (110, 295))
                boy_diamond3 = Diamond("Images/DBlue.png", "blue", (900, 470))
            if not PINK:
                x = create_images_list("Images/Pinkboy.png", "Images/PinkBRun.PNG", "Images/PinkBRunLeft.PNG")
                boy = Character((930, 60), "pink", x)
                boy_door = Door("Images/DoorBoyPink.png", "pink", (90, 440))

                boy_diamond1 = Diamond("Images/DPink.png", "pink", (110, 70))
                boy_diamond2 = Diamond("Images/DPink.png", "pink", (110, 295))
                boy_diamond3 = Diamond("Images/DPink.png", "pink", (900, 470))
            if not PURPLE:
                x = create_images_list("Images/Purpleboy.png", "Images/PurpleBRun.PNG", "Images/PurpleBRunLeft.PNG")
                boy = Character((930, 60), "purple", x)
                boy_door = Door("Images/DoorBoyPurple.png", "purple", (90, 440))

                boy_diamond1 = Diamond("Images/DPurple.png", "purple", (110, 70))
                boy_diamond2 = Diamond("Images/DPurple.png", "purple", (110, 295))
                boy_diamond3 = Diamond("Images/DPurple.png", "purple", (900, 470))

        doors = [boy_door, girl_door]
        lavas = [green_lava1, green_lava2, green_lava3]
        diamonds = [boy_diamond1, boy_diamond2, boy_diamond3, girl_diamond1, girl_diamond2, girl_diamond3]
        t0 = time.time()
        while boy.alive and girl.alive and run:  # Caharater1 is alive and Caracter2 is alive and Bool:
            retry = False
            screen.blit(background, (0, 0))
            for obstacle in objects1:
                obstacle.display_obstacle()
            for door in doors:
                door.display_door()
            for diamond in diamonds:
                diamond.display_diamond()
            girl.display_character(objects1, lavas)
            boy.display_character(objects1, lavas)
            if boy.door(doors) and girl.door(doors):
                run = False
            for lava in lavas:
                lava.display_lava()
            # refreshing screen:
            pygame.display.flip()
            pygame.display.update()
            clock.tick(65)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        boy.move_right()
                    if event.key == pygame.K_LEFT:
                        boy.move_left()
                    if event.key == pygame.K_UP:
                        boy.start_jump()

                    if event.key == pygame.K_d:
                        girl.move_right()
                    if event.key == pygame.K_a:
                        girl.move_left()
                    if event.key == pygame.K_w:
                        girl.start_jump()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        boy.stop_moving_right()
                    if event.key == pygame.K_LEFT:
                        boy.stop_moving_left()

                    if event.key == pygame.K_d:
                        girl.stop_moving_right()
                    if event.key == pygame.K_a:
                        girl.stop_moving_left()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            B = True
        if run:
            retry_button = pygame.transform.scale(pygame.image.load("Images/retry-icon-9.jpg"), (100, 100))
            retry_button = Button(retry_button,(450,200),100,100)
            home_button = pygame.transform.scale(pygame.image.load("Images/home.png"),(65,65))
            home_button = Button(home_button,(468,310),65,65)
            screen.blit(background, (0, 0))
            retry_button.display_button()
            home_button.display_button()
            pygame.display.flip()
            pygame.display.update()
            if B:
                pygame.mixer.stop()
                loser()
                lose_sound()
                B = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if mouse_in_button(retry_button, mouse_pos):
                        retry = True
                    if mouse_in_button(home_button,mouse_pos):
                        run = False
                        home(1)
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
    pygame.mixer.stop()
    win_sound()
    print(time.time() - t0)
    return 1



# sending the results to whatsapp
def home(level):
    start_run = True
    play_music("Sounds/startSoundTrack.mp3")
    blue = False
    red = True
    pink = True
    purple = True

    BLUE = True
    RED = False
    PINK = True
    PURPLE = True
    start_pic = pygame.transform.scale(pygame.image.load("Images/StartPic!!!.png"), screen_size)
    background = pygame.transform.scale(pygame.image.load("Images/background2.jpeg"), screen_size)

    big_boy = pygame.transform.scale(pygame.image.load("Images/Redboy.png"), (170, 280))
    big_girl = pygame.transform.scale(pygame.image.load("Images/Bluegirl.png"), (170, 285))

    while start_run:
        screen.blit(start_background, (0, 0))
        screen.blit(big_girl, (105, 225))
        screen.blit(big_boy, (730, 230))
        Play_BUTTON.display_button()

        if red: one_Button.display_button()
        if blue: two_Button.display_button()
        if pink: three_Button.display_button()
        if purple: four_Button.display_button()

        if RED: oneButton.display_button()
        if BLUE: twoButton.display_button()
        if PINK: threeButton.display_button()
        if PURPLE: fourButton.display_button()

        pygame.display.flip()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_in_button(Play_BUTTON, event.pos):
                    button_click()
                    start_run = False
                if RED:
                    if mouse_in_button(oneButton,event.pos):
                        big_girl = pygame.transform.scale(pygame.image.load("Images/Redgirl.png"), (170, 280))
                        red = False
                        blue = True
                        pink = True
                        purple = True
                        button_click()
                if BLUE:
                    if mouse_in_button(twoButton,event.pos):
                        big_girl = pygame.transform.scale(pygame.image.load("Images/Bluegirl.png"), (170, 280))
                        red = True
                        blue = False
                        pink = True
                        purple = True
                        button_click()
                if PINK:
                    if mouse_in_button(threeButton,event.pos):
                        big_girl = pygame.transform.scale(pygame.image.load("Images/Pinkgirl.png"), (170, 280))
                        red = True
                        blue = True
                        pink = False
                        purple = True
                        button_click()
                if PURPLE:
                    if mouse_in_button(fourButton,event.pos):
                        big_girl = pygame.transform.scale(pygame.image.load("Images/Purplegirl.png"), (170, 280))
                        red = True
                        blue = True
                        pink = True
                        purple = False
                        button_click()

                if red:
                    if mouse_in_button(one_Button,event.pos):
                        big_boy = pygame.transform.scale(pygame.image.load("Images/Redboy.png"), (170, 285))
                        RED = False
                        BLUE = True
                        PINK = True
                        PURPLE = True
                        button_click()
                if blue:
                    if mouse_in_button(two_Button,event.pos):
                        big_boy = pygame.transform.scale(pygame.image.load("Images/Blueboy.png"), (170, 285))
                        RED = True
                        BLUE = False
                        PINK = True
                        PURPLE = True
                        button_click()
                if pink:
                    if mouse_in_button(three_Button,event.pos):
                        big_boy = pygame.transform.scale(pygame.image.load("Images/Pinkboy.png"), (170, 285))
                        RED = True
                        BLUE = True
                        PINK = False
                        PURPLE = True
                        button_click()
                if purple:
                    if mouse_in_button(four_Button,event.pos):
                        big_boy = pygame.transform.scale(pygame.image.load("Images/Purpleboy.png"), (170, 285))
                        RED = True
                        BLUE = True
                        PINK = True
                        PURPLE = False
                        button_click()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    pygame.mixer.stop()
    if level == 1:
        level = level + level1(red, blue, pink, purple, RED, BLUE, PINK, PURPLE)
    if level == 2:
        level = level + level2(red, blue, pink, purple, RED, BLUE, PINK, PURPLE)

home(level)

print("gever retzah ata")
quit()