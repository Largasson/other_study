def gen_num(N, M, prefix=None):
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        gen_num(N, M - 1, prefix)
        prefix.pop()

gen_num(3, 3)
