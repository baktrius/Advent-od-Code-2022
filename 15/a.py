from helper import stdin
import re

pattern = "^Sensor at x=(-?\\d+), y=(-?\\d+): closest beacon is at x=(-?\\d+), y=(-?\\d+)$"

if __name__ == "__main__":
    dsc_y = 2000000
    ranges = []
    bad_beacons = set()
    for line in stdin:
        if (match := re.match(pattern, line)):
            s_x, s_y, b_x, b_y = map(int, match.groups())
            dist = abs(s_x - b_x) + abs(s_y - b_y)
            if (diff := dist - abs(dsc_y - s_y)) >= 0:
                ranges.append((s_x - diff, s_x + diff))
            if (b_y == dsc_y):
                bad_beacons.add(b_x)
    ranges = sorted(ranges)
    res = 0
    i = 0
    while i < len(ranges):
        start, end = ranges[i]
        i += 1
        while i < len(ranges) and ranges[i][0] <= end:
            end = max(end, ranges[i][1])
            i += 1
        res += end - start + 1
    print(ranges)
    for beacon in bad_beacons:
        for rng in ranges:
            if rng[0] <= beacon and rng[1] >= beacon:
                res -= 1
                break
    print(res)
