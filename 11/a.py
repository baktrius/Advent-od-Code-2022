from helper import stdin, re

pattern = ("Monkey (\\d):\\s+Starting items: ((?:\\d+, )*\\d+)\\s+Operation: new = (\\w+) ([+*]) (\\w+)\\s+" +
           "Test: divisible by (\\d+)\\s+If true: throw to monkey (\\d+)\\s+If false: throw to monkey (\\d+)\\s+")


class Monkey:
    def __init__(self, items: list[int], div, v1, op, v2, m1, m2) -> None:
        self.items = items
        self.div = div
        self.v1 = v1
        self.op = op
        self.v2 = v2
        self.m1 = m1
        self.m2 = m2
        self.inspections = 0

    def round(self, monkeys: list["Monkey"]):
        while self.items:
            self.inspect(monkeys)

    def inspect(self, monkeys: list["Monkey"]):
        self.inspections += 1
        item = self.items.pop(0)
        i1 = item if self.v1 == "old" else int(self.v1)
        i2 = item if self.v2 == "old" else int(self.v2)
        if self.op == "*":
            item = i1 * i2
        elif self.op == "+":
            item = i1 + i2
        else:
            assert False
        item //= 3
        if item % self.div == 0:
            monkeys[self.m1].append(item)
        else:
            monkeys[self.m2].append(item)

    def append(self, item):
        self.items.append(item)

    def describe(self):
        print(", ".join(map(str, self.items)))


if __name__ == "__main__":
    inp = stdin.read()
    monkeys = []
    for i, monkey_description in enumerate(re.finditer(pattern, inp)):
        id, items, v1, op, v2, div, m1, m2 = monkey_description.groups()
        assert i == int(id)
        items = list(map(int, re.split(", ", items)))
        div = int(div)
        m1 = int(m1)
        m2 = int(m2)
        monkeys.append(Monkey(items, div, v1, op, v2, m1, m2))
    for r in range(20):
        for monkey in monkeys:
            monkey.round(monkeys)
        print(f"after round {r+1}:")
        for monkey in monkeys:
            monkey.describe()
    for monkey in monkeys:
        print(monkey.inspections)
