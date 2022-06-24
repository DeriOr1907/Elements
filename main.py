from Classes.Button import *
from Classes.Wall import *
from Classes.Star import *
from Classes.Portal import *
from Classes.Door import *
from Classes.Magic_Button import *
import time
import random
from datetime import datetime

pygame.display.set_caption('Elements')
clock = pygame.time.Clock()


def mouse_in_button(button, mouse_pos):
    if button.Location[0] + button.width > mouse_pos[0] > button.Location[0] and button.Location[1] < mouse_pos[1] < button.Location[1] + button.height:
        return True


pygame.mixer.init()


def play_music(str):
    sound = pygame.mixer.Sound(str)
    pygame.mixer.Sound.play(sound)


def gem():
    sound = pygame.mixer.Sound("Sounds/loser.ogg")
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

# def hebrew(text):
#     return unicode(text,  "Windows-1255")

def get_str(x,y):
    pressed_enter = False
    phoneNum = ""
    pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(x,y, 150, 20))
    pygame.display.flip()
    pygame.draw.rect(screen, (255, 255, 255),
                     pygame.Rect(x , y , 148, 18))
    pygame.display.flip()
    while not pressed_enter:
        # get the string for comment
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.draw.rect(screen, (50, 50, 50),
                                 pygame.Rect(x,y, 150, 20))
                pygame.display.flip()
                pygame.draw.rect(screen, (255, 255, 255),
                                 pygame.Rect(x,y, 148, 18))
                pygame.display.flip()
                if event.key == pygame.K_RETURN:
                    pressed_enter = True
                elif event.key == pygame.K_BACKSPACE \
                        and not (len(phoneNum) == 0):
                    phoneNum = phoneNum[:-1]
                else:
                    phoneNum += event.unicode
                font2 = pygame.font.SysFont('chalkduster.ttf', 25, bold=False)
                img2 = font2.render(phoneNum, True, (50, 50, 50))
                screen.blit(img2, (x, y))
                pygame.display.update()

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    return phoneNum

# pywhatkit.sendwhatmsg()

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
one_Button = Button(one_Button,(720-70, 150),70,70)
two_Button = pygame.transform.scale(pygame.image.load("Images/2button.png"), (70,70))
two_Button = Button(two_Button,(800-70, 150),70,70)
three_Button = pygame.transform.scale(pygame.image.load("Images/3button.png"), (70,70))
three_Button = Button(three_Button,(880-70, 150),70,70)
four_Button = pygame.transform.scale(pygame.image.load("Images/4button.png"), (70,70))
four_Button = Button(four_Button,(960-70, 150),70,70)

sound_button = pygame.transform.scale(pygame.image.load("Images/sound.png"), (30,30))
sound_button = Button(sound_button,(950, 10),30,30)
no_sound_button = pygame.transform.scale(pygame.image.load("Images/no sound.png"), (30,30))
no_sound_button = Button(no_sound_button,(950, 10),30,30)
sound_on = True
timer = pygame.transform.scale(pygame.image.load("Images/timer.png"), (53,53))

objects_color = (95, 80, 45)
o1 = Object(1050, 30, 0, 500, objects_color)
o2 = Object(30, 530, -10, 0, objects_color)
o3 = Object(30, 530, 980, 0, objects_color)
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
obj18 = Object(40, 15, 600, 440, objects_color)
obj19 = Object(120, 15, 430, 350, objects_color)
obj20 = Object(600, 15, 600, 280, objects_color)
obj21 = Object(250, 15, 840, 200, objects_color)
obj22 = Object(300, 15, 595, 90, objects_color)
obj23 = Object(40, 15, 435, 200, objects_color)
obj24 = Object(40, 15, 515, 150, objects_color)
obj25 = Object(23, 55, 308, 500, objects_color)
obj26 = Object(25, 55, 665, 500, objects_color)
obj27 = Object(15, 55, 904, 500, objects_color)
obj28 = Object(15, 55, 80, 500, objects_color)
obj29 = Object(50, 50, 925, 160, objects_color)
obj30 = Object(15, 15, 780, 265, objects_color)
obj31 = Object(15, 30, 595, 265, objects_color)

objects4 = [obj1, obj2, obj3, o4, obj5, obj6, obj7, obj8, obj9, obj10, obj11, obj12, obj14, obj15, obj16, obj17, obj18, obj19, obj20, obj21, obj22, obj23, obj24, obj25, obj26, obj27, obj28, obj29, obj30, obj31]

o5 = Object(220, 15, 0, 100, objects_color)
o6 = Object(200, 15, 780, 100, objects_color)
o7 = Object(425, 25, 285, 225, objects_color)
o8 = Object(300, 25, 0, 325, objects_color)
o9 = Object(300, 25, 700, 325, objects_color)
o10 = Object(300, 100, 250, 420, objects_color)
o11 = Object(60, 100, 718, 450, objects_color)
o12 = Object(90, 15, 590, 430, objects_color)
o13 = Object(50, 30, 400, 200, objects_color)
o14 = Object(50, 30, 535, 200, objects_color)

objects3 = [o1, o2, o3, o4, o5, o6, o7, o8, o9, o10, o11, o12, o13, o14]

OBJ5 = Object(200, 100, 400, 400, objects_color)
OBJ6 = Object(2000, 15, 600, 300, objects_color)
OBJ7 = Object(400, 15, 0, 300, objects_color)
OBJ8 = Object(300, 15, 350, 220, objects_color)
OBJ9 = Object(15, 140, 350, 95, objects_color)
OBJ10 = Object(15, 235, 635, 0, objects_color)
OBJ11 = Object(300, 15, 150, 90, objects_color)
OBJ12 = Object(315, 15, 550, 90, objects_color)
OBJ13 = Object(15, 150, 150, 90, objects_color)
OBJ14 = Object(15, 135, 850, 105, objects_color)
OBJ15 = Object(140, 15, 95, 225, objects_color)
OBJ16 = Object(140, 15, 780, 225, objects_color)
OBJ17 = Object(98, 15, 0, 150, objects_color)
OBJ18 = Object(70, 15, 915, 150, objects_color)
OBJ19 = Object(15, 30, 101, 480, objects_color)
OBJ20 = Object(15, 30, 285, 480, objects_color)
OBJ21 = Object(15, 30, 701, 480, objects_color)
OBJ22 = Object(15, 30, 885, 480, objects_color)
OBJ23 = Object(110, 15, 145, 420, objects_color)
OBJ24 = Object(109, 15, 745, 420, objects_color)

objects2 = [o1, o2, o3, o4, OBJ5, OBJ6, OBJ7, OBJ8, OBJ9, OBJ10, OBJ11, OBJ12, OBJ13, OBJ14, OBJ15, OBJ16, OBJ17, OBJ18, OBJ19, OBJ20, OBJ21, OBJ22, OBJ23, OBJ24]

ob1 = Object(590, 40, 210, 180, objects_color)
ob2 = Object(410, 40, 300, 360, objects_color)
ob3 = Object(118, 100, 441, 450, objects_color)
ob4 = Object(80, 15, 80, 280, objects_color)
ob5 = Object(80, 15, 140, 400, objects_color)
ob6 = Object(80, 15, 850, 280, objects_color)
ob7 = Object(80, 15, 790, 400, objects_color)

objects1 = [o1, o2, o3, o4, ob1, ob2, ob3, ob4, ob5, ob6, ob7]

name = ""
level = [1]
stars = [0]
phNum = ""

