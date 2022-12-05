from sys import stdin


def to_int(shape, base):
    return ord(shape) - ord(base)


def score_from_shape(shape):
    return shape + 1


def play_result(opponent, you):
    result = (you - opponent + 4) % 3
    return result


def score_from_res(res):
    return res * 3


def shape_from_expected_res(opponent, res):
    return (opponent + res - 1) % 3


total_score = 0
for line in stdin:
    opponent, res = line.split()
    opponent = to_int(opponent, 'A')
    res = to_int(res, 'X')
    you = shape_from_expected_res(opponent, res)
    if play_result(opponent, you) != res:
        print(opponent, you, res, play_result(opponent, you))
        assert False
    total_score += score_from_shape(you) + score_from_res(res)
print(total_score)
