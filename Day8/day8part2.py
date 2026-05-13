import numpy as np
import itertools

f = open("day8.txt", "r")
grid = []
for line in f.readlines():
    grid.append([char for char in line if char != "\n"])
f.close()
grid = np.array(grid)
gy, gx = grid.shape

antennae = [str(i) for i in np.unique(grid) if i != "."]
antinodes = []
for a in antennae:
    y, x = np.where(grid == a)
    coords = [(int(i), int(j)) for i, j in zip(y, x)]
    for c1, c2 in itertools.combinations(coords, 2):
        delta = (c1[0] - c2[0], c1[1] - c2[1])
        for i in range(-1, -gx - 1, -1):
            p = c1[0] + i * delta[0], c1[1] + i * delta[1]
            if 0 <= p[0] < gy and 0 <= p[1] < gx:
                antinodes.append(p)
            else:
                break
        for i in range(0, gx + 1, 1):
            p = c1[0] + i * delta[0], c1[1] + i * delta[1]
            if 0 <= p[0] < gy and 0 <= p[1] < gx:
                antinodes.append(p)
            else:
                break
        # print(antinodes)
print(set(antinodes), len(set(antinodes)))