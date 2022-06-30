#Contains the grids used by the program
from cells import *
import pygame as pg

class Grid:
    def __init__(self, columns, rows):
        self.cols = columns
        self.rows = rows

        self.grid = [[Cell(x, y, self) for x in range(self.cols)] for y in range(self.rows)]

        self.configure_cells()

    def reset(self):
        self.grid = [[Cell(x, y, self) for x in range(self.cols)] for y in range(self.rows)]

    def configure_cells(self):
        for cell in self.list():
            cell.get_neighbors()

    def list(self):
        out = []
        for row in self.grid:
            for cell in row:
                out.append(cell)
        return out

    def __getitem__(self, index):
        return self.grid[index[1]][index[0]]
    def __setitem__(self, index, other):
        self.grid[index[1]][index[0]] = other

    def possible_directions(self, x, y): #Returns available directions for given position
        if x == 0 and y == 0:
            return[1, 2]
        elif x == 0 and y == self.rows - 1:
            return[0, 1]
        elif x == self.cols - 1 and y == 0:
            return[2, 3]
        elif x == self.cols - 1 and y == self.rows - 1:
            return [0, 3]
        elif x == 0:
            return [0, 1, 2]
        elif y == 0:
            return [1, 2, 3]
        elif x == self.cols - 1:
            return [0, 2, 3]
        elif y == self.rows - 1:
            return [0, 1, 3]
        else:
            return [0, 1, 2, 3]

    def get_cell_from_direction(self, cell, d):
        if d == 0:
            return self.grid[cell.y - 1][cell.x]
        elif d == 1:
            return self.grid[cell.y][cell.x + 1]
        elif d == 2:
            return self.grid[cell.y + 1][cell.x]
        elif d == 3:
            return self.grid[cell.y][cell.x - 1]

    def get_neighbor_cells(self, cell):
        d = self.possible_directions(cell.x, cell.y)
        cell_directions = [None, None, None, None]
        for direction in d:
            cell_directions[direction] = self.get_cell_from_direction(cell, direction)
        return cell_directions

    def draw(self, surface, size):
        for cell in self.list():
            pg.draw.line(surface, [0, 0, 0], [cell.x * size, cell.y * size], [cell.x * size + size, cell.y * size], 1) if not cell.is_linked(0) else False
            pg.draw.line(surface, [0, 0, 0], [cell.x * size + size, cell.y * size], [cell.x * size + size, cell.y * size + size], 1) if not cell.is_linked(1) else False

        #Bottom line
        pg.draw.line(surface, [0, 0, 0], [0, self.rows * size], [self.cols * size, self.rows * size], 1)

