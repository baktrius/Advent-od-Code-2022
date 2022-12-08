from helper import GroupsParser
import numpy as np


if __name__ == "__main__":
    res = 0
    for group in GroupsParser("^(\\d*)$", [str]):
        inp = np.array([[int(letter) for letter in line[0]] for line in group])
        vis = np.zeros_like(inp)
        h, w = inp.shape
        for x in range(w):
            tree = -1
            for y in range(h):
                if inp[y, x] > tree:
                    vis[y, x] = 1
                    tree = inp[y, x]
        for x in range(w):
            tree = -1
            for y in range(h-1, -1, -1):
                if inp[y, x] > tree:
                    vis[y, x] = 1
                    tree = inp[y, x]

        for y in range(h):
            tree = -1
            for x in range(w):
                if inp[y, x] > tree:
                    vis[y, x] = 1
                    tree = inp[y, x]
        for y in range(h):
            tree = -1
            for x in range(w-1, -1, -1):
                if inp[y, x] > tree:
                    vis[y, x] = 1
                    tree = inp[y, x]
        print(np.count_nonzero(vis))
    print(res)
