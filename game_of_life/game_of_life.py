# File:  game_of_life.py
# The following program designs and implements a flexible game invented by John
# Conway in 1970. It is a zero player game involving a grid of a certain size
# and an initial configuration. The program allows the player to configure the
# size of the grid and the initial configuration as input and the game
# continues to play until intervened by the player or when the game reaches a
# steady state (sometimes). The following rules are applied to the initial
# configuration for the run of the game.

# The rules of the game are simple, and describe the evolution of the
# grid:

# 1. Birth: a cell that is dead at time t will be alive at time t + 1
#    if exactly 3 of its eight neighbors were alive at time t.
#
# 2.  Death: a cell can die by:
#  a) Overcrowding: if a cell is alive at time t + 1 and 4 or more of
#     its neighbors are also alive at time t, the cell will be dead at
#     time t + 1.
#  b) Exposure: If a live cell at time t has only 1 live neighbor or no
#     live neighbors, it will be dead at time t + 1.
#
# 3. Survival: a cell survives from time t to time t + 1 if and only
#   if 2 or 3 of its neighbors are alive at time t.

# imports
import argparse

# Class definition:
class Grid(object):
    def __init__(self, grid_size):
        pass

    def set_initial_configuration(self):
        pass

    def start_play(self):
        pass

    def stop_play(self):
        pass

    def pause_play(self):
        pass

    def resume_play(self):
        pass


class Cell(object):
    def __init__(self, cell_size, row, column):
        self.row = row
        self.column = column
        self.active = False

    def get_neighbours(self):
        pass

    def activate(self):
        pass

    def kill(self):
        pass



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--size", type=int, default=120, help="Size of the square grid")
    parser.add_argument("-i", "--input_file", type=str, default="center", help="file with pattern for initial configuration")

    parser.parse_args()

    grid_size = parser.size
    in_file = parser.input_file

    grid = Grid(grid_size)

    grid.get_initial_configuration()


