import pygame
pygame.init()
screen_size = (1000,530)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Elements')
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load("Images/background2.jpeg"), screen_size)
while True: #Caharater1 is alive and Caracter2 is alive:
    screen.blit(background, (0, 0))
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()