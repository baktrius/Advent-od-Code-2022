from helper import stdin
import re
import numpy as np

neighbors = np.array([
    [-1, 0, 0, 0, 0, 1],
    [0, -1, 0, 0, 1, 0],
    [0, 0, -1, 1, 0, 0]
], dtype=np.int32)

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
    for cube in cubes:
        pos = cube - mins + 1
        space[tuple(pos)] = 1
    visited = np.zeros_like(space)

    poss = [np.zeros((3), dtype=np.int32)]
    res = 0
    while poss:
        pos = poss.pop()
        if any(pos < 0) or any(pos >= sizes) or visited[tuple(pos)]:
            continue
        if space[tuple(pos)] == 1:
            res += 1
            continue
        visited[tuple(pos)] = 1
        poss.extend(neighbors.T + pos)

    print(res)
