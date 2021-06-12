import pygame
from Variables import *
import numpy as np

class Draw:
    def __init__(self):
        global SCREEN, CLOCK
        pygame.init()

        SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        SCREEN.fill(BLACK)

    def draw_board(self, cells, draw_grid = False):
        SCREEN.fill(BLACK)
        for (x,y), life in np.ndenumerate(cells):
            rect = pygame.Rect(round(x*BLOCK_SIZE), round(y*BLOCK_SIZE), BLOCK_SIZE, BLOCK_SIZE)
            if draw_grid:
                pygame.draw.rect(SCREEN, WHITE if life == ALIVE else GRAY_WHITE, rect, 0 if life == ALIVE else 1)
            else:
                pygame.draw.rect(SCREEN, WHITE if life == ALIVE else BLACK, rect, 0)
