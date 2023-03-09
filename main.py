import pygame
from planet import Planets
import math

pygame.init()
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
WIDTH, HEIGHT = 800, 700
BLUE = (59, 160, 230)
RED = (188, 39, 50)
GREY = (80, 78, 81)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Solar System Simulation')

sun = Planets(0, 0, 30, YELLOW, 1.98892 * 10**30)
sun.sun = True
earth = Planets(-1 * Planets.AU, 0, 16, BLUE, 5.9742 * 10**24)
mars = Planets(-1.524 * Planets.AU, 0, 12, RED, 6.39 * 10**23)
mercury = Planets(0.387 * Planets.AU, 0, 8, GREY, 0.330*10**24)
venus = Planets(0.723 * Planets.AU, 0, 14, WHITE, 4.8685 * 10**24)
p = [sun, earth, mars, mercury, venus]


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        # WIN.fill(WHITE)

        # pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False

        for i in p:
            i.draw(WIN)
        pygame.display.update()

    pygame.quit()


main()
