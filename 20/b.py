from helper import stdin

decryption_key = 811589153

if __name__ == "__main__":
    inp = list(
        enumerate([int(line) * decryption_key for line in stdin if line != '']))
    inp_len = len(inp)
    # print(list(map(lambda x: x[1], inp)))
    p = 0
    for _ in range(10):
        for i in range(inp_len):
            while inp[p][0] != i:
                p = (p + 1) % inp_len
            curr = inp.pop(p)
            inp.insert((p + curr[1] % (inp_len - 1) +
                        inp_len - 1) % (inp_len - 1), curr)
            p = (p + inp_len - 1) % inp_len
            # print(list(map(lambda x: x[1], inp)))
    vals = list(map(lambda x: x[1], inp))
    zero_index = vals.index(0)
    print(vals[(zero_index + 1000) % inp_len] + vals[(zero_index + 2000) %
          inp_len] + vals[(zero_index + 3000) % inp_len])
