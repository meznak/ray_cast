import pygame as pg
from random import randint

from boundary import Boundary
from particle import Particle
from ray import Ray


def main():
    ### CONFIG
    screen_w = 500
    screen_h = 500
    border_on = True
    num_walls = 6
    num_rays = 180
    ### END CONFIG

    pg.init()
    screen = pg.display.set_mode((screen_w, screen_h))

    running = True
    pg.event.set_allowed([pg.QUIT, pg.KEYDOWN, pg.KEYUP])

    p = Particle()
    boundaries = []
    rays = []

    if border_on:
        boundaries.append(Boundary(screen, (0, 0), (screen_w, 0)))
        boundaries.append(Boundary(screen, (screen_w, 0), (screen_w, screen_h)))
        boundaries.append(Boundary(screen, (screen_w, screen_h), (0, screen_h)))
        boundaries.append(Boundary(screen, (0, screen_h), (0, 0)))

    for i in range(num_walls):
        boundaries.append(Boundary(screen,
                                   (randint(0, screen_w), randint(0, screen_h)),
                                   (randint(0, screen_w), randint(0, screen_h))))

    for i in range(num_rays):
        rays.append(Ray(p, i * 360 / num_rays))

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill((0, 0, 0))

        for b in boundaries:
            b.update(screen)

        p.update(screen)
        for r in rays:
            r.update(screen, p, boundaries)

        pg.display.update()
        pg.time.wait(75)


if __name__ == "__main__":
    main()
