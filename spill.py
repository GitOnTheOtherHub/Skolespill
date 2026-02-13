import pygame as pg
import numpy as np

pg.init()
screen = pg.display.set_mode((500, 500))
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    frame = np.random.uniform(0,1, (80, 60, 3))
    surf = pg.surfarray.make_surface(frame*255)
    surf = pg.transform.scale(surf, (500, 500))

    screen.blit(surf, (0, 0))
    pg.display.update()

pg.quit()