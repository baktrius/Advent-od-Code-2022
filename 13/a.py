from helper import stdin
from json import loads


if __name__ == "__main__":
    res = 0
    for i, group in enumerate(stdin.read().split('\n\n'), 1):
        line1, line2 = group.split('\n')[:2]
        val1 = loads(line1)
        val2 = loads(line2)

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

        if rec_cmp(val1, val2) == -1:
            res += i
    print(res)
