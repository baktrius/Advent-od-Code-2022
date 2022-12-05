
current = 0
best = 0
try:
    while True:
        line = input()
        if line == "":
            current = 0
        else:
            current += int(line)
            best = max(current, best)
except EOFError:
    print(best)
