from helper import GroupsParser, flatten, stdin

size = 14
if __name__ == "__main__":
    res = 0
    signal = stdin.read()
    for i in range(len(signal) - size + 1):
        pack = sorted(signal[i:i+size])
        if any([a == b for a, b in zip(pack[1:], pack[:-1])]):
            pass
        else:
            print(i+size)
            exit(0)
    print("no start")