size = (700,150)
sizel = (700,160)
wq1 = pygame.transform.scale(pygame.image.load("Images/wq1.png"), size)
wq2 = pygame.transform.scale(pygame.image.load("Images/wq2.png"), size)
wq3 = pygame.transform.scale(pygame.image.load("Images/wq3.png"), size)
wq4 = pygame.transform.scale(pygame.image.load("Images/wq4.png"), size)
wq5 = pygame.transform.scale(pygame.image.load("Images/wq5.png"), size)
wq6 = pygame.transform.scale(pygame.image.load("Images/wq6.png"), size)
wq7 = pygame.transform.scale(pygame.image.load("Images/wq7.png"), size)
wq8 = pygame.transform.scale(pygame.image.load("Images/wq8.png"), size)
wq9 = pygame.transform.scale(pygame.image.load("Images/wq9.png"), size)
wq10 = pygame.transform.scale(pygame.image.load("Images/wq10.png"), size)
wq11 = pygame.transform.scale(pygame.image.load("Images/wq11.png"), size)
wq12 = pygame.transform.scale(pygame.image.load("Images/wq12.png"), size)
wq13 = pygame.transform.scale(pygame.image.load("Images/wq13.png"), size)
wq14 = pygame.transform.scale(pygame.image.load("Images/wq14.png"), size)
wq15 = pygame.transform.scale(pygame.image.load("Images/wq15.png"), size)


lq1 = pygame.transform.scale(pygame.image.load("Images/lq1.png"), sizel)
lq2 = pygame.transform.scale(pygame.image.load("Images/lq2.png"), sizel)
lq3 = pygame.transform.scale(pygame.image.load("Images/lq3.png"), sizel)
lq4 = pygame.transform.scale(pygame.image.load("Images/lq4.png"), sizel)
lq5 = pygame.transform.scale(pygame.image.load("Images/lq5.png"), sizel)
lq6 = pygame.transform.scale(pygame.image.load("Images/lq6.png"), sizel)
lq7 = pygame.transform.scale(pygame.image.load("Images/lq7.png"), sizel)
lq8 = pygame.transform.scale(pygame.image.load("Images/lq8.png"), sizel)
lq9 = pygame.transform.scale(pygame.image.load("Images/lq9.png"), sizel)
lq10 = pygame.transform.scale(pygame.image.load("Images/lq10.png"), sizel)
lq11 = pygame.transform.scale(pygame.image.load("Images/lq11.png"), sizel)
lq12 = pygame.transform.scale(pygame.image.load("Images/lq12.png"), sizel)
lq13 = pygame.transform.scale(pygame.image.load("Images/lq13.png"), sizel)
lq14 = pygame.transform.scale(pygame.image.load("Images/lq14.png"), sizel)
lq15 = pygame.transform.scale(pygame.image.load("Images/lq15.png"), sizel)
lq16 = pygame.transform.scale(pygame.image.load("Images/lq16.png"), sizel)
lq17 = pygame.transform.scale(pygame.image.load("Images/lq17.png"), sizel)
lq18 = pygame.transform.scale(pygame.image.load("Images/lq18.png"), sizel)
lq19 = pygame.transform.scale(pygame.image.load("Images/lq19.png"), sizel)
lq20 = pygame.transform.scale(pygame.image.load("Images/lq20.png"), sizel)
lq21 = pygame.transform.scale(pygame.image.load("Images/lq21.png"), sizel)
lq22 = pygame.transform.scale(pygame.image.load("Images/lq22.png"), sizel)
lq23 = pygame.transform.scale(pygame.image.load("Images/lq23.png"), sizel)
lq24 = pygame.transform.scale(pygame.image.load("Images/lq24.png"), sizel)
lq25 = pygame.transform.scale(pygame.image.load("Images/lq25.png"), sizel)
lq26 = pygame.transform.scale(pygame.image.load("Images/lq26.png"), sizel)
win_quotes = [wq1, wq2, wq3, wq4, wq5, wq6, wq7, wq8, wq9, wq10, wq11, wq12, wq13, wq14, wq15]
lose_quotes = [lq1, lq2, lq3, lq4, lq5, lq6, lq7, lq8, lq9, lq10, lq11, lq12, lq13, lq14, lq15, lq16, lq17, lq18, lq19, lq20, lq21, lq22, lq23, lq24, lq25, lq26]


def middle(red, blue, pink, purple, RED, BLUE, PINK, PURPLE,t,tmax,diamonds):
    big_boy = None
    big_girl = None
    if not red: big_girl = pygame.transform.scale(pygame.image.load("Images/Redgirl.png"), (140, 220))
    if not blue: big_girl = pygame.transform.scale(pygame.image.load("Images/Bluegirl.png"), (140, 220))
    if not pink:big_girl = pygame.transform.scale(pygame.image.load("Images/Pinkgirl.png"), (140, 220))
    if not purple: big_girl = pygame.transform.scale(pygame.image.load("Images/Purplegirl.png"), (140, 220))

    if not RED: big_boy = pygame.transform.scale(pygame.image.load("Images/Redboy.png"), (135, 225))
    if not BLUE: big_boy = pygame.transform.scale(pygame.image.load("Images/Blueboy.png"), (135, 225))
    if not PINK: big_boy = pygame.transform.scale(pygame.image.load("Images/Pinkboy.png"), (135, 225))
    if not PURPLE: big_boy = pygame.transform.scale(pygame.image.load("Images/Purpleboy.png"), (135, 225))

    start_run = True

    star1 = Star("Images/Star.png", 120, (300, 140),2)
    star2 = Star("Images/Star.png", 160, (420,115),2.5)
    star3 = Star("Images/Star.png", 120, (590, 140),2)

    Background = pygame.transform.scale(pygame.image.load("Images/winbackground.png"), screen_size)
    play_button = pygame.transform.scale(pygame.image.load("Images/PlayButton!!!.png"), (75, 75))
    play_button = Button(play_button, (460, 290), 75, 75)
    home_button = pygame.transform.scale(pygame.image.load("Images/home.png"), (55, 55))
    home_button = Button(home_button, (473, 370), 55, 55)
    gem = pygame.transform.scale(pygame.image.load("Images/diamond-icon.jpg"), (58, 58))
    stoper = pygame.transform.scale(pygame.image.load("Images/clock.png"), (55, 55))
    didgem = pygame.transform.scale(pygame.image.load("Images/X.png"), (50, 50))
    didstoper = pygame.transform.scale(pygame.image.load("Images/X.png"), (50, 50))
    retry_button = pygame.transform.scale(pygame.image.load("Images/retry-icon-9.jpg"), (50, 50))
    retry_button = Button(retry_button, (475, 435), 50, 50)
    s = 1
    if len(diamonds) == 0:
        s += 1
        didgem = pygame.transform.scale(pygame.image.load("Images/V.png"), (60, 55))
    if t <= tmax:
        s += 1
        didstoper = pygame.transform.scale(pygame.image.load("Images/V.png"), (60, 55))
    stars[0] = stars[0] + s
    with open(name + ".txt", 'w', encoding='utf-8') as f:
        f.write(str(level[0]) + "\n")
        f.write(str(stars[0]) + "\n")
    x = random.randint(0, len(win_quotes) - 1)
    while start_run:
        screen.blit(Background, (0, 0))
        screen.blit(big_girl, (150, 270))
        screen.blit(big_boy, (700, 270))
        screen.blit(gem, (60, 120))
        screen.blit(stoper, (60, 185))
        screen.blit(didgem, (130, 120))
        screen.blit(didstoper, (130, 185))
        screen.blit(win_quotes[x], (150, 0))
        play_button.display_button()
        home_button.display_button()
        retry_button.display_button()

        if s == 1:
            star1.display_star(True)
        if s == 2:
            star2.display_star(star1.display_star(True))
        if s == 3:
            a = star1.display_star(True)
            b = star2.display_star(a)
            star3.display_star(b and a)

        pygame.display.flip()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_in_button(play_button, event.pos):
                    start_run = False
                if mouse_in_button(home_button, event.pos):
                    start_run = False
                    home()
                if mouse_in_button(retry_button, event.pos):
                    start_run = False
                    level[0] = level[0] - 1
                    stars[0] = stars[0] - s
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    print(win_quotes[x])
    win_quotes.remove(win_quotes[x])


