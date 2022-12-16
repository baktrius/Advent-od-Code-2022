from helper import stdin
import numpy as np
import re

pattern = "^Valve (..) has flow rate=(\\d+); tunnels? leads? to valves? ((?:.., )*..)$"

if __name__ == "__main__":
    valves = {}
    nonzero_valves = []
    i = 0
    for line in stdin:
        if (match := re.match(pattern, line)):
            name, flow, neighbors = match.groups()
            valves[name] = (i, int(flow), neighbors.split(', '))
            i += 1
            if flow != '0':
                nonzero_valves.append(name)

    connections = np.zeros((len(valves), len(valves)), dtype=np.int32)
    for valve in valves.values():
        i, _, neighbors = valve
        for neighbor in neighbors:
            connections[i, valves[neighbor][0]] = 1

    dists = connections.copy()
    temp = connections.copy()
    for i in range(2, 31):
        temp = ((temp @ connections) >= 1).astype(np.int32)
        dists[dists == 0] = temp[dists == 0] * i

    max_scores = np.zeros((1 << len(nonzero_valves)), dtype=np.int32)

    def solve(released_pressure=0, curr_valve='AA', left_valves: set = set(nonzero_valves), left_time=26, used_valves=0):
        res = released_pressure
        times = dists[valves[curr_valve][0], :]
        for valve in list(left_valves):
            dis = times[valves[valve][0]]
            if dis < left_time:
                left_valves.remove(valve)
                valve_num = 1 << nonzero_valves.index(valve)
                open_time = left_time - dis - 1
                res = max(res, solve(
                    released_pressure + valves[valve][1] * open_time, valve, left_valves, open_time, used_valves + valve_num))
                left_valves.add(valve)
        max_scores[used_valves] = max(
            released_pressure, max_scores[used_valves])
        return res

    solve()
    max_scores2 = sorted(enumerate(max_scores),
                         key=lambda x: x[1], reverse=True)
    res = max1Score = max_scores2[0][1]
    min1Score = max1Score // 2
    min2Score = 0
    for i1, score1 in max_scores2:
        if score1 < min1Score:
            break
        for i2, score2 in max_scores2:
            if score2 < min2Score:
                break
            if i1 & i2 == 0:
                new = score1 + score2
                if new > res:
                    res = new
                    min1Score = new / 2
                    min2Score = new - max1Score
                    print(i1, score1, i2, score2)
                break
    print(res)
