import numpy as np
import copy
import tqdm


def loop_check(grid: np.ndarray):
    # returns True if there's an infinite loop
    num_rot = 0
    max_rot = 4 * np.count_nonzero(
        grid == "#"
    )  # i.e. we hit every obstacle at least 4 times
    # needed for back-and-forth loops
    # print("stata")
    gy, gx = grid.shape
    pos_y, pos_x = np.where(grid == "^")
    pos_y = pos_y[0]
    pos_x = pos_x[0]
    while 0 <= pos_y < gy - 1:
        if num_rot > max_rot:
            return True
        # print(num_rot)
        # print(grid[pos_y, pos_x])
        if str(grid[pos_y - 1, pos_x]).isdigit():
            # print(int(grid[pos_y - 1, pos_x]) - num_rot)
            if abs(num_rot - int(grid[pos_y - 1, pos_x])) % 4 == 0:
                # print(num_rot, grid[pos_y - 1, pos_x])
                return True
        if grid[pos_y - 1, pos_x] == "#":
            grid = np.rot90(grid)
            num_rot += 1
            pos_y, pos_x = np.where(grid == "^")
            pos_y = pos_y[0]
            pos_x = pos_x[0]
            # print(pos_y, pos_x)
        else:
            grid[pos_y - 1, pos_x] = "^"
            grid[pos_y, pos_x] = str(num_rot)
            pos_y = pos_y - 1
        # print(grid)
        # a = input()
    return False


f = open("day6.txt", "r")
grid = []
for line in f.readlines():
    grid.append([char for char in line if char != "\n"])
f.close()
grid = np.array(grid, dtype=object)
# print(loop_check(grid))
# np.savetxt("grid_test.txt", grid, fmt="%s")
total_loops = 0
for idx, x in tqdm.tqdm(np.ndenumerate(grid), total=grid.size):
    if x == ".":
        new_grid = copy.deepcopy(grid)
        new_grid[idx] = "#"
        if loop_check(new_grid):
            total_loops += 1
print(total_loops)
