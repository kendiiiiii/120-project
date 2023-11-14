import pygame

pygame.init()

SCREEN_WIDTH = 8008
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True
while run:
    
    for even in pygame.event.get():
        run = False
        
pygame.quit()