from helper import stdin
import re
import numpy as np

pattern = "Blueprint (\\d+): Each ore robot costs (\\d+) ore. Each clay robot costs (\\d+) ore. Each obsidian robot costs (\\d+) ore and (\\d+) clay. Each geode robot costs (\\d+) ore and (\\d+) obsidian."


def solve(i, ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian):
    robots = np.array([1, 0, 0, 0], dtype=np.int32)
    resources = np.zeros((4), dtype=np.int32)
    costs = np.array([
        [ore_ore, 0, 0, 0],
        [clay_ore, 0, 0, 0],
        [obsidian_ore, obsidian_clay, 0, 0],
        [geode_ore, 0, geode_obsidian, 0]], dtype=np.int32)
    best = 0
    max_robots = np.max(costs, axis=0)
    max_robots[-1] = 32
    print(max_robots)

    def solve2(resources, time_left=32, at_least=8):
        nonlocal costs, best
        future = resources + time_left * robots
        if future[3] > best:
            print(robots)
            best = future[3]
            print(best)

        # some nasty heuristic ending calculations earlier
        if time_left < 20:
            temp_resources = resources.copy()
            temp_robots = robots.copy()
            for _ in range(time_left):
                temp_resources += temp_robots
                if temp_resources[2] >= geode_obsidian:
                    temp_robots[3] += 1
                elif temp_resources[1] >= obsidian_clay:
                    temp_robots[2] += 1
                else:
                    temp_robots[1] += 1
            if temp_resources[3] < at_least:
                return

        for i, cost in reversed(list(enumerate(costs))):
            if robots[i] < max_robots[i] and all(future >= cost):
                future_time = time_left
                temp_resources = resources - cost
                while any(temp_resources < 0):
                    future_time -= 1
                    temp_resources += robots
                future_time -= 1
                temp_resources += robots
                robots[i] += 1
                solve2(temp_resources, future_time, max(best, at_least))
                robots[i] -= 1

    solve2(resources)
    return best


if __name__ == "__main__":
    res = 1
    for i, line in list(enumerate(stdin, 1))[:3]:
        if (match := re.match(pattern, line)):
            data = map(int, match.groups())
            res *= solve(*data)
        elif line == '\n':
            pass
        else:
            print(line)
            assert False
    print(res)
