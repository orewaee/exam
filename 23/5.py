# https://inf-ege.sdamgia.ru/problem?id=17386

def f(a, b):
    if a > b or a == 11:
        return 0
    elif a == b:
        return 1
    else:
        return f(a + 1, b) + f(a * 2, b) + f(a + 5, b)


print(f(1, 9) * f(9, 18)) # 57
