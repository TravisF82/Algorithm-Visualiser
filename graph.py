import pygame
import math
import sys

print("PYTHON:", sys.executable)

class Graph():
    PADDING = 50

    def __init__(self, width, height):
        self.WINDOW_WIDTH = width
        self.WINDOW_HEIGHT = height

    def Run(self):
        pygame.init()
        window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()
            pygame.draw.rect(window, Color.WHITE, (50, 50, 100, 100), border_top_left_radius=10, border_top_right_radius=10)


            clock.tick(240)
        pygame.quit()

class Color():
    GREEN = (27, 207, 33)
    BLUE = (17, 84, 217)
    WHITE = (255, 255, 255)
    PURPLE = (213, 20, 219)
    BLACK = (0, 0, 0)