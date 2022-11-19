# https://inf-ege.sdamgia.ru/problem?id=11262

def f(n):
    l = [int(i) for i in list(str(n))]

    a = l[0] + l[1]
    b = l[1] + l[2]
    c = l[2] + l[3]

    array = [a, b, c]
    array.sort(reverse=True)

    return int(f"{array[1]}{array[0]}")


for i in range(1000, 9999):
    if f(i) == 1517:
        print(i)
        exit()

# 1698
