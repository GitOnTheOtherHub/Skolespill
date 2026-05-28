import pygame


pygame.init()

WIDTH = 700
HEIGHT = 500


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption ("Spill")

clock = pygame.time.Clock
fps = 60

enemy_size = 50
enemy_x = WIDTH // 2
enemy_y = HEIGHT // 2
enemy_speed = 3

#loop
run = True
while run:

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.display.flip()
            pygame.quit()


enemy_image = pygame.image.load('enemy.png', (WIDTH, HEIGHT))
enemy_x = max(0, min(WIDTH - enemy_size, enemy_x))
enemy_y = max(0, min(HEIGHT - enemy_size, enemy_y))
