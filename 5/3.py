# https://inf-ege.sdamgia.ru/problem?id=15974

def f(n):
    a = bin(n)[2:]
    b = "10" if n % 2 == 0 else "01"

    return int(f"{a}{b}", 2)


array = []

for i in range(1, 1000):
    r = f(i)

    if r <= 102:
        array.append(r)

print(array[-1]) # 101
