import pygame
import math

class Graph:

    GREEN = "#1bcf21"
    BLUE = "#1154d9"
    WHITE = "#ffffff"
    PURPLE = "#d514db"
    BLACK = "#000000"

    PADDING = 50

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Algorithm Visualizer")
    
    def CreateBars(self, data):
        self.bar_width = math.floor((self.width - self.PADDING * 2) / len(data))
        self.bar_height = math.floor(self.height / (max(data) - min(data)))