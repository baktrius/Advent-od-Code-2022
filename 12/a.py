from helper import stdin, flatten
import numpy as np


if __name__ == "__main__":
    inp = stdin.read().split('\n')[:-1]
    h = len(inp)
    w = len(inp[0])
    inp2 = flatten(inp)

    def getPosAndReplace(ch, ch2):
        pos = inp2.index(ch)
        inp2[pos] = ch2
        return np.array([pos // w, pos % w])

    s_pos = getPosAndReplace('S', 'a')
    e_pos = getPosAndReplace('E', 'z')

    inp3 = list(map(ord, inp2))
    inp4 = np.array(inp3).reshape((h, w)) - ord('a')
    inp4[tuple(s_pos)] = -1

    print(inp4)

    res = 0
    heads = [(s_pos, 0)]
    while heads:
        res += 1
        new_heads = []
        for head, v in heads:
            for new_head in [head + [1, 0], head + [-1, 0], head + [0, 1], head + [0, -1]]:
                if new_head[0] >= 0 and new_head[0] < h and new_head[1] >= 0 and new_head[1] < w:
                    new_v = inp4[tuple(new_head)]
                    if new_v != -1 and new_v - 1 <= v:
                        if all(new_head == e_pos):
                            print(res)
                            exit(0)
                        new_heads.append((new_head, new_v))
                        inp4[tuple(new_head)] = -1
        heads = new_heads
    print(inp4)
    exit(1)
