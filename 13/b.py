from helper import stdin
from json import loads


if __name__ == "__main__":
    def cmp(v1: int, v2: int):
        return int(v2 < v1) - int(v1 < v2)

    def rec_cmp(v1, v2):
        if isinstance(v1, int) and isinstance(v2, int):
            return cmp(v1, v2)
        elif isinstance(v1, list) and isinstance(v2, list):
            for vv1, vv2 in zip(v1, v2):
                if (res := rec_cmp(vv1, vv2)):
                    return res
            return cmp(len(v1), len(v2))
        elif isinstance(v1, int) and isinstance(v2, list):
            return rec_cmp([v1], v2)
        elif isinstance(v1, list) and isinstance(v2, int):
            return rec_cmp(v1, [v2])
        else:
            assert False

    pos1, pos2 = 1, 2

    for group in stdin.read().split('\n\n'):
        for line in map(loads, group.split('\n')[:2]):
            pos1 += int(rec_cmp(line, [[2]]) == -1)
            pos2 += int(rec_cmp(line, [[6]]) == -1)
    print(pos1 * pos2)
