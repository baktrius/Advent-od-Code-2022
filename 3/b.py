from sys import stdin


def priority(item):
    item = ord(item)
    if item <= ord('Z'):
        return item - ord('A') + 27
    else:
        return item - ord('a') + 1


total_sum = 0
for l1 in stdin:
    l1 = set(l1[:-1])
    l2 = set(next(stdin)[:-1])
    l3 = set(next(stdin)[:-1])
    common = list(l1.intersection(l2.intersection(l3)))
    assert len(common) == 1
    print(common[0])
    total_sum += priority(common[0])
print(total_sum)
