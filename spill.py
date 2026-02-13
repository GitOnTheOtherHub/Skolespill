import pygame
import math

pygame.display.set_caption("infiltrering")
win_width, win_height = (500, 500)
display = pygame.display.set_mode((win_width, win_height))

enviornment = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]
fov = 80
xpos, ypos = (1, 1)
rot_r = math.pi/4

run = True
while run:
    
    for e in pygame.event.get():
        if e.type == quit:
            run = False