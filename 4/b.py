from sys import stdin
import re
from typing import Union


class LineParser():
    def __init__(self, inp, pattern: Union[str, re.Pattern]) -> None:
        self.inp = inp
        self.pattern = pattern

    def getLine(self):
        return re.match(self.pattern, next(self.inp)).groups()

    def __iter__(self):
        return self

    def __next__(self):
        return self.getLine()


if __name__ == "__main__":
    total_count = 0
    for line in LineParser(stdin, "^(\\d+)-(\\d+),(\\d+)-(\\d+)$"):
        s1, e1, s2, e2 = list(map(int, line))
        if e1 < s2 or e2 < s1:
            pass
        else:
            total_count += 1
    print(total_count)
