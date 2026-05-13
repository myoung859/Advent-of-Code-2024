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
    # print(a)
    y, x = np.where(grid == a)
    coords = [(int(i), int(j)) for i, j in zip(y, x)]
    # print(coords)
    for c1, c2 in itertools.combinations(coords, 2):
        test_nodes = [
            # (c1[0] + c2[0], c1[1] + c2[1]),
            (2 * c1[0] - c2[0], 2 * c1[1] - c2[1]),
            (2 * c2[0] - c1[0], 2 * c2[1] - c1[1]),
        ]
        for t in test_nodes:
            if 0 <= t[0] < gy and 0 <= t[1] < gx:
                antinodes.append(t)
    # print(antinodes)
print(set(antinodes), len(set(antinodes)))
