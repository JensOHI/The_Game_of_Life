WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLOCK_SIZE = 15
global SCREEN, CLOCK

ALIVE = 1
DEAD = 0

neighbours = [
    [-1,-1],
    [0,-1],
    [1,-1],
    [1,0],
    [1,1],
    [0,1],
    [-1,1],
    [-1,0],
]