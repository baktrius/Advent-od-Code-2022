from helper import GroupsParser, flatten, stdin, re


if __name__ == "__main__":
    x_val = 1
    cycle = 1

    def inc_cycle():
        global cycle
        if abs((cycle - 1) % 40 - x_val) <= 1:
            print("#", end="")
        else:
            print(".", end="")
        if cycle % 40 == 0:
            print()
        cycle += 1

    for line in stdin.read().split('\n'):
        if line == 'noop':
            inc_cycle()
        elif (match := re.match("^addx (-?\\d*)$", line)) is not None:
            val_inc = int(match.group(1))
            inc_cycle()
            inc_cycle()
            x_val += val_inc
        else:
            print("skipped:", line)
