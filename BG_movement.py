import pygame
import math

pygame.init()

timer = pygame.time.Clock
fps = 60

WIDTH = 700
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption ("Spill")

square_size = 50
square_x = WIDTH // 1
square_y = HEIGHT // 2
speed = 0.07

#lader inn bildet
bg = pygame.image.load("background.jpg").convert()
bg_width = bg.get_width()

tiles = math.ceil(WIDTH/ bg_width) + 1

run = True
while run:

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.display.flip()
            pygame.quit()

    

    #Bevegelse
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square_x -= speed
    if keys[pygame.K_RIGHT]:
        square_x += speed

    screen.blit(bg, (0,0))

    square_x = max(0, min(WIDTH - square_size, square_x))
    square_y = max(0, min(HEIGHT - square_size, square_y))

    firkant = pygame.draw.rect(
        screen,
        (50, 10, 102),
        (square_x, square_y, square_size, square_size)
    )

    sprite = pygame.image.load('Idle.png').convert_alpha()
    screen.blit(sprite, firkant)
    
    pygame.display.flip()
    timer.tick

