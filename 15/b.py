from helper import stdin
import re

pattern = "^Sensor at x=(-?\\d+), y=(-?\\d+): closest beacon is at x=(-?\\d+), y=(-?\\d+)$"

if __name__ == "__main__":
    sensors = []
    for line in stdin:
        if (match := re.match(pattern, line)):
            s_x, s_y, b_x, b_y = map(int, match.groups())
            dist = abs(s_x - b_x) + abs(s_y - b_y)
            sensors.append((s_x, s_y, dist))

    for dsc_y in range(4000000):
        ranges = []
        for s_x, s_y, dist in sensors:
            if (diff := dist - abs(dsc_y - s_y)) >= 0:
                ranges.append((s_x - diff, s_x + diff))
        ranges = sorted(ranges)
        end = 0
        for rng in ranges:
            if rng[0] <= end + 1:
                end = max(end, rng[1])
            else:
                break
        if end < 4000000:
            print(end + 1, dsc_y)
            # break