def level4(red, blue, pink, purple, RED, BLUE, PINK, PURPLE):
    global sound_on
    tmax = 120
    black = (0, 0, 0)
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
    green_lava5 = Lava("Images/green lava.PNG", "green", (610, 265))
    green_lava6 = Lava("Images/green lava.PNG", "green", (695, 265))
    B = False
    retry = True
    while run:
        if retry:
            if sound_on:
                play_music("Sounds/backgroundSoundtrack2.ogg")
            if not red:
                y = create_images_list("Images/Redgirl.png", "Images/RedGRun.PNG", "Images/RedGRunLeft.PNG")
                girl = Character((35, 450), "red", y)
                girl_lava1 = Lava("Images/red lava.PNG", "red", (95, 500))
                girl_door = Door("Images/DoorGirlRed.png", "red", (30, 30))

                girl_diamond1 = Diamond("Images/DRed!.png", "red", (741, 405))
                girl_diamond2 = Diamond("Images/DRed!.png", "red", (930, 250))
                girl_diamond3 = Diamond("Images/DRed!.png", "red", (125, 200))
                girl_diamond4 = Diamond("Images/DRed!.png", "red", (440, 170))
                girl_diamond5 = Diamond("Images/DRed!.png", "red", (650, 60))
            if not blue:
                y = create_images_list("Images/Bluegirl.png", "Images/BlueGRun.PNG", "Images/BlueGRunLeft.PNG")
                girl = Character((35, 450), "blue", y)
                girl_lava1 = Lava("Images/blue lava.PNG", "blue", (95, 500))
                girl_door = Door("Images/DoorGirlBlue.png", "blue", (30, 30))

                girl_diamond1 = Diamond("Images/DBlue.png", "blue", (741, 405))
                girl_diamond2 = Diamond("Images/DBlue.png", "blue", (930, 250))
                girl_diamond3 = Diamond("Images/DBlue.png", "blue", (125, 200))
                girl_diamond4 = Diamond("Images/DBlue.png", "blue", (440, 170))
                girl_diamond5 = Diamond("Images/DBlue.png", "blue", (650, 60))
            if not pink:
                y = create_images_list("Images/Pinkgirl.png", "Images/PinkGRun.PNG", "Images/PinkGRunLeft.PNG")
                girl = Character((35, 450), "pink", y)
                girl_lava1 = Lava("Images/pink lava.PNG", "pink", (95, 500))
                girl_door = Door("Images/DoorGirlPink.png", "pink", (30, 30))

                girl_diamond1 = Diamond("Images/DPink.png", "pink", (741, 405))
                girl_diamond2 = Diamond("Images/DPink.png", "pink", (930, 250))
                girl_diamond3 = Diamond("Images/DPink.png", "pink", (125, 200))
                girl_diamond4 = Diamond("Images/DPink.png", "pink", (440, 170))
                girl_diamond5 = Diamond("Images/DPink.png", "pink", (650, 60))
            if not purple:
                y = create_images_list("Images/Purplegirl.png", "Images/PurpleGRun.PNG", "Images/PurpleGRunLeft.PNG")
                girl = Character((35, 450), "purple", y)
                girl_lava1 = Lava("Images/purple lava.PNG", "purple", (95, 500))
                girl_door = Door("Images/DoorGirlPurple.png", "purple", (30, 30))

                girl_diamond1 = Diamond("Images/DPurple.png", "purple", (741, 405))
                girl_diamond2 = Diamond("Images/DPurple.png", "purple", (930, 250))
                girl_diamond3 = Diamond("Images/DPurple.png", "purple", (125, 200))
                girl_diamond4 = Diamond("Images/DPurple.png", "purple", (440, 170))
                girl_diamond5 = Diamond("Images/DPurple.png", "purple", (650, 60))

            if not RED:
                x = create_images_list("Images/Redboy.png", "Images/RedBRun.PNG", "Images/RedBRunLeft.PNG")
                boy = Character((920, 450), "red", x)
                boy_lava1 = Lava("Images/red lava.PNG", "red", (819, 500))
                boy_door = Door("Images/DoorBoyRed.png", "red", (800, 30))

                boy_diamond1 = Diamond("Images/DRed!.png", "red", (225, 405))
                boy_diamond2 = Diamond("Images/DRed!.png", "red", (475, 320))
                boy_diamond3 = Diamond("Images/DRed!.png", "red", (160, 200))
                boy_diamond4 = Diamond("Images/DRed!.png", "red", (895, 250))
                boy_diamond5 = Diamond("Images/DRed!.png", "red", (150, 60))
            if not BLUE:
                x = create_images_list("Images/Blueboy.png", "Images/BlueBRun.PNG", "Images/BlueBRunLeft.PNG")
                boy = Character((920, 450), "blue", x)
                boy_lava1 = Lava("Images/blue lava.PNG", "blue", (819, 500))
                boy_door = Door("Images/DoorBoyBlue.png", "blue", (800, 30))

                boy_diamond1 = Diamond("Images/DBlue.png", "blue", (225, 405))
                boy_diamond2 = Diamond("Images/DBlue.png", "blue", (475, 320))
                boy_diamond3 = Diamond("Images/DBlue.png", "blue", (160, 200))
                boy_diamond4 = Diamond("Images/DBlue.png", "blue", (895, 250))
                boy_diamond5 = Diamond("Images/DBlue.png", "blue", (150, 60))
            if not PINK:
                x = create_images_list("Images/Pinkboy.png", "Images/PinkBRun.PNG", "Images/PinkBRunLeft.PNG")
                boy = Character((920, 450), "pink", x)
                boy_lava1 = Lava("Images/pink lava.PNG", "pink", (819, 500))
                boy_door = Door("Images/DoorBoyPink.png", "pink", (800, 30))

                boy_diamond1 = Diamond("Images/DPink.png", "pink", (225, 405))
                boy_diamond2 = Diamond("Images/DPink.png", "pink", (475, 320))
                boy_diamond3 = Diamond("Images/DPink.png", "pink", (160, 200))
                boy_diamond4 = Diamond("Images/DPink.png", "pink", (895, 250))
                boy_diamond5 = Diamond("Images/DPink.png", "pink", (150, 60))
            if not PURPLE:
                x = create_images_list("Images/Purpleboy.png", "Images/PurpleBRun.PNG", "Images/PurpleBRunLeft.PNG")
                boy = Character((920, 450), "purple", x)
                boy_lava1 = Lava("Images/purple lava.PNG", "purple", (819, 500))
                boy_door = Door("Images/DoorBoyPurple.png", "purple", (800, 30))

                boy_diamond1 = Diamond("Images/DPurple.png", "purple", (225, 405))
                boy_diamond2 = Diamond("Images/DPurple.png", "purple", (475, 320))
                boy_diamond3 = Diamond("Images/DPurple.png", "purple", (160, 200))
                boy_diamond4 = Diamond("Images/DPurple.png", "purple", (895, 250))
                boy_diamond5 = Diamond("Images/DPurple.png", "purple", (150, 60))

        b1 = Magic_Button("Images/BBlue.PNG","blue",(26,240))
        b2 = Magic_Button("Images/‏‏BGreenOP.PNG","green", (953, 225))
        magic_buttons = [b1, b2]
        w1 = Wall("Images/WBlue.PNG", "blue", 100, 20, (693, 295))
        w2 = Wall("Images/WGreen.PNG", "green", 66, 20, (100, 24))
        walls = [w1, w2]
        doors = [boy_door, girl_door]
        lavas = [green_lava1, green_lava2, green_lava3, green_lava4, green_lava5, boy_lava1, girl_lava1, green_lava1,green_lava6]
        diamonds = [girl_diamond1, girl_diamond2, girl_diamond3, girl_diamond4, girl_diamond5, boy_diamond1, boy_diamond2, boy_diamond3, boy_diamond4, boy_diamond5]
        t0 = time.time()
        savewall = None
        while boy.alive and girl.alive and run:  # Caharater1 is alive and Caracter2 is alive and Bool:
            retry = False
            screen.blit(background, (0, 0))
            for obstacle in objects4:
                obstacle.display_obstacle()
            for door in doors:
                door.display_door()
            for wall in walls:
                wall.display_wall()
            for b in magic_buttons:
                b.display_magic_button()
                if not b.pressed:
                    if b.press(boy) or b.press(girl):
                        for w in walls:
                            if w.color == b.color:
                                savewall = w
                                walls.remove(w)
                else:
                    if not b.press(boy) and not b.press(girl):
                        if savewall:
                            if savewall.able_to_display(boy,girl):
                                walls.append(savewall)
                                b.pressed = False
                                savewall = None

            screen.blit(timer,(460,10))
            font = pygame.font.SysFont("Calibri Regular.ttf", 35)
            if int(time.time() - t0) < 10:
                screen.blit(font.render(str(int(time.time() - t0)), True, black),(480,30))
            else:
                screen.blit(font.render(str(int(time.time() - t0)), True, black), (475, 30))

            for diamond in diamonds:
                gem = diamond.collect(boy) and diamond.collect(girl)
                if gem:
                    diamond.display_diamond()
                else:
                    diamonds.remove(diamond)
            girl.display_character(objects4, lavas, walls)
            boy.display_character(objects4, lavas, walls)
            if boy.door(doors) and girl.door(doors):
                run = False
            for lava in lavas:
                lava.display_lava()
            if sound_on:
                sound_button.display_button()
            else:
                no_sound_button.display_button()

            # refreshing screen:
            pygame.display.flip()
            pygame.display.update()
            clock.tick(150)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if sound_on:
                        if mouse_in_button(sound_button, event.pos):
                            pygame.mixer.stop()
                            sound_on = False
                    else:
                        if mouse_in_button(no_sound_button, event.pos):
                            play_music("Sounds/backgroundSoundtrack2.ogg")
                            sound_on = True
                    print(mouse_pos)
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

                    if event.key == pygame.K_r:
                        girl.alive = False
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
            if len(lose_quotes) > 0:
                x = random.randint(0, len(lose_quotes) - 1)
        if run:
            retry_button = pygame.transform.scale(pygame.image.load("Images/retry-icon-9.jpg"), (100, 100))
            retry_button = Button(retry_button,(450,200),100,100)
            home_button = pygame.transform.scale(pygame.image.load("Images/home.png"),(65,65))
            home_button = Button(home_button,(468,310),65,65)
            screen.blit(background, (0, 0))
            retry_button.display_button()
            home_button.display_button()
            if len(lose_quotes) != 0:
                screen.blit(lose_quotes[x], (150, 20))
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
                        home()
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
    pygame.mixer.stop()
    win_sound()
    t = time.time() - t0
    print(t)
    level[0] = level[0] + 1
    middle(red,blue,pink,purple,RED,BLUE,PINK,PURPLE,t,tmax,diamonds)


