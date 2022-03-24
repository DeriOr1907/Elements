import pygame
from Constants import screen, screen_size
from Classes.Character import Character

pygame.display.set_caption('Elements')
clock = pygame.time.Clock()


def create_images_list(imgpath1, imgpath2, imgpath3):
    imags = [pygame.transform.scale(pygame.image.load(imgpath1), (45, 45)),
             pygame.transform.scale(pygame.image.load(imgpath2), (40,45)),
             pygame.transform.scale(pygame.image.load(imgpath3), (40,45))]
    return imags


bluegirl_images = create_images_list("Images/Bluegirl.png", "Images/BlueGRun.PNG", "Images/BlueGRunLeft.PNG")
bluegirl = Character((300, 200), "Blue", bluegirl_images)
redboy_images = create_images_list("Images/Redboy.png", "Images/RedBRun.PNG", "Images/RedBRunLeft.PNG")
background = pygame.transform.scale(pygame.image.load("Images/background2.jpeg"), screen_size)
redboy = Character((300, 200), "Red", redboy_images)
Bool = True
while Bool: # Caharater1 is alive and Caracter2 is alive and Bool:
    screen.blit(background, (0, 0))
    bluegirl.display_character()
    redboy.display_character()
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                bluegirl.move_right()
            if event.key == pygame.K_LEFT:
                bluegirl.move_left()
            if event.key == pygame.K_UP:
                bluegirl.start_jump()

            if event.key == pygame.K_d:
                redboy.move_right()
            if event.key == pygame.K_a:
                redboy.move_left()
            if event.key == pygame.K_w:
                redboy.start_jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                bluegirl.stop_moving_right()
            if event.key == pygame.K_LEFT:
                bluegirl.stop_moving_left()

            if event.key == pygame.K_d:
                redboy.stop_moving_right()
            if event.key == pygame.K_a:
                redboy.stop_moving_left()
        if event.type == pygame.QUIT:
            Bool = False
            pygame.quit()

quit()