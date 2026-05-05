import pygame

pygame.init()

win = pygame.display.set_mode((700, 500))
pygame.display.set_caption ("Spill")

timer = pygame.time.Clock
fps = 60
player_x = 300
player_y = 300
player_speed = 3

class player:
    def __init__(self, x, y):
        self.rect = pygame.rect(x, y, 32, 32)  
        self.x = x
        self.y = y

run = True
while run:
    #timer.tick(fps)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()