def level3(red, blue, pink, purple, RED, BLUE, PINK, PURPLE):
    global sound_on
    tmax = 35
    black = (0, 0, 0)
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
    savewall = None
    green_lava1 = Lava("Images/green lava.PNG", "green", (450, 205))
    green_lava2 = Lava("Images/green lava.PNG", "green", (550, 485))
    green_lava3 = Lava("Images/green lava.PNG", "green", (634, 485))
    B = False
    retry = True
    while run:
        if retry:
            if sound_on:
                play_music("Sounds/backgroundSoundtrack2.ogg")
            if not red:
                y = create_images_list("Images/Redgirl.png", "Images/RedGRun.PNG", "Images/RedGRunLeft.PNG")
                girl = Character((30, 60), "red", y)
                girl_door = Door("Images/DoorGirlRed.png", "red", (30, 440))

                girl_diamond1 = Diamond("Images/DRed!.png", "red", (860, 70))
                girl_diamond2 = Diamond("Images/DRed!.png", "red", (860, 295))
                girl_diamond3 = Diamond("Images/DRed!.png", "red", (860, 470))
            if not blue:
                y = create_images_list("Images/Bluegirl.png", "Images/BlueGRun.PNG", "Images/BlueGRunLeft.PNG")
                girl = Character((30, 60), "blue", y)
                girl_door = Door("Images/DoorGirlBlue.png", "blue", (30, 440))

                girl_diamond1 = Diamond("Images/DBlue.png", "blue", (860, 70))
                girl_diamond2 = Diamond("Images/DBlue.png", "blue", (860, 295))
                girl_diamond3 = Diamond("Images/DBlue.png", "blue", (860, 470))
            if not pink:
                y = create_images_list("Images/Pinkgirl.png", "Images/PinkGRun.PNG", "Images/PinkGRunLeft.PNG")
                girl = Character((30, 60), "pink", y)
                girl_door = Door("Images/DoorGirlPink.png", "pink", (30, 440))

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
                boy_door = Door("Images/DoorBoyRed.png", "red", (90, 440))

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

            w1 = Wall("Images/WRed.PNG","red",70,20,(250,350))
            walls = [w1]

            b1 = Magic_Button("Images/‏‏BRedOP.PNG", "red", (230, 450))
            b2 = Magic_Button("Images/‏‏BRedOP.PNG", "red", (960, 450))
            magic_buttons = [b1,b2]

            doors = [boy_door, girl_door]
            lavas = [green_lava1, green_lava2, green_lava3]
            diamonds = [boy_diamond1, boy_diamond2, boy_diamond3, girl_diamond1, girl_diamond2, girl_diamond3]
            t0 = time.time()
            while boy.alive and girl.alive and run:  # Caharater1 is alive and Caracter2 is alive and Bool:
                retry = False
                screen.blit(background, (0, 0))
                for obstacle in objects3:
                    obstacle.display_obstacle()
                for door in doors:
                    door.display_door()
                for wall in walls:
                    wall.display_wall()
                for b in magic_buttons:
                    b.display_magic_button()
                    if not b.pressed:
                        if b.press(boy) or b.press(girl):
                            for w in walls:
                                if w.color == b.color:
                                    savewall = w
                                    walls.remove(w)
                    else:
                        if not b.press(boy) and not b.press(girl):
                            if savewall:
                                if savewall.able_to_display(boy, girl):
                                    walls.append(savewall)
                                    magic_buttons[0].pressed = False
                                    magic_buttons[1].pressed = False
                                    savewall = None
                for diamond in diamonds:
                    gem = diamond.collect(boy) and diamond.collect(girl)
                    if gem:
                        diamond.display_diamond()
                    else:
                        diamonds.remove(diamond)
                girl.display_character(objects3, lavas, walls)
                boy.display_character(objects3, lavas, walls)
                if boy.door(doors) and girl.door(doors):
                    run = False
                for lava in lavas:
                    lava.display_lava()
                if sound_on:
                    sound_button.display_button()
                else:
                    no_sound_button.display_button()

                screen.blit(timer, (460, 10))
                font = pygame.font.SysFont("Calibri Regular.ttf", 35)
                if int(time.time() - t0) < 10:
                    screen.blit(font.render(str(int(time.time() - t0)), True, black), (480, 30))
                else:
                    screen.blit(font.render(str(int(time.time() - t0)), True, black), (475, 30))
                # refreshing screen:
                pygame.display.flip()
                pygame.display.update()
                clock.tick(150)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos
                        if sound_on:
                            if mouse_in_button(sound_button, event.pos):
                                pygame.mixer.stop()
                                sound_on = False
                        else:
                            if mouse_in_button(no_sound_button, event.pos):
                                play_music("Sounds/backgroundSoundtrack2.ogg")
                                sound_on = True
                        print(mouse_pos)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            boy.move_right()
                        if event.key == pygame.K_LEFT:
                            boy.move_left()
                        if event.key == pygame.K_UP:
                            boy.start_jump()

                        if event.key == pygame.K_r:
                            girl.alive = False

                        if event.key == pygame.K_d:
                            girl.move_right()
                        if event.key == pygame.K_a:
                            girl.move_left()
                        if event.key == pygame.K_w:
                            girl.start_jump()
                        if event.key == pygame.K_r:
                            girl.alive = False
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
            if len(lose_quotes) > 0:
                x = random.randint(0, len(lose_quotes) - 1)
        if run:
            retry_button = pygame.transform.scale(pygame.image.load("Images/retry-icon-9.jpg"), (100, 100))
            retry_button = Button(retry_button,(450,200),100,100)
            home_button = pygame.transform.scale(pygame.image.load("Images/home.png"),(65,65))
            home_button = Button(home_button,(468,310),65,65)
            screen.blit(background, (0, 0))
            retry_button.display_button()
            home_button.display_button()
            if len(lose_quotes) != 0:
                screen.blit(lose_quotes[x], (150, 20))

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
                        home()
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
    pygame.mixer.stop()
    win_sound()
    t = time.time() - t0
    print(t)
    level[0] = level[0] + 1
    middle(red,blue,pink,purple,RED,BLUE,PINK,PURPLE,t,tmax,diamonds)


