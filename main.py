import pygame
pygame.init()
screen_size = (984,553)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Elements')
clock = pygame.time.Clock()
img = pygame.transform.scale(pygame.image.load(""),(984,553))
while True: #Caharater1 is alive and Caracter2 is alive:
    screen.blit(img,(0, 0))
pygame.quit()
quit()