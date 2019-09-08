import pygame as pg


class Boundary:
    def __init__(self, screen: pg.display, start: tuple, end: tuple):
        self.start = pg.Vector2(start)
        self.end = pg.Vector2(end)
        self.image = None

    def update(self, screen: pg.display):
        self.image = pg.draw.line(screen, pg.Color('white'), self.start, self.end, 2)
