# https://inf-ege.sdamgia.ru/problem?id=11123

def f(a, b):
    if a < b:
        return 0
    elif a == b:
        return 1
    else:
        return f(a - 2, b) + f(a - 5, b)


print(f(22, 2)) # 23
