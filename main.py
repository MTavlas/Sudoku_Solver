import numpy as np
import itertools as ite
from time import time

sudoku_maze = np.array([[0, 0, 4, 0, 0, 0, 0, 6, 7],
                        [3, 0, 0, 4, 7, 0, 0, 0, 5],
                        [1, 5, 0, 8, 2, 0, 0, 0, 3],
                        [0, 0, 6, 0, 0, 0, 0, 3, 1],
                        [8, 0, 2, 1, 0, 5, 6, 0, 4],
                        [4, 1, 0, 0, 0, 0, 9, 0, 0],
                        [7, 0, 0, 0, 8, 0, 0, 4, 6],
                        [6, 0, 0, 0, 1, 2, 0, 0, 0],
                        [9, 3, 0, 0, 0, 0, 7, 1, 0]])

start_time = time()


class Point:
    def __init__(self, coords, sudoku):

        self.sudoku = sudoku
        self.coords = coords
        self.value = self.sudoku[coords]
        self.y, self.x = self.coords

        self.possible_values = list(range(1, 10))

        self.subgroup_neighbors, self.h_neighbors, self.v_neighbors = get_neighbors(self.coords)

        self.subgroup_neighbors_values = [self.sudoku[x] for x in self.subgroup_neighbors]
        self.h_neighbors_values = [self.sudoku[x] for x in self.h_neighbors]
        self.v_neighbors_values = [self.sudoku[x] for x in self.v_neighbors]
        self.joined_list = [*self.subgroup_neighbors_values, *self.h_neighbors_values, *self.v_neighbors_values]

    def calculate(self):

        if self.sudoku[self.coords] != 0:
            self.value = self.sudoku[self.coords]
        else:
            for item in self.joined_list:
                if item in self.possible_values:
                    self.possible_values.remove(item)
                    if self.possible_values.__len__() == 1:
                        self.value = self.possible_values[0]

        return self.value


def subgroup(n):
    if n < 3:
        return [0, 1, 2]
    if n < 6:
        return [3, 4, 5]
    else:
        return [6, 7, 8]


def get_neighbors(point):
    my_y, my_x = point
    subgroup_neighbors = list(ite.product(subgroup(my_y), subgroup(my_x)))
    h_neighbors = []
    v_neighbors = []
    for i in range(9):
        h_neighbors.append((my_y, i))
        v_neighbors.append((i, my_x))
    return subgroup_neighbors, h_neighbors, v_neighbors


all_coords = list(ite.product(range(9), range(9)))

while 0 in sudoku_maze:
    for coords in all_coords:
        sudoku_maze[coords] = Point(coords, sudoku_maze).calculate()

print(sudoku_maze)
print(f"It took me {time() - start_time} seconds to solve!")
