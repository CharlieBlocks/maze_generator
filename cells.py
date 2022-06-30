#Contains cell and cell subclasses
class Cell:
    def __init__(self, x, y, grid):
        self.x = x
        self.y = y 
        self.parent = grid

        self.up = None 
        self.down = None 
        self.left = None 
        self.right = None 

        self.link_directions = []

    def get_neighbors(self):
        cells = self.parent.get_neighbor_cells(self)
        self.up = cells[0]
        self.down = cells[2]
        self.left = cells[3]
        self.right = cells[1]

    def link(self, *args):
        if len(args) > 1:
            raise TypeError(f"PolarCell.link() takes 1 positional argument but {len(args)} were given.")
        if not isinstance(args[0], (Cell, int)):
            raise TypeError("Invalid argument passed to PolarCell.link().")

        if isinstance(args[0], Cell):
            linked_cell = args[0]
            if not self.is_neighbor(linked_cell):
                raise Exception("Invalid cell to link to.")

            direction = self.get_cell_direction(linked_cell)

            if direction == 2:
                linked_cell.link(0)
            elif direction == 3:
                linked_cell.link(1)
            else:
                self.link_directions.append(direction)

        elif isinstance(args[0], int):
            if args[0] == 2:
                linked_cell = self.parent.get_cell_from_direction(self, args[0])
                linked_cell.link(0)
            elif args[0] == 3:
                linked_cell = self.parent.get_cell_from_direction(self, args[0])
                linked_cell.link(1)
            else:
                self.link_directions.append(args[0])

    def is_linked(self, direction):
        if direction in self.link_directions:
            return True 
        return False

    def is_neighbor(self, cell):
        x_delta = cell.col - self.col
        y_delta = cell.row - self.row
        x_delta = abs(x_delta)
        y_delta = abs(y_delta)
        if x_delta == y_delta:
            return False
        if x_delta > 1:
            return False 
        if y_delta > 1:
            return False
        return True

    def get_cell_direction(self, cell):
        x_delta = cell.col - self.col
        y_delta = cell.row - self.row

        if x_delta == 1:
            return 1
        if x_delta == -1:
            return 3
        if y_delta == 1:
            return 0
        if y_delta == -1:
            return 2

