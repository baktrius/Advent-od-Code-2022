from helper import stdin
import numpy as np


if __name__ == "__main__":
    res = 0
    elves_num = 0
    elves = set()
    for y, line in enumerate(stdin):
        for x, char in enumerate(line):
            if char == '#':
                elves.add((x, y))
                elves_num += 1

    dirs = np.array([
        [-1, -1],
        [0, -1],
        [1, -1],
        [1, 0],
        [1, 1],
        [0, 1],
        [-1, 1],
        [-1, 0]
    ], dtype=np.int32)

    order = np.array([
        [0, 1, 2],
        [4, 5, 6],
        [6, 7, 0],
        [2, 3, 4]
    ], dtype=np.int32)

    for rund in range(10):
        proposal = set()

        def print_elves():
            for y in range(-5, 20):
                for x in range(-5, 20):
                    if (x, y) in elves:
                        print('#', end='')
                    elif (x, y, 0) in proposal:
                        print('0', end='')
                    elif (x, y, 1) in proposal:
                        print('1', end='')
                    elif (x, y, 2) in proposal:
                        print('2', end='')
                    elif (x, y, 3) in proposal:
                        print('3', end='')
                    else:
                        print('.', end='')
                print()

        for elf in elves:
            if not any([(tuple(np.array(elf, dtype=np.int32) + dr) in elves) for dr in dirs]):
                continue
            for i in range(4):
                dirs_to_check = dirs[order[(rund + i) % 4]]
                if not any([(tuple(np.array(elf, dtype=np.int32) + dr) in elves) for dr in dirs_to_check]):
                    proposal.add(
                        (*(np.array(elf, dtype=np.int32) + dirs_to_check[1]), i))
                    break

        for elf in elves:
            if not any([(tuple(np.array(elf, dtype=np.int32) + dr) in elves) for dr in dirs]):
                continue
            for i in range(4):
                dirs_to_check = dirs[order[(rund + i) % 4]]
                if not any([(tuple(np.array(elf, dtype=np.int32) + dr) in elves) for dr in dirs_to_check]):
                    for j in range(4):
                        if i != j:
                            proposal.discard(
                                (*(np.array(elf, dtype=np.int32) + dirs_to_check[1]), j))
                    break

        print(rund)
        print_elves()

        for elf in elves:
            for i in range(4):
                dirs_to_check = dirs[order[(rund + i) % 4]]
                if (*(np.array(elf, dtype=np.int32) + dirs_to_check[1]), i) in proposal:
                    elves.remove(elf)
                    elves.add(tuple(elf + dirs_to_check[1]))
                    break
    xs, ys = zip(*elves)
    res = (max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1) - elves_num
    print(res)
