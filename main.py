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
            x_ = x
            y_ = y
            dx = neighbour[0]
            dy = neighbour[1]
            if (x+dx) < 0:
                x_ = round(WINDOW_WIDTH / BLOCK_SIZE) - 1
            if (y+dy) < 0:
                y_ = round(WINDOW_HEIGHT / BLOCK_SIZE)
            if (x+dx) >= round(WINDOW_WIDTH / BLOCK_SIZE) - 1:
                x_ = -1
            if (y+dy) >= round(WINDOW_HEIGHT / BLOCK_SIZE):
                y_ = -1
            if cells[x_+dx][y_+dy] == ALIVE:
                numbers_of_neighbours += 1

        if life == DEAD and numbers_of_neighbours == 3:
            new_cells[x][y] = ALIVE
        if life == ALIVE and numbers_of_neighbours < 2:
            new_cells[x][y] = DEAD
        if life == ALIVE and numbers_of_neighbours > 3:
            new_cells[x][y] = DEAD



    return new_cells


def get_mouse_pos():
    pos = pygame.mouse.get_pos()
    x = math.floor(pos[0] / BLOCK_SIZE)
    y = math.floor(pos[1] / BLOCK_SIZE)
    if x == round(WINDOW_WIDTH / BLOCK_SIZE):
        x -= 1
    if y == round(WINDOW_HEIGHT / BLOCK_SIZE):
        y -= 1
    return x, y


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
            x, y = get_mouse_pos()
            cells[x][y] = ALIVE
        if pygame.mouse.get_pressed()[2]:
            x, y = get_mouse_pos()
            cells[x][y] = DEAD
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                initial_board_done = True
        draw.draw_board(cells, draw_grid=True)
        pygame.display.update()
        CLOCK.tick(1000)

    print("-------------------- Starting Game of Life --------------------")
    print("Press Down Key to continue")

    #Running Game of Life
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()

        cells = update_cells(cells)
        draw.draw_board(cells)
        pygame.display.update()
        CLOCK.tick(10)

if __name__ == "__main__":
    main()
