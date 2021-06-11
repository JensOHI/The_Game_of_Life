import pygame
import sys
import numpy as np
import math
from Variables import *
from Draw import Draw
from copy import deepcopy


def update_cells(cells):
    new_cells = deepcopy(cells)
    for (x,y), life in np.ndenumerate(cells):
        numbers_of_neighbours = 0
        for neighbour in neighbours:
            dx = neighbour[0]
            dy = neighbour[1]
            if (x+dx) < 0 or (y+dy) < 0 or (x+dx) >= round(WINDOW_WIDTH / BLOCK_SIZE) or (y+dy) >= round(WINDOW_HEIGHT / BLOCK_SIZE):
                continue
            if cells[x+dx][y+dy] == ALIVE:
                numbers_of_neighbours += 1

        if life == DEAD and numbers_of_neighbours == 3:
            new_cells[x][y] = ALIVE
        if life == ALIVE and numbers_of_neighbours < 2:
            new_cells[x][y] = DEAD
        if life == ALIVE and numbers_of_neighbours > 3:
            new_cells[x][y] = DEAD



    return new_cells

def main():
    print("-------------------- Lauching Game of Life --------------------")
    draw = Draw()
    CLOCK = pygame.time.Clock()
    cells = np.zeros((round(WINDOW_WIDTH / BLOCK_SIZE), round(WINDOW_HEIGHT / BLOCK_SIZE)))
    print()

    print("-------------------- Set Initial Board --------------------")
    print("Press Down Key to continue")
    #Set initial board
    initial_board_done = False
    while not initial_board_done:
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            x = math.floor(pos[0] / BLOCK_SIZE)
            y = math.floor(pos[1] / BLOCK_SIZE)
            if x == round(WINDOW_WIDTH / BLOCK_SIZE):
                x -= 1
            if y == round(WINDOW_HEIGHT / BLOCK_SIZE):
                y -= 1
            cells[x][y] = ALIVE
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                initial_board_done = True
        draw.draw_board(cells)
        pygame.display.update()
        CLOCK.tick(1000)

    print("-------------------- Starting Game of Life --------------------")
    print("Press Down Key to continue")

    #Running Game of Life
    while True:
        CLOCK.tick(10)
        cells = update_cells(cells)
        draw.draw_board(cells)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == "__main__":
    main()