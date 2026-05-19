import pygame

pygame.init()

win = pygame.display.set_mode((700, 500))
pygame.display.set_caption ("Spill")

timer = pygame.time.Clock
fps = 60


#lader inn bildet
bg = pygame.image.load("background.jpg").convert()
bg_width = bg.get_width()




run = True
while run:
    #timer.tick(fps)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()





