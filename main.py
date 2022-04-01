import pygame
from Constants import screen, screen_size
from Classes.Character import *
from Classes.Object import *
from Classes.Button import *
from helpers import *
pygame.display.set_caption('Elements')
clock = pygame.time.Clock()


def create_images_list(imgpath1, imgpath2, imgpath3):
    imags = [pygame.transform.scale(pygame.image.load(imgpath1), (36, 55)),
             pygame.transform.scale(pygame.image.load(imgpath2), (41, 45)),
             pygame.transform.scale(pygame.image.load(imgpath3), (41, 45))]
    return imags


start_background = pygame.transform.scale(pygame.image.load("Images/StartPic!!!.png"), screen_size)
Play_BUTTON = pygame.transform.scale(pygame.image.load("Images/PlayButton!!!.png"), (90,90))
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

objects_color = (95, 80, 45)
obj1 = Object(1050, 30, 0, 500, objects_color)
obj2 = Object(20, 530, 0, 0, objects_color)
obj3 = Object(20, 530, 980, 0, objects_color)
obj4 = Object(1050, 25, 0, 0, objects_color)
obj5 = Object(500, 50, 350, 370, objects_color)
obj6 = Object(500, 50, 150, 270, objects_color)
obj7 = Object(50, 400, 0, 370, objects_color)
obj8 = Object(550, 800, 900, 470, objects_color)
obj9 = Object(50, 70, 30, 400, objects_color)
objects = [obj1, obj2, obj3, obj4, obj5,obj6,obj7,obj8,obj9]

run = True
start_run = True

blue = False
red = True
pink = True
purple = True

BLUE = True
RED = False
PINK = True
PURPLE = True

background = pygame.transform.scale(pygame.image.load("Images/background2.jpeg"), screen_size)

big_boy = pygame.transform.scale(pygame.image.load("Images/Redboy.png"), (170, 280))
big_girl = pygame.transform.scale(pygame.image.load("Images/Bluegirl.png"), (180, 285))


start_pic = pygame.transform.scale(pygame.image.load("Images/StartPic!!!.png"), screen_size)


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
                start_run = False
            if RED:
                if mouse_in_button(oneButton,event.pos):
                    big_girl = pygame.transform.scale(pygame.image.load("Images/Redgirl.png"), (170, 285))
                    red = False
                    blue = True
                    pink = True
                    purple = True

            if BLUE:
                if mouse_in_button(twoButton,event.pos):
                    big_girl = pygame.transform.scale(pygame.image.load("Images/Bluegirl.png"), (170, 285))
                    red = True
                    blue = False
                    pink = True
                    purple = True
            if PINK:
                if mouse_in_button(threeButton,event.pos):
                    big_girl = pygame.transform.scale(pygame.image.load("Images/Pinkgirl.png"), (170, 285))
                    red = True
                    blue = True
                    pink = False
                    purple = True
            if PURPLE:
                if mouse_in_button(fourButton,event.pos):
                    big_girl = pygame.transform.scale(pygame.image.load("Images/Purplegirl.png"), (170, 285))
                    red = True
                    blue = True
                    pink = True
                    purple = False

            if red:
                if mouse_in_button(one_Button,event.pos):
                    big_boy = pygame.transform.scale(pygame.image.load("Images/Redboy.png"), (170, 285))
                    RED = False
                    BLUE = True
                    PINK = True
                    PURPLE = True
            if blue:
                if mouse_in_button(two_Button,event.pos):
                    big_boy = pygame.transform.scale(pygame.image.load("Images/Blueboy.png"), (170, 285))
                    RED = True
                    BLUE = False
                    PINK = True
                    PURPLE = True
            if pink:
                if mouse_in_button(three_Button,event.pos):
                    big_boy = pygame.transform.scale(pygame.image.load("Images/Pinkboy.png"), (170, 285))
                    RED = True
                    BLUE = True
                    PINK = False
                    PURPLE = True
            if purple:
                if mouse_in_button(four_Button,event.pos):
                    big_boy = pygame.transform.scale(pygame.image.load("Images/Purpleboy.png"), (170, 285))
                    RED = True
                    BLUE = True
                    PINK = True
                    PURPLE = False
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

if not red:
    girl = create_images_list("Images/Redgirl.png", "Images/RedGRun.PNG", "Images/RedGRunLeft.PNG")
    girl = Character((300, 200), "red", girl)
if not blue:
    girl = create_images_list("Images/Bluegirl.png", "Images/BlueGRun.PNG", "Images/BlueGRunLeft.PNG")
    girl = Character((300, 200), "blue", girl)
if not pink:
    girl = create_images_list("Images/Pinkgirl.png","Images/PinkGRun.PNG","Images/PinkGRunLeft.PNG")
    girl = Character((300, 200), "pink", girl)
if not purple:
    girl = create_images_list("Images/Purplegirl.png","Images/PurpleGRun.PNG","Images/PurpleGRunLeft.PNG")
    girl = Character((300, 200), "purple", girl)

if not RED:
    boy = create_images_list("Images/Redboy.png", "Images/RedBRun.PNG", "Images/RedBRunLeft.PNG")
    boy = Character((300, 200), "red", boy)
if not BLUE:
    boy = create_images_list("Images/Blueboy.png","Images/BlueBRun.PNG","Images/BlueBRunLeft.PNG")
    boy = Character((300, 200), "blue", boy)
if not PINK:
    boy = create_images_list("Images/Pinkboy.png","Images/PinkBRun.PNG","Images/PinkBRunLeft.PNG")
    boy = Character((300, 200), "pink", boy)
if not PURPLE:
    boy = create_images_list("Images/Purpleboy.png","Images/PurpleBRun.PNG","Images/PurpleBRunLeft.PNG")
    boy = Character((300, 200), "purple", boy)


while boy.alive and girl.alive and run:  # Caharater1 is alive and Caracter2 is alive and Bool:
    screen.blit(background, (0, 0))
    for obstacle in objects:
        obstacle.display_obstacle()
    girl.display_character(objects)
    boy.display_character(objects)
    # refreshing screen:
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
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
            run = False
            pygame.quit()
            quit()
quit()