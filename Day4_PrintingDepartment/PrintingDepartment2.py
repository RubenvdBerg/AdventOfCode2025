import numpy as np

def calculate_solution(input):
    data = np.array([[char for char in row] for row in input.splitlines()])
    return calculate_rolls(data)

def calculate_rolls(grid):
    original_count = np.sum(grid == "@")
    while True:
        start_grid = grid.copy()
        for h,w in np.argwhere(grid == "@"):
            if get_neighbours(grid, h, w) < 4:
                grid[h][w] = "."
        if np.array_equal(grid, start_grid):
            break
    return original_count-np.sum(grid == "@")

def get_neighbours(grid, y, x):
    max_y, max_x = grid.shape

    def limit_grid(val, limit):
        return [min(max(val+i, 0), limit) for i in [-1,2]]

    y0, y1 = limit_grid(y, max_y)
    x0, x1 = limit_grid(x, max_x)
    return np.count_nonzero(grid[y0:y1, x0:x1] == "@") - 1

if __name__ == '__main__':
    with open("input.txt") as file:
        print(calculate_solution(file.read()))