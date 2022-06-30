#A main file that acts as an interface for the maze generator
import tkinter as tk
import pygame as pg
from grids import Grid
from algorithms import BinaryTree
from threading import Thread

MAZE_TYPES = ["Rectangle", "Circular"]
MAZE_ALGORITHMS = ["Binary Tree", "Aldous-Broder"]
PATHFINDERS = ["None", "Dijkstra"]

ALGORITHMS = {"Binary Tree" : BinaryTree}

CELL_SIZE = 50

def GenerateMazeCallback(type, algorithm, path, args):
    if type == MAZE_TYPES[0]:
        grid = Grid(int(args["SIZEX"]), int(args["SIZEY"]))
        grid[1, 1].link(2)
        if args["SHOW"] == 0:
            show_maze_instant(grid, ALGORITHMS[algorithm])

def show_maze_instant(grid, algorithm):
    pg.init()
    win_size = (CELL_SIZE * grid.cols + 1, CELL_SIZE * grid.rows + 1)

    surface = pg.display.set_mode(win_size)
    pg.display.set_caption("Maze")

    surface.fill([255, 255, 255])
    algorithm(grid)
    grid.draw(surface, CELL_SIZE)

    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    win = tk.Tk()
    win.title("Maze Generator")
    win.geometry("420x200")
    win.resizable(False, False)

    #Main body
    maze_type_var = tk.StringVar(win)
    maze_type_var.set(MAZE_TYPES[0])
    maze_type = tk.OptionMenu(win, maze_type_var, *MAZE_TYPES,)
    maze_type.config(width = 10)
    maze_type.grid(column=0, row=0, padx=3)

    maze_algorithm_var = tk.StringVar(win)
    maze_algorithm_var.set(MAZE_ALGORITHMS[0])
    maze_algorithm = tk.OptionMenu(win, maze_algorithm_var, *MAZE_ALGORITHMS,)
    maze_algorithm.config(width = 10)
    maze_algorithm.grid(column=1, row=0, padx=3) 

    pathfinder_var = tk.StringVar(win)
    pathfinder_var.set(PATHFINDERS[0])
    pathfinder = tk.OptionMenu(win, pathfinder_var, *PATHFINDERS,)
    pathfinder.config(width = 10)
    pathfinder.grid(column=2, row=0, padx=3) 


    
    tk.Label(win, text="X: ").place(x=5, y=60)
    size_x = tk.Entry(win, font=('Arial 11'))
    size_x.config(width=4)
    size_x.insert(tk.END, 8)
    size_x.place(x=25, y=60)

    tk.Label(win, text = "Y: ").place(x=5, y=85)
    size_y = tk.Entry(win, font = ("Arial 11"))
    size_y.config(width = 4)
    size_y.insert(tk.END, 8)
    size_y.place(x=25, y=85)

    show_generation_var = tk.IntVar()
    show_generation = tk.Checkbutton(win, text="Show Generation", variable=show_generation_var)
    show_generation.grid(column=1, row=3, pady=10) 

    build = tk.Button(win, text="Generate", command = lambda : GenerateMazeCallback(maze_type_var.get(), maze_algorithm_var.get(), pathfinder_var, {"SHOW" : show_generation_var.get(), "SIZEX" : size_x.get(), "SIZEY" : size_y.get()})) 
    build.grid(column=1, row=5, pady=40)

    win.mainloop()