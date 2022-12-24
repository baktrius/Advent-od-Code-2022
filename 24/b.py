from helper import stdin
import numpy as np


if __name__ == "__main__":
    lines = stdin.read().split('\n')
    lines = lines[1:-2]
    lines = list(map(lambda line: line[1:-1], lines))
    h = len(lines)
    w = len(lines[0])
    area = np.array([[{'.': 0, '>': 1, 'v': 2, '<': 3, '^': 4}[char]
                    for char in line] for line in lines], dtype=np.int32)
    winds = [
        np.array(np.nonzero(area == 1), dtype=np.int32),
        np.array(np.nonzero(area == 2), dtype=np.int32),
        np.array(np.nonzero(area == 3), dtype=np.int32),
        np.array(np.nonzero(area == 4), dtype=np.int32)
    ]
    neighbors = [
        (0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)
    ]

    def solve(start, end):
        possible = set()
        for i in range(100000):
            winds[0][1] = np.remainder(winds[0][1] + 1, w)
            winds[1][0] = np.remainder(winds[1][0] + 1, h)
            winds[2][1] = np.remainder(winds[2][1] + (w - 1), w)
            winds[3][0] = np.remainder(winds[3][0] + (h - 1), h)
            if end in possible:
                return i + 1

            occ = np.zeros_like(area, dtype=np.int32)
            for wind in winds:
                occ[wind[0], wind[1]] = 1
            next_possible = set()
            for pos_y, pos_x in possible:
                for n_y, n_x in neighbors:
                    ty = pos_y + n_y
                    tx = pos_x + n_x
                    if ty >= 0 and tx >= 0 and ty < h and tx < w and occ[ty, tx] == 0:
                        next_possible.add((ty, tx))

            if occ[start] == 0:
                next_possible.add(start)
            possible = next_possible

    print(solve((0, 0), (h-1, w-1)),
          solve((h-1, w-1), (0, 0)), solve((0, 0), (h-1, w-1)))
