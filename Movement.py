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

walkwest = False
walkeast = False
Walknorth = False
Walksouth = False

if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_w:
        Walknorth = True

if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_a:
        walkeast = True

if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_s:
        Walksouth = True

if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_d:
        Walkwast = True


if event.type == pygame.KEYUP:
    if event.key == pygame.K_w:
        Walknorth = False

if event.type == pygame.KEYUP:
    if event.key == pygame.K_a:
        Walknorth = False

if event.type == pygame.KEYUP:
    if event.key == pygame.K_s:
        Walknorth = False

if event.type == pygame.KEYUP:
    if event.key == pygame.K_d:
        Walknorth = False
    