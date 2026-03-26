import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption ("Spill")

run = True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False
pygame.quit()

Walkleft = False
Walkright = False
Walkup = False
Walkdown = False

if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_w:
        Walkup = True
        

if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_a:
        Walkleft = True

if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_s:
        Walkdown = True

if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_d:
        Walkright = True


if event.type == pygame.KEYUP:
    if event.key == pygame.K_w:
        Walkup = False

if event.type == pygame.KEYUP:
    if event.key == pygame.K_a:
        Walkleft = False

if event.type == pygame.KEYUP:
    if event.key == pygame.K_s:
        Walkdown = False

if event.type == pygame.KEYUP:
    if event.key == pygame.K_d:
        Walkright = False
    