def level2(red, blue, pink, purple, RED, BLUE, PINK, PURPLE):
    global sound_on
    tmax = 35
    black = (0, 0, 0)
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

    B = False
    retry = True
    while run:
        if retry:
            if sound_on:
                play_music("Sounds/backgroundSoundtrack2.ogg")
            if not red:
                y = create_images_list("Images/Redgirl.png", "Images/RedGRun.PNG", "Images/RedGRunLeft.PNG")
                girl = Character((540, 340), "red", y)
                girl_lava1 = Lava("Images/red lava.PNG", "red", (800, 485))
                girl_lava2 = Lava("Images/red lava.PNG", "red", (716, 485))

                girl_door = Door("Images/DoorGirlRed.png", "red", (375, 160))

                girl_diamond1 = Diamond("Images/DRed!.png", "red", (355, 465))
                girl_diamond2 = Diamond("Images/DRed!.png", "red", (200, 55))
                girl_diamond3 = Diamond("Images/DRed!.png", "red", (550, 55))
                girl_diamond4 = Diamond("Images/DRed!.png", "red", (175, 190))
                girl_diamond5 = Diamond("Images/DRed!.png", "red", (45, 465))
            if not blue:
                y = create_images_list("Images/Bluegirl.png", "Images/BlueGRun.PNG", "Images/BlueGRunLeft.PNG")
                girl = Character((540, 340), "blue", y)
                girl_lava1 = Lava("Images/blue lava.PNG", "blue", (800, 485))
                girl_lava2 = Lava("Images/blue lava.PNG", "blue", (716, 485))

                girl_door = Door("Images/DoorGirlBlue.png", "blue", (375, 160))

                girl_diamond1 = Diamond("Images/DBlue.png", "blue", (355, 465))
                girl_diamond2 = Diamond("Images/DBlue.png", "blue", (200, 55))
                girl_diamond3 = Diamond("Images/DBlue.png", "blue", (550, 55))
                girl_diamond4 = Diamond("Images/DBlue.png", "blue", (175, 190))
                girl_diamond5 = Diamond("Images/DBlue.png", "blue", (45, 465))
            if not pink:
                y = create_images_list("Images/Pinkgirl.png", "Images/PinkGRun.PNG", "Images/PinkGRunLeft.PNG")
                girl = Character((540, 340), "pink", y)
                girl_lava1 = Lava("Images/pink lava.PNG", "pink", (800, 485))
                girl_lava2 = Lava("Images/pink lava.PNG", "pink", (716, 485))

                girl_door = Door("Images/DoorGirlPink.png", "pink", (375, 160))

                girl_diamond1 = Diamond("Images/DPink.png", "pink", (355, 465))
                girl_diamond2 = Diamond("Images/DPink.png", "pink", (200, 55))
                girl_diamond3 = Diamond("Images/DPink.png", "pink", (550, 55))
                girl_diamond4 = Diamond("Images/DPink.png", "pink", (175, 190))
                girl_diamond5 = Diamond("Images/DPink.png", "pink", (45, 465))
            if not purple:
                y = create_images_list("Images/Purplegirl.png", "Images/PurpleGRun.PNG", "Images/PurpleGRunLeft.PNG")
                girl = Character((540, 340), "purple", y)
                girl_lava1 = Lava("Images/purple lava.PNG", "purple", (800, 485))
                girl_lava2 = Lava("Images/purple lava.PNG", "purple", (716, 485))

                girl_door = Door("Images/DoorGirlPurple.png", "purple", (375, 160))

                girl_diamond1 = Diamond("Images/DPurple.png", "purple", (355, 465))
                girl_diamond2 = Diamond("Images/DPurple.png", "purple", (200, 55))
                girl_diamond3 = Diamond("Images/DPurple.png", "purple", (550, 55))
                girl_diamond4 = Diamond("Images/DPurple.png", "purple", (175, 190))
                girl_diamond5 = Diamond("Images/DPurple.png", "purple", (45, 465))
            if not RED:
                x = create_images_list("Images/Redboy.png", "Images/RedBRun.PNG", "Images/RedBRunLeft.PNG")
                boy = Character((441, 340), "red", x)
                boy_lava1 = Lava("Images/red lava.PNG", "red", (200, 485))
                boy_lava2 = Lava("Images/red lava.PNG", "red", (116, 485))

                boy_door = Door("Images/DoorBoyRed.png", "red", (568, 160))

                boy_diamond1 = Diamond("Images/DRed!.png", "red", (615, 465))
                boy_diamond2 = Diamond("Images/DRed!.png", "red", (780, 55))
                boy_diamond3 = Diamond("Images/DRed!.png", "red", (425, 55))
                boy_diamond4 = Diamond("Images/DRed!.png", "red", (810, 190))
                boy_diamond5 = Diamond("Images/DRed!.png", "red", (930, 465))
            if not BLUE:
                x = create_images_list("Images/Blueboy.png", "Images/BlueBRun.PNG", "Images/BlueBRunLeft.PNG")
                boy = Character((441, 340), "blue", x)
                boy_lava1 = Lava("Images/blue lava.PNG", "blue", (200, 485))
                boy_lava2 = Lava("Images/blue lava.PNG", "blue", (116, 485))

                boy_door = Door("Images/DoorBoyBlue.png", "blue", (568, 160))

                boy_diamond1 = Diamond("Images/DBlue.png", "blue", (615, 465))
                boy_diamond2 = Diamond("Images/DBlue.png", "blue", (780, 55))
                boy_diamond3 = Diamond("Images/DBlue.png", "blue", (425, 55))
                boy_diamond4 = Diamond("Images/DBlue.png", "blue", (810, 190))
                boy_diamond5 = Diamond("Images/DBlue.png", "blue", (930, 465))
            if not PINK:
                x = create_images_list("Images/Pinkboy.png", "Images/PinkBRun.PNG", "Images/PinkBRunLeft.PNG")
                boy = Character((441, 340), "pink", x)
                boy_lava1 = Lava("Images/pink lava.PNG", "pink", (200, 485))
                boy_lava2 = Lava("Images/pink lava.PNG", "pink", (116, 485))

                boy_door = Door("Images/DoorBoyPink.png", "pink", (568, 160))

                boy_diamond1 = Diamond("Images/DPink.png", "pink", (615, 465))
                boy_diamond2 = Diamond("Images/DPink.png", "pink", (780, 55))
                boy_diamond3 = Diamond("Images/DPink.png", "pink", (425, 55))
                boy_diamond4 = Diamond("Images/DPink.png", "pink", (810, 190))
                boy_diamond5 = Diamond("Images/DPink.png", "pink", (930, 465))
            if not PURPLE:
                x = create_images_list("Images/Purpleboy.png", "Images/PurpleBRun.PNG", "Images/PurpleBRunLeft.PNG")
                boy = Character((441, 340), "purple", x)
                boy_lava1 = Lava("Images/purple lava.PNG", "purple", (200, 485))
                boy_lava2 = Lava("Images/purple lava.PNG", "purple", (116, 485))

                boy_door = Door("Images/DoorBoyPurple.png", "purple", (568, 160))

                boy_diamond1 = Diamond("Images/DPurple.png", "purple", (615, 465))
                boy_diamond2 = Diamond("Images/DPurple.png", "purple", (780, 55))
                boy_diamond3 = Diamond("Images/DPurple.png", "purple", (425, 55))
                boy_diamond4 = Diamond("Images/DPurple.png", "purple", (810, 190))
                boy_diamond5 = Diamond("Images/DPurple.png", "purple", (930, 465))

        por1 = Portal("Images/p1.png","Images/p2.png","Images/p3.png","Images/p4.png","Images/p5.png",(590,25))
        por2 = Portal("Images/‏‏p1 - right.png","Images/‏‏p2 - right.png","Images/‏‏p3 - right.png","Images/‏‏p4 - right.png","Images/‏‏p5 - right.png",(660,25))

        b1 = Magic_Button("Images/BYellowDown.PNG", "yellow", (480, 200))
        w1 = Wall("Images/WYellow.PNG", "yellow", 65, 20, (350, 25))
        walls = [w1]
        magic_buttons = [b1]
        doors = [boy_door, girl_door]
        lavas = [girl_lava1, boy_lava1, girl_lava2, boy_lava2]
        diamonds = [girl_diamond1, boy_diamond1, girl_diamond2, boy_diamond2, girl_diamond3, boy_diamond3, girl_diamond4, boy_diamond4, girl_diamond5, boy_diamond5]
        t0 = time.time()
        savewall = None
        while boy.alive and girl.alive and run:  # Caharater1 is alive and Caracter2 is alive and Bool:
            retry = False
            screen.blit(background, (0, 0))
            for obstacle in objects2:
                obstacle.display_obstacle()
            for door in doors:
                door.display_door()
            if len(walls) != 0:
                for wall in walls:
                    wall.display_wall()

            for b in magic_buttons:
                b.display_magic_button()
                if not b.pressed:
                    if b.press(boy) or b.press(girl):
                        for w in walls:
                            if w.color == b.color:
                                savewall = w
                                walls.remove(w)
                else:
                    if not b.press(boy) and not b.press(girl):
                        if savewall:
                            if savewall.able_to_display(boy,girl):
                                walls.append(savewall)
                                b.pressed = False
                                savewall = None

            for diamond in diamonds:
                gem = diamond.collect(boy) and diamond.collect(girl)
                if gem:
                    diamond.display_diamond()
                else:
                    diamonds.remove(diamond)
            girl.display_character(objects2, lavas, walls)
            boy.display_character(objects2, lavas, walls)
            if boy.door(doors) and girl.door(doors):
                run = False
            for lava in lavas:
                lava.display_lava()
            if sound_on:
                sound_button.display_button()
            else:
                no_sound_button.display_button()
            por1.display_portal(boy,girl,(690,40))
            por2.display_portal(boy,girl,(560,40))

            screen.blit(timer,(460,10))
            font = pygame.font.SysFont("Calibri Regular.ttf", 35)
            if int(time.time() - t0) < 10:
                screen.blit(font.render(str(int(time.time() - t0)), True, black),(480,30))
            else:
                screen.blit(font.render(str(int(time.time() - t0)), True, black), (475, 30))
            # refreshing screen:
            pygame.display.flip()
            pygame.display.update()
            clock.tick(150)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if sound_on:
                        if mouse_in_button(sound_button, event.pos):
                            pygame.mixer.stop()
                            sound_on = False
                    else:
                        if mouse_in_button(no_sound_button, event.pos):
                            play_music("Sounds/backgroundSoundtrack2.ogg")
                            sound_on = True
                    print(mouse_pos)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        boy.move_right()
                    if event.key == pygame.K_LEFT:
                        boy.move_left()
                    if event.key == pygame.K_UP:
                        boy.start_jump()
                    if event.key == pygame.K_r:
                        girl.alive = False

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
            if len(lose_quotes) > 0:
                x = random.randint(0, len(lose_quotes) - 1)
        if run:
            retry_button = pygame.transform.scale(pygame.image.load("Images/retry-icon-9.jpg"), (100, 100))
            retry_button = Button(retry_button, (450, 200), 100, 100)
            home_button = pygame.transform.scale(pygame.image.load("Images/home.png"), (65, 65))
            home_button = Button(home_button, (468, 310), 65, 65)
            screen.blit(background, (0, 0))
            retry_button.display_button()
            home_button.display_button()
            if len(lose_quotes) != 0:
                screen.blit(lose_quotes[x], (150, 20))
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
                    if mouse_in_button(home_button, mouse_pos):
                        run = False
                        home()
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
    pygame.mixer.stop()
    win_sound()
    t = time.time() - t0
    print(t)
    level[0] = level[0] + 1
    middle(red,blue,pink,purple,RED,BLUE,PINK,PURPLE,t,tmax,diamonds)


