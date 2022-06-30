import random

def BinaryTree(grid):
    for y in range(grid.rows):
        for x in range(grid.cols):
            if y == grid.rows - 1 and x == grid.cols - 1:
                continue
            elif y == grid.rows - 1:
                d = 1
            elif x == grid.rows - 1:
                d = 2
            else:
                d = random.choice([1, 2])
            grid[x, y].link(d)
