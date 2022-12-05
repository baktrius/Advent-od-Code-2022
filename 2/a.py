from sys import stdin


def shape_to_int(shape, base):
    return ord(shape) - ord(base)


def score_from_shape(shape):
    return shape + 1


def score_from_res(opponent, you):
    result = (you - opponent + 3) % 3
    return [3, 6, 0][result]


total_score = 0
for line in stdin:
    opponent, you = line.split()
    opponent = shape_to_int(opponent, 'A')
    you = shape_to_int(you, 'X')
    total_score += score_from_shape(you) + score_from_res(opponent, you)
print(total_score)
