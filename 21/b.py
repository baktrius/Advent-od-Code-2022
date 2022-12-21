from helper import stdin
import re
from typing import Dict

pattern1 = "^(\\w+): (\\d+)$"
pattern2 = "^(\\w+): (\\w+) (.) (\\w+)$"


class Const():
    def __init__(self, num) -> None:
        self.num = num
        pass

    def get(self):
        return self.num


class Variable():
    def __init__(self, recipe) -> None:
        self.recipe = recipe

    def get(self):
        return self.recipe


def operation(v1, op, v2):
    val1 = v1.get()
    val2 = v2.get()
    if isinstance(v1, Const) and isinstance(v2, Const):
        if op == '+':
            res = val1 + val2
        elif op == '-':
            res = val1 - val2
        elif op == '*':
            res = val1 * val2
        elif op == '/':
            res = val1 / val2
        return Const(res)
    if isinstance(v1, Const):
        if op == '+':
            res = Variable(lambda x: val2(x - val1))
        elif op == '-':
            res = Variable(lambda x: val2(val1 - x))
        elif op == '*':
            res = Variable(lambda x: val2(x / val1))
        elif op == '/':
            res = Variable(lambda x: val2(val1 / x))
        elif op == '=':
            res = Const(val2(val1))
        return res
    if isinstance(v2, Const):
        if op == '+':
            res = Variable(lambda x: val1(x - val2))
        elif op == '-':
            res = Variable(lambda x: val1(val2 + x))
        elif op == '*':
            res = Variable(lambda x: val1(x / val2))
        elif op == '/':
            res = Variable(lambda x: val1(val2 * x))
        elif op == '=':
            res = Const(val1(val2))
        return res
    assert False


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
        return Const(self.num)


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

        # monkeys[self.name] = BasicMonkey(res)
        return operation(val1, self.op, val2)

    def setOp(self, op):
        self.op = op


class Human(Monkey):
    def __init__(self) -> None:
        super().__init__()

    def get(self, monkeys: Dict[str, 'Monkey']):
        return Variable(lambda x: x)


if __name__ == "__main__":
    monkeys = dict()
    for line in stdin:
        if (match := re.match(pattern1, line)):
            name, digit = match.groups()
            monkeys[name] = BasicMonkey(int(digit))
        elif (match := re.match(pattern2, line)):
            name, dep1, op, dep2 = match.groups()
            monkeys[name] = MathMonkey(name, dep1, op, dep2)
        elif line == '':
            pass
        else:
            assert False
    monkeys["humn"] = Human()
    monkeys["root"].setOp("=")
    print(monkeys["root"].get(monkeys).get())
