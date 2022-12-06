from helper import GroupsParser, flatten, stdin


if __name__ == "__main__":
    res = 0
    signal = stdin.read()
    for i in range(len(signal) - 3):
        pack = sorted(signal[i:i+4])
        if pack[0] == pack[1] or pack[1] == pack[2] or pack[2] == pack[3]:
            pass
        else:
            print(i+4)
            exit(0)
    print("no start")
