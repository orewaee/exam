# https://inf-ege.sdamgia.ru/problem?id=13418

def f(a, b):
    if a > b or a == 26:
        return 0
    elif a == b:
        return 1
    else:
        return f(a + 1, b) + f(a * 2 + 1, b)


print(f(1, 27)) # 13
    