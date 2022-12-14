from helper import stdin
import numpy as np

if __name__ == "__main__":
    lines = stdin.read().split('\n')[:-1]
    min_x, max_x, min_y, max_y = 500, 500, 0, 0
    for line in lines:
        for point in line.split(' -> '):
            x, y = map(int, point.split(','))
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
    print(min_x, max_x, min_y, max_y)

    space = np.zeros((max_y - min_y + 3, max_x - min_x + 3), dtype=np.int32)

    def get_space(x, y):
        return space[y - min_y + 1, x - min_x + 1]

    def set_space(x, y, v):
        space[y - min_y + 1, x - min_x + 1] = v

    for line in lines:
        points = line.split(' -> ')
        x, y = map(int, points[0].split(','))
        for point in points[1:]:
            x2, y2 = map(int, point.split(','))
            dis = abs(x - x2 + y - y2)
            for i in range(dis + 1):
                mx, my = x + (x2 - x) * i // dis, y + (y2 - y) * i // dis
                set_space(mx, my, 1)
            x, y = x2, y2

    def printSpace():
        for line in space:
            print("".join(map(lambda v: ['.', '#', 'O'][v], line)))

    printSpace()

    for i in range(1000000):
        s_x, s_y = 500, 0
        inf_fall = True
        if get_space(s_x, s_y):
            printSpace()
            assert False
        while s_x >= min_x and s_x <= max_x and s_y >= min_y and s_y <= max_x:
            if not get_space(s_x, s_y + 1):
                s_y += 1
            elif not get_space(s_x - 1, s_y + 1):
                s_y += 1
                s_x -= 1
            elif not get_space(s_x + 1, s_y + 1):
                s_y += 1
                s_x += 1
            else:
                set_space(s_x, s_y, 2)
                inf_fall = False
                break
        if inf_fall:
            print(i)
            printSpace()
            break
