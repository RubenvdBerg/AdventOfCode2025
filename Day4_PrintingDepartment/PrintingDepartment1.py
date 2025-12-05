import numpy as np

def calculate_solution1(input):
    data = np.array([[char for char in row] for row in input.splitlines()])
    return sum(calculate_rolls(data))

def calculate_rolls(grid):
    height, width  = grid.shape
    for h in range(height):
        for w in range(width):
            value = grid[h][w]
            if value == "@":
                if sum(get_neighbours(grid, h, w)) < 4:
                    yield 1

def get_neighbours(grid, y, x):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            y_i = y + i
            x_j = x + j
            if y_i >= 0 and x_j >= 0 and not (i == 0 and j == 0):
                try:
                    if grid[y_i][x_j] == "@":
                        yield 1
                except IndexError:
                    pass


if __name__ == '__main__':
    with open("input.txt") as file:
        print(calculate_solution1(file.read()))