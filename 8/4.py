# https://inf-ege.sdamgia.ru/problem?id=10473

l = [1, 2, 3, 4]

array = []
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    p = f"{a}{b}{c}{d}{e}"

                    if p.count("1") == 2:
                        array.append(p)

print(len(array)) # 270
