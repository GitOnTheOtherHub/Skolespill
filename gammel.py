""""
Dette spillet et 2D platformer spill med objektet å drepe flest mulig fiender
Du må beskytte degselv fra en horde med muterte bakterier
Du kan angripe ved å trykke på Z for høyre angrep og X for venstre angrep
Du kan bevege deg til høyre og venstre via høyre og venstre pil taster.

"""

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
square_x = WIDTH // 2.1
square_y = HEIGHT // 2
speed = 0.07

enemy_size = 50
enemy_x = WIDTH // 1
enemy_y = HEIGHT // 1
enemy_speed = 1

#lader inn bildene
bg = pygame.image.load("background.jpg").convert()
bg_width = bg.get_width()

spiller = pygame.image.load('Idle.png').convert_alpha()
bakterie = pygame.image.load('enemy.png').convert_alpha()

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

    firkant_enemy = pygame.draw.rect(
        screen,
        (33, 94, 19),
        (enemy_x, enemy_y, enemy_size, enemy_size)
    )

    screen.blit(spiller, firkant)
    screen.blit(bakterie, firkant_enemy)

    # pygame.transform.scale(spiller, (100, 100))

    pygame.display.flip()
    timer.tick

