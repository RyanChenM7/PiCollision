import subprocess
import sys


def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

# noinspection PyPep8
# SW = (self.h_pos-self.size, GROUND)
# SE = (self.h_pos+self.size, GROUND)
# NW = (self.h_pos-self.size, GROUND-2*self.size)
# NE = (self.h_pos+self.size, GROUND-2*self.size)


try:
    import numpy as np
except ImportError:
    install('numpy')
    import numpy as np

try:
    import pygame
except ImportError:
    install('pygame')
    import pygame

white = pygame.Color("white")
red = pygame.Color("red")
blue = pygame.Color("blue")

try:
    import os
except ImportError:
    install('os')
    import os

try:
    from decimal import *
except ImportError:
    install('decimal')
    import decimal

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (25, 75)

WIDTH = 1280
HEIGHT = 720
GROUND = HEIGHT-100
WALL = 100

count = 0


def collide(b1, b2, forced=False):
    global count
    m1 = Decimal(b1.mass)
    m2 = Decimal(b2.mass)
    v1 = Decimal(b1.h_vel)
    v2 = Decimal(b2.h_vel)
    if b2.h_pos - b1.h_pos <= b1.size + b2.size or forced:
        count += 1

        u2 = Decimal(2)*v1*m1/(m1+m2)-v2*(m1-m2)/(m1+m2)
        u1 = v1*(m1-m2)/(m1+m2) + Decimal(2)*v2*m2/(m1+m2)

        b1.h_vel = u1
        b2.h_vel = u2


class Block:
    def __init__(self, h_pos, mass, h_vel):
        self.h_pos = Decimal(h_pos)
        self.h_vel = Decimal(h_vel)
        self.mass = mass
        self.size = Decimal(0.5*np.log10(int(mass))*10+10)
        self.rect = pygame.Rect([float(self.h_pos)-float(self.size), GROUND, 2*float(self.size), -2*float(self.size)])

    def update(self, screen):
        self.h_pos += self.h_vel
        pygame.draw.rect(screen, white, self.rect)

    def wall(self):
        if self.h_pos - WALL <= self.size:
            global count
            count += 1
            self.h_vel *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, white, self.rect)


block1 = Block(200, 1, 0)
block2 = Block(350, 10**2, -0.3)

line_width = 5


def draw_lines(screen):
    # Wall
    pygame.draw.line(screen, red, (WALL-line_width, GROUND+line_width),
                     (WALL-line_width, 0), line_width)

    # Ground
    pygame.draw.line(screen, red, (WALL-line_width, GROUND+line_width),
                     (WIDTH-line_width, GROUND+line_width), line_width)


def draw_text(screen, text):
    font = pygame.font.Font('freesansbold.ttf', 32)

    # create a text suface object,
    # on which text is drawn on it.
    text = font.render(str(text), True, white, blue)

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (WIDTH - 100, HEIGHT - 50)
    screen.blit(text, textRect)


def main():
    pygame.init()
    logo = pygame.image.load("PISYMBOL.jpg")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Computing Pi with Colliding Blocks")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    running = True
    clock = pygame.time.Clock()

    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                return print(event)

        screen.fill((80, 80, 80))
        draw_text(screen, count)
        draw_lines(screen)
        if block1.h_pos < WALL + block1.size or block2.h_pos < WALL + block1.size + block2.size:
            block1.rect = pygame.Rect([WALL, GROUND, 2*float(block1.size), -2*float(block1.size)])
            block2.rect = pygame.Rect([WALL + 2*block1.size, GROUND, 2*float(block2.size), -2*float(block2.size)])
        else:
            block1.rect = pygame.Rect([float(block1.h_pos)-float(block1.size), GROUND, 2*float(block1.size), -2*float(block1.size)])
            block2.rect = pygame.Rect([float(block2.h_pos)-float(block2.size), GROUND, 2*float(block2.size), -2*float(block2.size)])

        block1.update(screen)
        block2.update(screen)
        block1.wall()
        collide(block1, block2)







        pygame.display.update()
        clock.tick(100000)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    main()
