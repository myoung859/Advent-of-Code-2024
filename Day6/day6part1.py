import numpy as np

f = open("day6.txt", "r")
grid = []
for line in f.readlines():
    grid.append([char for char in line if char != "\n"])
f.close()
grid = np.array(grid)
gy, gx = grid.shape

pos_y, pos_x = np.where(grid == "^")
pos_y = pos_y[0]
pos_x = pos_x[0]
while 0 <= pos_y < gy - 1:

    if grid[pos_y - 1, pos_x] == "#":
        grid = np.rot90(grid)
        pos_y, pos_x = np.where(grid == "^")
        pos_y = pos_y[0]
        pos_x = pos_x[0]
    else:
        grid[pos_y - 1, pos_x] = "^"
        grid[pos_y, pos_x] = "x"
        pos_y = pos_y - 1
print(np.sum(grid == "x"))
