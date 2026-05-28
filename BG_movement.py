import pygame
import math

pygame.init()

timer = pygame.time.Clock
fps = 60

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption ("Spill")




#lader inn bildet
bg = pygame.image.load("background.jpg").convert()
bg_width = bg.get_width()
screen.blit(bg, (0,0))

tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1



run = True
while run:
    #timer.tick(fps)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()





