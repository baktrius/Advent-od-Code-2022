current = 0
bests = []


def add_best(value):
    global bests
    bests.append(value)
    bests = sorted(bests, reverse=True)[:3]


try:
    while True:
        line = input()
        if line == "":
            add_best(current)
            current = 0
        else:
            current += int(line)
except EOFError:
    if current != 0:
        add_best(current)
    print(sum(bests))
