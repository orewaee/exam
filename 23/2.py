# https://inf-ege.sdamgia.ru/problem?id=18503

def f(a, b):
    if a > b or a == 13:
        return 0
    elif a == b:
        return 1
    else:
        return f(a + 1, b) + f(a + 2, b) + f(a * 3, b)


print(f(1, 10) * f(10, 15)) # 168
