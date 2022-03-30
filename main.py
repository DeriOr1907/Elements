import pygame
from Constants import screen, screen_size
from Classes.Character import *
from Classes.Object import *

pygame.display.set_caption('Elements')
clock = pygame.time.Clock()


def create_images_list(imgpath1, imgpath2, imgpath3):
    imags = [pygame.transform.scale(pygame.image.load(imgpath1), (45, 45)),
             pygame.transform.scale(pygame.image.load(imgpath2), (40, 45)),
             pygame.transform.scale(pygame.image.load(imgpath3), (40, 45))]
    return imags


bluegirl_images = create_images_list("Images/Bluegirl.png", "Images/BlueGRun.PNG", "Images/BlueGRunLeft.PNG")
bluegirl = Character((300, 200), "Blue", bluegirl_images)
redboy_images = create_images_list("Images/Redboy.png", "Images/RedBRun.PNG", "Images/RedBRunLeft.PNG")
background = pygame.transform.scale(pygame.image.load("Images/background2.jpeg"), screen_size)
redboy = Character((300, 200), "Red", redboy_images)
objects_color = (95, 80, 45)
obj1 = Object(1050, 30, 0, 500, objects_color)
obj2 = Object(20, 530, 0, 0, objects_color)
obj3 = Object(20, 530, 980, 0, objects_color)
obj4 = Object(1050, 25, 0, 0, objects_color)
obj5 = Object(500, 300, 350, 370, objects_color)
obj6 = Object(500, 100, 150, 270, objects_color)
obj7 = Object(50, 100, 0, 370, objects_color)
obj8 = Object(550, 100, 900, 470, objects_color)
obj9 = Object(50, 70, 30, 400, objects_color)
objects = [obj1, obj2, obj3, obj4, obj5,obj6,obj7,obj8,obj9]
boy = redboy
girl = bluegirl
run = True
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
