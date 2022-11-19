# https://inf-ege.sdamgia.ru/problem?id=13737

l = list("ДЕКОР")

i = 1
for a in l:
    for b in l:
        for c in l:
            for d in l:
                if a == "К":
                    print(i)
                    exit()

                i += 1

# 251
