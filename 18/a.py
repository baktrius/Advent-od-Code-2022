from helper import stdin
import re
import numpy as np

neighbours = [
    [-1, 0, 0, 0, 0, 1],
    [0, -1, 0, 0, 1, 0],
    [0, 0, -1, 1, 0, 0]
]

if __name__ == "__main__":
    cubes = []
    for line in stdin:
        if (match := re.match("(\\d+),(\\d+),(\\d+)", line)):
            cubes.append(np.array(list(map(int, match.groups()))))
        elif line == "":
            pass
        else:
            assert False
    coordinates = list(zip(*cubes))
    maxs = np.array(list(map(max, coordinates)))
    mins = np.array(list(map(min, coordinates)))
    sizes = maxs - mins + 3
    assert min(mins) >= 0
    space = np.zeros(sizes)
    res = 0
    for cube in cubes:
        pos = cube - mins + 1
        n_pos = neighbours + np.expand_dims(pos, axis=1)
        res += 6 - 2 * np.sum(space[n_pos[0], n_pos[1], n_pos[2]])
        space[tuple(pos)] = 1
    print(res)
