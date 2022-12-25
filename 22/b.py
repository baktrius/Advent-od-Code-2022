# Not finished!

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
        a.resize((w), refcheck=False)
        area[i] = a

    cmds = lines[h+1]
    stride = 50

    sides = area[::stride, ::stride] != 0
    assert np.count_nonzero(sides) == 6
    ys, xs = np.nonzero(sides)
    x = xs[0] + 1
    y = ys[0]
    pxs = [x - 1, x]
    pys = [y, y]
    dirs = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]
    first_dir = 0
    edge_dirs = [first_dir]
    rel_dirs = [1]

    def get(arr: np.array, x, y):
        if x < 0 or y < 0 or y >= arr.shape[0] or x >= arr.shape[1]:
            return 0
        return arr[y, x]

    def is_on_edge(a, x, y):
        val = get(a, x-1, y-1) + get(a, x-1, y) + get(a, x, y-1) + get(a, x, y)
        return val > 0 and val < 4

    while x != pxs[0] or y != pys[0]:
        first_dir = (first_dir + 3) % 4
        for i in range(3):
            dy, dx = dirs[first_dir]
            if is_on_edge(sides, x + dx, y + dy):
                x += dx
                y += dy
                pxs.append(x)
                pys.append(y)
                edge_dirs.append(first_dir)
                rel_dirs.append(i - 1)
                break
            first_dir = (first_dir + 1) % 4

    pp = list(zip(pxs, pys))
    edges = list(zip(pp, pp[1:]))
    edges_mapping = dict()
    while edges:
        if rel_dirs[1] == -1:
            dir1 = edge_dirs.pop(0)
            dir2 = edge_dirs.pop(0)
            dr = (dir1 - dir2 + 4) % 4
            edges_mapping[edges[0]] = (edges[1], (6 - dr) % 4)
            edges_mapping[edges[1]] = (edges[0], (2 + dr) % 4)
            edges.pop(0)
            edges.pop(0)
            try:
                s = rel_dirs.pop(0) + rel_dirs.pop(0) + rel_dirs.pop(0) - 1
                rel_dirs.insert(0, s)
            except IndexError:
                pass
        else:
            edges.append(edges.pop(0))
            rel_dirs.append(rel_dirs.pop(0))
            edge_dirs.append(edge_dirs.pop(0))
    # pprint(edges_mapping)

    cmds = re.split("(R|L)", cmds)
    pos = np.array((0, list(area[0]).index(1)), dtype=np.int32)
    dirs = [np.array([0, 1]), np.array([1, 0]),
            np.array([0, -1]), np.array([-1, 0])]

    helper = np.array([
        [[0, 0], [1, 0]],
        [[0, 1], [0, 0]],
        [[1, 1], [0, 1]],
        [[1, 0], [1, 1]]
    ], dtype=np.int32)
    compensation = np.array([
        [0, 0],
        [0, -1],
        [-1, -1],
        [-1, 0]
    ], dtype=np.int32)
    curr_dir = 0
    for cmd in cmds:
        if cmd == 'L':
            curr_dir = (curr_dir + 3) % 4
        elif cmd == 'R':
            curr_dir = (curr_dir + 1) % 4
        else:
            steps = int(cmd)
            for _ in range(steps):
                new_pos = pos + dirs[curr_dir]
                new_dir = curr_dir
                if get(area, new_pos[1], new_pos[0]) == 0:
                    n = np.sum(np.mod(np.mod(new_pos, stride), stride - 1))
                    if new_dir == 0 or new_dir == 3:
                        n = stride - n - 1
                    es, ee = helper[curr_dir] + new_pos // stride
                    edge = (tuple(reversed(es)), tuple(reversed(ee)))
                    des_edge, rot = edges_mapping[edge]
                    new_dir = (curr_dir + rot) % 4
                    d1, d2 = des_edge
                    d1x, d1y = d1
                    d2x, d2y = d2
                    new_pos = np.array([
                        d1y * stride + (d2y - d1y) * n,
                        d1x * stride + (d2x - d1x) * n
                    ], dtype=np.int32)
                    new_pos += compensation[(new_dir + 3) % 4]
                    assert get(area, new_pos[1], new_pos[0]) != 0
                if area[new_pos[0], new_pos[1]] == 2:
                    break
                pos = new_pos
                # print(pos)
                curr_dir = new_dir
    pos += 1
    print(pos[0] * 1000 + pos[1] * 4 + curr_dir)
