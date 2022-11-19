# https://inf-ege.sdamgia.ru/problem?id=33750

def f(n):
    bin_n = bin(n)[2:]
    l = list(bin_n)

    l[-1] = l[1] * 2

    return int("".join(l), 2)


for i in range(2, 1000):
    if f(i) > 76:
        print(i)
        exit()

# 40