def level1(red, blue, pink, purple, RED, BLUE, PINK, PURPLE):
    global sound_on
    tmax = 35
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
    black = (0, 0, 0)

    B = False
    retry = True
    while run:
        if retry:
            if sound_on:
                play_music("Sounds/backgroundSoundtrack2.ogg")
            if not red:
                y = create_images_list("Images/Redgirl.png", "Images/RedGRun.PNG", "Images/RedGRunLeft.PNG")
                girl = Character((540, 340), "red", y)
                girl_lava1 = Lava("Images/red lava.PNG", "red", (20, 485))
                girl_lava2 = Lava("Images/red lava.PNG", "red", (104, 485))
                girl_lava3 = Lava("Images/red lava.PNG", "red", (188, 485))
                girl_lava4 = Lava("Images/red lava.PNG", "red", (272, 485))
                girl_lava5 = Lava("Images/red lava.PNG", "red", (356, 485))

                girl_door = Door("Images/DoorGirlRed.png", "red", (300, 120))

                girl_diamond1 = Diamond("Images/DRed!.png", "red", (40, 465))
                girl_diamond2 = Diamond("Images/DRed!.png", "red", (208, 465))
                girl_diamond3 = Diamond("Images/DRed!.png", "red", (376, 465))
                girl_diamond4 = Diamond("Images/DRed!.png", "red", (875, 250))
            if not blue:
                y = create_images_list("Images/Bluegirl.png", "Images/BlueGRun.PNG", "Images/BlueGRunLeft.PNG")
                girl = Character((540, 340), "blue", y)
                girl_lava1 = Lava("Images/blue lava.PNG", "blue", (20, 485))
                girl_lava2 = Lava("Images/blue lava.PNG", "blue", (104, 485))
                girl_lava3 = Lava("Images/blue lava.PNG", "blue", (188, 485))
                girl_lava4 = Lava("Images/blue lava.PNG", "blue", (272, 485))
                girl_lava5 = Lava("Images/blue lava.PNG", "blue", (356, 485))

                girl_door = Door("Images/DoorGirlBlue.png", "blue", (300, 120))

                girl_diamond1 = Diamond("Images/DBlue.png", "blue", (40, 465))
                girl_diamond2 = Diamond("Images/DBlue.png", "blue", (208, 465))
                girl_diamond3 = Diamond("Images/DBlue.png", "blue", (376, 465))
                girl_diamond4 = Diamond("Images/DBlue.png", "blue", (875, 250))
            if not pink:
                y = create_images_list("Images/Pinkgirl.png", "Images/PinkGRun.PNG", "Images/PinkGRunLeft.PNG")
                girl = Character((540, 340), "pink", y)
                girl_lava1 = Lava("Images/pink lava.PNG", "pink", (20, 485))
                girl_lava2 = Lava("Images/pink lava.PNG", "pink", (104, 485))
                girl_lava3 = Lava("Images/pink lava.PNG", "pink", (188, 485))
                girl_lava4 = Lava("Images/pink lava.PNG", "pink", (272, 485))
                girl_lava5 = Lava("Images/pink lava.PNG", "pink", (356, 485))

                girl_door = Door("Images/DoorGirlPink.png", "pink", (300, 120))

                girl_diamond1 = Diamond("Images/DPink.png", "pink", (40, 465))
                girl_diamond2 = Diamond("Images/DPink.png", "pink", (208, 465))
                girl_diamond3 = Diamond("Images/DPink.png", "pink", (376, 465))
                girl_diamond4 = Diamond("Images/DPink.png", "pink", (875, 250))
            if not purple:
                y = create_images_list("Images/Purplegirl.png", "Images/PurpleGRun.PNG", "Images/PurpleGRunLeft.PNG")
                girl = Character((540, 340), "purple", y)
                girl_lava1 = Lava("Images/purple lava.PNG", "purple", (20, 485))
                girl_lava2 = Lava("Images/purple lava.PNG", "purple", (104, 485))
                girl_lava3 = Lava("Images/purple lava.PNG", "purple", (188, 485))
                girl_lava4 = Lava("Images/purple lava.PNG", "purple", (272, 485))
                girl_lava5 = Lava("Images/purple lava.PNG", "purple", (356, 485))

                girl_door = Door("Images/DoorGirlPurple.png", "purple", (300, 120))

                girl_diamond1 = Diamond("Images/DPurple.png", "purple", (40, 465))
                girl_diamond2 = Diamond("Images/DPurple.png", "purple", (208, 465))
                girl_diamond3 = Diamond("Images/DPurple.png", "purple", (376, 465))
                girl_diamond4 = Diamond("Images/DPurple.png", "purple", (875, 250))
            if not RED:
                x = create_images_list("Images/Redboy.png", "Images/RedBRun.PNG", "Images/RedBRunLeft.PNG")
                boy = Character((441, 340), "red", x)
                boy_lava1 = Lava("Images/red lava.PNG", "red", (895, 485))
                boy_lava2 = Lava("Images/red lava.PNG", "red", (811, 485))
                boy_lava3 = Lava("Images/red lava.PNG", "red", (727, 485))
                boy_lava4 = Lava("Images/red lava.PNG", "red", (643, 485))
                boy_lava5 = Lava("Images/red lava.PNG", "red", (559, 485))

                boy_door = Door("Images/DoorBoyRed.png", "red", (655, 120))

                boy_diamond1 = Diamond("Images/DRed!.png", "red", (915, 465))
                boy_diamond2 = Diamond("Images/DRed!.png", "red", (747, 465))
                boy_diamond3 = Diamond("Images/DRed!.png", "red", (579, 465))
                boy_diamond4 = Diamond("Images/DRed!.png", "red", (105, 250))
            if not BLUE:
                x = create_images_list("Images/Blueboy.png", "Images/BlueBRun.PNG", "Images/BlueBRunLeft.PNG")
                boy = Character((441, 340), "blue", x)
                boy_lava1 = Lava("Images/blue lava.PNG", "blue", (895, 485))
                boy_lava2 = Lava("Images/blue lava.PNG", "blue", (811, 485))
                boy_lava3 = Lava("Images/blue lava.PNG", "blue", (727, 485))
                boy_lava4 = Lava("Images/blue lava.PNG", "blue", (643, 485))
                boy_lava5 = Lava("Images/blue lava.PNG", "blue", (559, 485))

                boy_door = Door("Images/DoorBoyBlue.png", "blue", (655, 120))

                boy_diamond1 = Diamond("Images/DBlue.png", "blue", (915, 465))
                boy_diamond2 = Diamond("Images/DBlue.png", "blue", (747, 465))
                boy_diamond3 = Diamond("Images/DBlue.png", "blue", (579, 465))
                boy_diamond4 = Diamond("Images/DBlue.png", "blue", (105, 250))
            if not PINK:
                x = create_images_list("Images/Pinkboy.png", "Images/PinkBRun.PNG", "Images/PinkBRunLeft.PNG")
                boy = Character((441, 340), "pink", x)
                boy_lava1 = Lava("Images/pink lava.PNG", "pink", (895, 485))
                boy_lava2 = Lava("Images/pink lava.PNG", "pink", (811, 485))
                boy_lava3 = Lava("Images/pink lava.PNG", "pink", (727, 485))
                boy_lava4 = Lava("Images/pink lava.PNG", "pink", (643, 485))
                boy_lava5 = Lava("Images/pink lava.PNG", "pink", (559, 485))

                boy_door = Door("Images/DoorBoyPink.png", "pink", (655, 120))

                boy_diamond1 = Diamond("Images/DPink.png", "pink", (915, 465))
                boy_diamond2 = Diamond("Images/DPink.png", "pink", (747, 465))
                boy_diamond3 = Diamond("Images/DPink.png", "pink", (579, 465))
                boy_diamond4 = Diamond("Images/DPink.png", "pink", (105, 250))
            if not PURPLE:
                x = create_images_list("Images/Purpleboy.png", "Images/PurpleBRun.PNG", "Images/PurpleBRunLeft.PNG")
                boy = Character((441, 340), "purple", x)
                boy_lava1 = Lava("Images/purple lava.PNG", "purple", (895, 485))
                boy_lava2 = Lava("Images/purple lava.PNG", "purple", (811, 485))
                boy_lava3 = Lava("Images/purple lava.PNG", "purple", (727, 485))
                boy_lava4 = Lava("Images/purple lava.PNG", "purple", (643, 485))
                boy_lava5 = Lava("Images/purple lava.PNG", "purple", (559, 485))

                boy_door = Door("Images/DoorBoyPurple.png", "purple", (655, 120))

                boy_diamond1 = Diamond("Images/DPurple.png", "purple", (915, 465))
                boy_diamond2 = Diamond("Images/DPurple.png", "purple", (747, 465))
                boy_diamond3 = Diamond("Images/DPurple.png", "purple", (579, 465))
                boy_diamond4 = Diamond("Images/DPurple.png", "purple", (105, 250))

        magic_buttons = []
        walls = []
        doors = [boy_door, girl_door]
        lavas = [girl_lava1, girl_lava2, girl_lava3, girl_lava4, girl_lava5, boy_lava1, boy_lava2, boy_lava3, boy_lava4,
                 boy_lava5]
        diamonds = [girl_diamond1, girl_diamond2, girl_diamond3, girl_diamond4, boy_diamond1, boy_diamond2,
                    boy_diamond3, boy_diamond4]
        t0 = time.time()
        savewall = None
        while boy.alive and girl.alive and run:  # Caharater1 is alive and Caracter2 is alive and Bool:
            retry = False
            screen.blit(background, (0, 0))
            for obstacle in objects1:
                obstacle.display_obstacle()
            for door in doors:
                door.display_door()
            for wall in walls:
                wall.display_wall()
            for b in magic_buttons:
                b.display_magic_button()
                if not b.pressed:
                    if b.press(boy) or b.press(girl):
                        for w in walls:
                            if w.color == b.color:
                                savewall = w
                                walls.remove(w)
                else:
                    if not b.press(boy) and not b.press(girl):
                        if savewall:
                            if savewall.able_to_display(boy, girl):
                                walls.append(savewall)
                                b.pressed = False
                                savewall = None

            for diamond in diamonds:
                gem = diamond.collect(boy) and diamond.collect(girl)
                if gem:
                    diamond.display_diamond()
                else:
                    diamonds.remove(diamond)
            girl.display_character(objects1, lavas, walls)
            boy.display_character(objects1, lavas, walls)
            if boy.door(doors) and girl.door(doors):
                run = False
            for lava in lavas:
                lava.display_lava()

            black = (0, 0, 0)
            screen.blit(timer,(460,10))
            font = pygame.font.SysFont("Calibri Regular.ttf", 35)
            if int(time.time() - t0) < 10:
                screen.blit(font.render(str(int(time.time() - t0)), True, black),(480,30))
            else:
                screen.blit(font.render(str(int(time.time() - t0)), True, black), (475, 30))
            if sound_on:
                sound_button.display_button()
            else:
                no_sound_button.display_button()
            # refreshing screen:
            pygame.display.flip()
            pygame.display.update()
            clock.tick(150)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if sound_on:
                        if mouse_in_button(sound_button, event.pos):
                            pygame.mixer.stop()
                            sound_on = False
                    else:
                        if mouse_in_button(no_sound_button, event.pos):
                            play_music("Sounds/backgroundSoundtrack2.ogg")
                            sound_on = True
                    print(mouse_pos)
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
                    if event.key == pygame.K_r:
                        girl.alive = False

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
            if len(lose_quotes) > 0:
                x = random.randint(0, len(lose_quotes) - 1)
        if run:
            retry_button = pygame.transform.scale(pygame.image.load("Images/retry-icon-9.jpg"), (100, 100))
            retry_button = Button(retry_button, (450, 200), 100, 100)
            home_button = pygame.transform.scale(pygame.image.load("Images/home.png"), (65, 65))
            home_button = Button(home_button, (468, 310), 65, 65)
            screen.blit(background, (0, 0))
            retry_button.display_button()
            home_button.display_button()

            if len(lose_quotes) != 0:
                screen.blit(lose_quotes[x], (150, 20))

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
                    if mouse_in_button(home_button, mouse_pos):
                        run = False
                        home()
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()

    pygame.mixer.stop()
    win_sound()
    t = time.time() - t0
    print(t)
    level[0] = level[0] + 1
    middle(red,blue,pink,purple,RED,BLUE,PINK,PURPLE,t,tmax,diamonds)


