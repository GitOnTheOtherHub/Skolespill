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