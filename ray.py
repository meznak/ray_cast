from particle import Particle
import pygame as pg

drawline = pg.draw.line


class Ray:
    def __init__(self, p: Particle, heading: float = 0):
        self.start = p.pos
        self.heading = heading
        self.end: pg.math.Vector2 = pg.math.Vector2()
        self.image = None

    def update(self, screen: pg.display, p: Particle, boundaries: list):
        self.start = p.pos
        self.end.from_polar((10000, self.heading))

        closest = float("inf")
        new_end = pg.Vector2()

        x3 = self.start.x
        x4 = self.end.x
        y3 = self.start.y
        y4 = self.end.y

        for b in boundaries:
            x1 = b.start.x
            x2 = b.end.x
            y1 = b.start.y
            y2 = b.end.y

            den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if den == 0:
                return

            t_num = (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)
            t = t_num / den
            u_num = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3))
            u = u_num / den

            if u >= 0 and 0 <= t <= 1:
                x = x1 + t * (x2 - x1)
                y = y1 + t * (y2 - y1)
                dist = self.start.distance_to((x, y))
                if dist < closest:
                    closest = dist
                    new_end.xy = x, y

        if closest == float("inf"):
            self.end = self.start
            self.image = None
        else:
            self.end = new_end
            self.image = drawline(screen, (100, 100, 100), self.start, self.end, 1)