def send():
    runend = True
    b = False
    if len(phNum) == 13:
        t = time.localtime()
        current_h = time.strftime("%H", t)
        current_m = time.strftime("%M", t)
        b = True
    end_b = pygame.transform.scale(pygame.image.load("Images/EndGame.png"), screen_size)
    tziun = (12 - stars[0])*6
    tziun = 100 - tziun
    msg = "שלום " + name+ "! הגעתם לסוף המשחק, כל הכבוד! הציון שלך במשחק הוא: " + " " + str(tziun) + "שתפו את חברכם וגלו מי השחקן הטוב ביותר!"
    while runend:
        screen.blit(end_b, (0, 0))
        pygame.display.flip()
        pygame.display.update()
        time.sleep(10)
        if b:
            nisuy.send_sms(msg, phNum)
            b = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runend = False
                pygame.quit()
                quit()


def home():
    global phNum
    global sound_on
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

    big_boy = pygame.transform.scale(pygame.image.load("Images/Redboy.png"), (170, 280))
    big_girl = pygame.transform.scale(pygame.image.load("Images/Bluegirl.png"), (170, 285))

    while start_run:
        screen.blit(start_background, (0, 0))
        screen.blit(big_girl, (105, 225))
        screen.blit(big_boy, (730, 230))
        if sound_on:
            sound_button.display_button()
        else:
            no_sound_button.display_button()
        Play_BUTTON.display_button()
        star = pygame.transform.scale(pygame.image.load("Images/Star.png"), (60, 60))
        screen.blit(star, (30, 20))
        black = (0, 0, 0)
        font = pygame.font.SysFont("ttf.Calibri", 50)
        screen.blit(font.render("X " + str(stars[0]), True, black), (100, 40))

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
                    start_run = False
                if sound_on:
                    if mouse_in_button(sound_button, event.pos):
                        pygame.mixer.stop()
                        sound_on = False
                else:
                    if mouse_in_button(no_sound_button, event.pos):
                        play_music("Sounds/startSoundTrack.mp3")
                        sound_on = True
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
    while level[0] <= 4:
        if level[0] == 1:
            level1(red, blue, pink, purple, RED, BLUE, PINK, PURPLE)
        if level[0] == 2:
            level2(red, blue, pink, purple, RED, BLUE, PINK, PURPLE)
        if level[0] == 3:
            level3(red, blue, pink, purple, RED, BLUE, PINK, PURPLE)
        if level[0] == 4:
            level4(red, blue, pink, purple, RED, BLUE, PINK, PURPLE)
    send()
    # the end


