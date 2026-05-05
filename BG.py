import pygame
pygame.init()

win = pygame.display.set_mode((700, 500))
pygame.display.set_caption ("Spill")

timer = pygame.time.Clock
fps = 60


run = True
while run:
    #timer.tick(fps)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()


