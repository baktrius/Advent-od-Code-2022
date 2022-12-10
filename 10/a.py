from helper import GroupsParser, flatten, stdin, re


if __name__ == "__main__":
    res = 0
    x_val = 1
    cycle = 1

    def inc_cycle():
        global cycle, res
        cycle += 1
        if cycle % 40 == 20 and cycle <= 220:
            res += x_val * cycle

    for line in stdin.read().split('\n'):
        if line == 'noop':
            inc_cycle()
        elif (match := re.match("^addx (-?\\d*)$", line)) is not None:
            val_inc = int(match.group(1))
            inc_cycle()
            x_val += val_inc
            inc_cycle()
        else:
            print("skipped:", line)

    print(res)
