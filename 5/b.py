from helper import GroupsParser, stdin


if __name__ == "__main__":
    stacks = None
    for line in stdin:
        if line == '\n':
            break
        assert len(line) % 4 == 0
        s = len(line) // 4
        if stacks is None:
            stacks = [[] for _ in range(s)]
        for i in range(s):
            crate = line[i*4:i*4+3]
            if crate[0] == '[' and crate[2] == ']':
                stacks[i].insert(0, crate[1])
    print(stacks)

    for group in GroupsParser("^move (\\d*) from (\\d*) to (\\d*)$", [int]*3):
        for line in group:
            n, src, desc = line
            src -= 1
            desc -= 1
            stacks[desc].extend(stacks[src][-n:])
            stacks[src] = stacks[src][:-n]

    print("".join([stack[-1] for stack in stacks]))
