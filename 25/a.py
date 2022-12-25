from helper import stdin


if __name__ == "__main__":
    res = 0
    for line in stdin:
        if line == '':
            break
        val = 0
        for char in line[:-1]:
            val = val * 5 + "=-012".index(char) - 2
        print(val)
        res += val

    carry = 0
    num = []
    while res:
        rem = res % 5 + carry
        num.append("012=-012"[rem])
        carry = 1 if rem >= 3 else 0
        res //= 5
    print("".join(reversed(num)))
