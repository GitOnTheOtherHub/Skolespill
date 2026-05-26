import pygame


pygame.init()

WIDTH = 700
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption ("Spill")

clock = pygame.time.Clock
fps = 60

#
square_size = 50
square_x = WIDTH // 1
square_y = HEIGHT // 2
speed = 0.1


#loop
while True:

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.display.flip()
            pygame.quit()

    screen.fill((50, 10, 10))

    #Bevegelse
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square_x -= speed
    if keys[pygame.K_RIGHT]:
        square_x += speed

    square_x = max(0, min(WIDTH - square_size, square_x))
    square_y = max(0, min(HEIGHT - square_size, square_y))

    firkant = pygame.draw.rect(
        screen,
        (0, 200, 255),
        (square_x, square_y, square_size, square_size)
    )

    sprite = pygame.image.load('Idle.png').convert_alpha()
    screen.blit(sprite, firkant)

    pygame.display.flip()
    clock.tick


