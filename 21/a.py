from helper import stdin
import re
from typing import Dict

pattern1 = "^(\\w+): (\\d+)$"
pattern2 = "^(\\w+): (\\w+) (.) (\\w+)$"


class Monkey():
    def __init__(self) -> None:
        pass

    def get(self, monkeys: Dict[str, 'Monkey']):
        pass


class BasicMonkey(Monkey):
    def __init__(self, num: int) -> None:
        super().__init__()
        self.num = num

    def get(self, monkeys: Dict[str, 'Monkey']):
        return self.num


class MathMonkey(Monkey):
    def __init__(self, name: str, dep1: str, op: str, dep2: str) -> None:
        super().__init__()
        self.name = name
        self.dep1 = dep1
        self.op = op
        self.dep2 = dep2

    def get(self, monkeys: Dict[str, 'Monkey']):
        val1 = monkeys[self.dep1].get(monkeys)
        val2 = monkeys[self.dep2].get(monkeys)
        if self.op == '+':
            res = val1 + val2
        elif self.op == '-':
            res = val1 - val2
        elif self.op == '*':
            res = val1 * val2
        elif self.op == '/':
            res = val1 / val2
        monkeys[self.name] = BasicMonkey(res)
        return res


if __name__ == "__main__":
    monkeys = dict()
    for line in stdin:
        if (match := re.match(pattern1, line)):
            name, digit = match.groups()
            monkeys[name] = BasicMonkey(int(digit))
        elif (match := re.match(pattern2, line)):
            name, dep1, op, dep2 = match.groups()
            monkeys[name] = MathMonkey(name, dep1, op, dep2)
            pass
        elif line == '':
            pass
        else:
            assert False
    print(monkeys["root"].get(monkeys))
