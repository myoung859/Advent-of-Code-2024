import re
import numpy as np

xmas = np.array([["S", "O", "S"], ["O", "A", "O"], ["M", "O", "M"]])

filters = [np.rot90(xmas, i) for i in range(0, 4)]

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
            if (sample == f).sum() == 5:
                total += 1
print(total)
