# https://inf-ege.sdamgia.ru/problem?id=3195

l = list("АКРУ")

i = 1
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    if i == 350:
                        print(f"{a}{b}{c}{d}{e}")
                        exit()
                    
                    i += 1

# КККУК
