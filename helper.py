from sys import stdin
import re
from typing import Union


class GroupsParser():
    def __init__(self, pattern: Union[str, re.Pattern], maps: list, inp=stdin) -> None:
        self.inp = inp
        self.pattern = pattern
        self.maps = maps
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        group = []
        try:
            while (line := next(self.inp)) != '\n':
                group.append([f(v) for f, v in zip(
                    self.maps, re.match(self.pattern, line).groups())])
                self.num += 1
        except StopIteration:
            if len(group) == 0:
                raise
        except AttributeError:
            print(self.num, line)
            raise
        return group


def flatten(l):
    return [item for sublist in l for item in sublist]
