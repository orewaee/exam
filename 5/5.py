def f(n):
    a = bin(n)[2:]
    l = [int(i) for i in list(a)]

    s = sum(l)

    b = "11" if s % 2 == 1 else "00"

    return int(f"{a}{b}", 2)


for i in range(1, 1000):
    r = f(i)

    if r > 114:
        print(r)
        exit()

# 115
