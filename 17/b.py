from helper import stdin
import numpy as np
import itertools

rocks = itertools.cycle([
    np.array([(0, 0, 0, 0), (0, 1, 2, 3)]),
    np.array([(0, 1, 1, 1, 2), (1, 0, 1, 2, 1)]),
    np.array([(0, 0, 0, 1, 2), (0, 1, 2, 2, 2)]),
    np.array([(0, 1, 2, 3), (0, 0, 0, 0)]),
    np.array([(0, 0, 1, 1), (0, 1, 0, 1)]),
])

rocks_num = 1000000000000

if __name__ == "__main__":
    line = stdin.readline()[:-1]
    movements = itertools.cycle(enumerate(line))
    cave = np.zeros((4 * 10000 + 10, 9), dtype=np.int32)
    cave[0, :] = 2
    cave[:, 0] = 1
    cave[:, -1] = 1
    max_y = 1

    def get_cave_part(rock, x, y) -> np.array:
        return cave[rock[0] + y, rock[1] + x]

    def print_cave():
        for line in reversed(cave[:max_y, :]):
            print("".join(map(lambda x: ['.', '|', '#'][x], line)))

    seen_configuration = dict()
    maxs_y = []

    def next_rock():
        global max_y
        rock = next(rocks)
        y = max_y + 3
        x = 3
        for i2, move in movements:
            if move == '<':
                if np.max(get_cave_part(rock, x - 1, y)) == 0:
                    x -= 1
            elif move == '>':
                if np.max(get_cave_part(rock, x + 1, y)) == 0:
                    x += 1
            else:
                print(ord(move))
                assert False
            if np.max(get_cave_part(rock, x, y - 1)) == 0:
                y -= 1
            else:
                cave[rock[0] + y, rock[1] + x] = 2
                max_y = max(max_y, *(rock[0] + y + 1))
                return x, i2

    for i in range(rocks_num):
        x, i2 = next_rock()
        maxs_y.append(max_y)
        el = (i % 5, i2, x)
        if el in seen_configuration:
            prev_i = seen_configuration[el]
            # cycle detection code is a little bugged
            # but for my input stabilizes after 3000 rock falls
            # hence such a strange if condition
            if i > 3000 and all(maxs_y[prev_i] < np.array(maxs_y[prev_i+1:i+1])):
                prev_max_y = maxs_y[prev_i]
                cycle_len = i - prev_i
                cycle_h = max_y - prev_max_y
                left_rocks = rocks_num - i - 1
                left_cycles = left_rocks // cycle_len
                rem_cycles = left_rocks % cycle_len
                print(max_y + left_cycles * cycle_h +
                      maxs_y[prev_i + rem_cycles] - prev_max_y -
                      1, max_y, left_cycles * cycle_h,
                      maxs_y[prev_i + rem_cycles] - prev_max_y, i, cycle_len)
                break
        seen_configuration[el] = i
    print(max_y - 1)
