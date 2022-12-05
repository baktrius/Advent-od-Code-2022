from helper import GroupsParser, flatten, stdin


if __name__ == "__main__":
    res = 0
    for group in GroupsParser("^(\\d+)$", [int]):
        res = max(res, sum(flatten(group)))
    print(res)
