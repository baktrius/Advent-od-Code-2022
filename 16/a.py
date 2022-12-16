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

    def solve(released_pressure=0, curr_valve='AA', left_valves: set = set(nonzero_valves), left_time=30):
        res = released_pressure
        times = dists[valves[curr_valve][0], :]
        for valve in list(left_valves):
            dis = times[valves[valve][0]]
            if dis < left_time:
                left_valves.remove(valve)
                open_time = left_time - dis - 1
                res = max(res, solve(
                    released_pressure + valves[valve][1] * open_time, valve, left_valves, open_time))
                left_valves.add(valve)
        return res

    print(connections)
    print(dists)
    print(solve())
