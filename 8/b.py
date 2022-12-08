from helper import GroupsParser
import numpy as np


if __name__ == "__main__":
    res = 0
    for group in GroupsParser("^(\\d*)$", [str]):
        inp = np.array([[int(letter) for letter in line[0]] for line in group])
        h, w = inp.shape
        for x in range(w):
            for y in range(h):
                tree = inp[y, x]
                for x1 in range(x, w):
                    if inp[y, x1] >= tree and x1 != x:
                        break
                for y1 in range(y, h):
                    if inp[y1, x] >= tree and y1 != y:
                        break
                for x2 in range(x, -1, -1):
                    if inp[y, x2] >= tree and x2 != x:
                        break
                for y2 in range(y, -1, -1):
                    if inp[y2, x] >= tree and y2 != y:
                        break
                res = max(res, (x1 - x) * (x - x2) * (y1 - y) * (y - y2))
    print(res)