def start():
    ins = pygame.transform.scale(pygame.image.load("Images/Instructions.png"), screen_size)
    instructions = True
    while instructions:
        screen.blit(ins, (0, 0))
        pygame.display.flip()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                instructions = False
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    global phNum
    global name
    run = True
    whatsapp_button = pygame.transform.scale(pygame.image.load("Images/Whatsapp_logo.png"), (90, 90))
    whatsapp_button = Button(whatsapp_button,(455, 260), 90, 90)
    start_BUTTON = pygame.transform.scale(pygame.image.load("Images/start_button.png"), (160, 85))
    start_BUTTON = Button(start_BUTTON, (420, 150), 85,160)
    n_button = pygame.transform.scale(pygame.image.load("Images/name.png"), (250, 90))
    n_button = Button(n_button,(380, 370),90,250)
    while run:
        screen.blit(start_background, (0, 0))
        whatsapp_button.display_button()
        start_BUTTON.display_button()
        n_button.display_button()
        font = pygame.font.SysFont('chalkduster.ttf', 45, bold=False)
        img = font.render(name, True, (50, 50, 50))
        screen.blit(img, (400, 400))
        font2 = pygame.font.SysFont('chalkduster.ttf', 20, bold=False)
        img = font2.render("ENTER PHONE NUMBER:", True, (50, 50, 50))
        screen.blit(img, (425, 250))
        font3 = pygame.font.SysFont('chalkduster.ttf', 25, bold=False)
        img = font3.render(phNum, True, (50, 50, 50))
        screen.blit(img, (450, 350))

        pygame.display.flip()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_in_button(whatsapp_button, event.pos):
                    button_click()
                    phNum = (get_str(425,348))
                if mouse_in_button(n_button, event.pos):
                    button_click()
                    name = get_str(425,410)
                if mouse_in_button(start_BUTTON, event.pos):
                    button_click()
                    run = False
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    with open(name+".txt", 'a', encoding='utf-8') as f:
        f.write(str(level[0])+"\n")
        f.write(str(stars[0])+"\n")

    with open(name+".txt", "r") as f:  # read from file
        level[0] = int(f.readline())
        stars[0] = int(f.readline())
    if len(phNum) == 10:
        phNum = phNum[1:]
        phNum = "+972" + phNum
    else:
        phNum = ""

    home()


start()
import nisuy
send()
print("gever retzah ata")
quit()
