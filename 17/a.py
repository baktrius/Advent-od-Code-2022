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

rocks_num = 2022

if __name__ == "__main__":
    movements = itertools.cycle(stdin.readline()[:-1])
    cave = np.zeros((4 * 2022 + 10, 9), dtype=np.int32)
    cave[0, :] = 2
    cave[:, 0] = 1
    cave[:, -1] = 1
    max_y = 1

    def get_cave_part(rock, x, y) -> np.array:
        return cave[rock[0] + y, rock[1] + x]

    def print_cave():
        for line in reversed(cave[:max_y, :]):
            print("".join(map(lambda x: ['.', '|', '#'][x], line)))

    for _, rock in zip(range(rocks_num), rocks):
        y = max_y + 3
        x = 3
        for move in movements:
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
                # print_cave()
                # print()
                break
    print(max_y - 1)
