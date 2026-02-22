import re
import numpy as np

# maybe a slightly scuffed way to do this...
filters = [
    np.array(["X", "M", "A", "S"])[np.newaxis, :],
    np.array(["S", "A", "M", "X"])[np.newaxis, :],
    np.array([["X"], ["M"], ["A"], ["S"]]),
    np.array([["S"], ["A"], ["M"], ["X"]]),
    np.array(
        [
            ["X", "O", "O", "O"],
            ["O", "M", "O", "O"],
            ["O", "O", "A", "O"],
            ["O", "O", "O", "S"],
        ]
    ),
    np.array(
        [
            ["S", "O", "O", "O"],
            ["O", "A", "O", "O"],
            ["O", "O", "M", "O"],
            ["O", "O", "O", "X"],
        ]
    ),
    np.array(
        [
            ["O", "O", "O", "S"],
            ["O", "O", "A", "O"],
            ["O", "M", "O", "O"],
            ["X", "O", "O", "O"],
        ]
    ),
    np.array(
        [
            ["O", "O", "O", "X"],
            ["O", "O", "M", "O"],
            ["O", "A", "O", "O"],
            ["S", "O", "O", "O"],
        ]
    ),
]
f = open("day4.txt", "r")
grid = []
for line in f.readlines():
    grid.append([char for char in line if char != "\n"])
f.close()
grid = np.array(grid)
gy, gx = grid.shape
print([f.shape for f in filters])


total = 0
for f in filters:
    fy, fx = f.shape
    for i in range(0, gy - fy + 1):
        for j in range(0, gx - fx + 1):
            sample = grid[i : i + fy, j : j + fx]
            if (sample == f).sum() == 4:
                total += 1
print(total)
