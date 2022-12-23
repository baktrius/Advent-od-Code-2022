from helper import stdin
import numpy as np
import re


if __name__ == "__main__":
    lines = stdin.read().split('\n')
    w = 0
    h = 0
    for line in lines:
        size = len(line)
        if not size:
            break
        h += 1
        w = max(w, size)

    area = np.zeros((h, w), dtype=np.int32)
    for i in range(h):
        l = list(map(lambda x: {' ': 0, '.': 1, '#': 2}[x], lines[i]))
        a = np.array(l, dtype=np.int32)
        a.resize((w))
        area[i] = a

    cmds = lines[h+1]

    print(area)
    cmds = re.split("(R|L)", cmds)
    pos = np.array((0, list(area[0]).index(1)), dtype=np.int32)
    dirs = [np.array([0, 1]), np.array([1, 0]),
            np.array([0, -1]), np.array([-1, 0])]
    curr_dir = 0
    for cmd in cmds:
        if cmd == 'L':
            curr_dir = (curr_dir + 3) % 4
        elif cmd == 'R':
            curr_dir = (curr_dir + 1) % 4
        else:
            steps = int(cmd)
            for _ in range(steps):
                new_pos = np.mod(pos + dirs[curr_dir], (h, w))
                while area[new_pos[0], new_pos[1]] == 0:
                    new_pos = np.mod(new_pos + dirs[curr_dir], (h, w))
                if area[new_pos[0], new_pos[1]] == 2:
                    break
                pos = new_pos
    pos += 1
    print(pos[0] * 1000 + pos[1] * 4 + curr_dir)
