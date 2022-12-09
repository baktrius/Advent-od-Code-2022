from helper import GroupsParser
import numpy as np


if __name__ == "__main__":
    res = 0
    hpos = np.array((0, 0))
    tpos = np.array((0, 0))
    dirs = {"R": np.array((-1, 0)), "L": np.array((1, 0)),
            "D": np.array((0, -1)), "U": np.array((0, 1))}
    visited = set(["0;0"])
    for group in GroupsParser("^(R|L|U|D) (\\d*)$", [str, int]):
        for cur_dir, steps in group:
            for _ in range(steps):
                hpos += dirs[cur_dir]
                if np.max(np.abs(hpos - tpos)) > 1:
                    tpos += np.sign(hpos - tpos)
                    visited.add(";".join(map(str, tpos)))
    print(len(visited))
