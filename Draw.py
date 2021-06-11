import pygame
from Variables import *
import numpy as np

class Draw:
    def __init__(self):
        global SCREEN, CLOCK
        pygame.init()

        SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        SCREEN.fill(BLACK)

    def draw_board(self, cells):
        for (x,y), life in np.ndenumerate(cells):
            rect = pygame.Rect(round(x*BLOCK_SIZE), round(y*BLOCK_SIZE), BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, WHITE if life == 1 else BLACK, rect, 0)