import pygame as pg
import numpy as np

def main():
    pg.init()
screen = pg.display.set_mode((500, 500))
running = True

hres = 120
halfvres = 100

mod = hres/60
posx, posy, rot = 0, 0, 0
frame = np.random.uniform(0,1, (hres, halfvres*2, 3))

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    for i in range(hres):
        rot_i = rot + np.deg2rad(1/mod - 30)
        sin, cos = np.sin(rot_i), np.cos(rot_i)

    for j in range(halfvres):
        n = halfvres/(halfvres-j)
        x, y = posx + cos*n, posy + sin*n


    if int(x)%2 == int (y)%2:
        frame[i] [halfvres*2-j] = [0, 0, 0]
    else:
        frame[i] [halfvres*2-j] = [1, 1, 1]


    surf = pg.surfarray.make_surface(frame*255)
    surf = pg.transform.scale(surf, (500, 500))

    screen.blit(surf, (0, 0))
    pg.display.update()
if __name__== '__main__':
    main()
pg.quit()