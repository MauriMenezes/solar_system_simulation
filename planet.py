import pygame
WIDTH, HEIGHT = 800, 700


class Planets:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 200/AU
    TIMESTEP = 3600 * 24  # 1 day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + WIDTH / 2
        pygame.draw.circle(win, self.color, (x, y), self.radius)
