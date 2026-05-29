""""
Dette spillet et 2D platformer spill med objektet å drepe flest mulig fiender
Du må beskytte degselv fra en horde med muterte bakterier
Du kan angripe ved å trykke på Z for høyre angrep og X for venstre angrep
Du kan bevege deg til høyre og venstre via høyre og venstre pil taster.

"""

import pygame
import random
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

    class enemy:
     def __init__(self, x):
        self.w, self.h = 34, 48
        self.x = WIDTH - 50
        self.y = HEIGHT - 80              # Stand on the ground.
        self.dir = random.choice([-1, 1])        # Random initial direction.
        self.speed = random.uniform(1.2, 2.6)    # Random patrol speed.
        self.left = x - random.randint(40, 120)  # Random left patrol bound.
        self.right = x + random.randint(40, 120) # Random right patrol bound.
        self.alive = True
        
    @property
    def rect(self):
        """pygame.Rect: The player's bounding box for collision checks."""
        return pygame.Rect(self.x, self.y, self.w, self.h)
    
    Enemy_color = 200, 50, 50

    def draw(self, surf):
        pygame.draw.rect(surf, Enemy_color, self.rect, border_radius=6)


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

    screen.blit(spiller, firkant)


    # pygame.transform.scale(spiller, (100, 100))

    pygame.display.flip()
    timer.tick

