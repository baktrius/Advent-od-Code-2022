from helper import GroupsParser
import numpy as np


if __name__ == "__main__":
    res = 0
    knots = np.zeros((10, 2), dtype=np.int32)
    dirs = {"R": np.array((-1, 0)), "L": np.array((1, 0)),
            "D": np.array((0, -1)), "U": np.array((0, 1))}
    visited = set(["0;0"])
    for group in GroupsParser("^(R|L|U|D) (\\d*)$", [str, int]):
        for cur_dir, steps in group:
            for _ in range(steps):
                knots[0] += dirs[cur_dir]
                for i in range(1, 10):
                    if np.max(np.abs(knots[i] - knots[i-1])) > 1:
                        knots[i] += np.sign(knots[i-1] - knots[i])
                visited.add(";".join(map(str, knots[9])))
    print(visited)
    print(len(visited))
