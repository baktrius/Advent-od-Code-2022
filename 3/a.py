from sys import stdin


def priority(item):
    item = ord(item)
    if item <= ord('Z'):
        return item - ord('A') + 27
    else:
        return item - ord('a') + 1


total_sum = 0
for line in stdin:
    line = line[:-1]
    s = len(line)//2
    p1 = set(line[:s])
    p2 = set(line[s:])
    common = list(p1.intersection(p2))
    assert len(common) == 1
    total_sum += priority(common[0])
print(total_sum)
