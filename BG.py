import pygame
import sys
pygame.init()

win = pygame.display.set_mode((700, 500))
pygame.display.set_caption ("Spill")

run = True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False
pygame.quit()

