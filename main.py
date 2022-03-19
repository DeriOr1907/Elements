import pygame
from Classes.Character import *
pygame.init()
screen_size = (1000,530)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Elements')
clock = pygame.time.Clock()


def create_images_list(imgpath1,imgpath2,imgpath3):
    imags = [pygame.transform.scale(pygame.image.load(imgpath1), (45,45)), pygame.transform.scale(pygame.image.load(imgpath2), (45,45)), pygame.transform.scale(pygame.image.load(imgpath3), (45,45))]
    return imags


bluegirl_images = create_images_list("Images/Bluegirl.png", "Images/BlueGRun.PNG", "Images/BlueGRunLeft.PNG")
bluegirl = Character((300,200),"Blue",bluegirl_images)
background = pygame.transform.scale(pygame.image.load("Images/background2.jpeg"), screen_size)
while True: # Caharater1 is alive and Caracter2 is alive:
    screen.blit(background, (0, 0))
    bluegirl.display_character()
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()