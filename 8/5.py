# https://inf-ege.sdamgia.ru/problem?id=45242

l = list("АБРТЫ")

i = 1
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    word = f"{a}{b}{c}{d}{e}"

                    if word.count("Ы") == 0 and word.count("АА") == 0:
                        print(i)
                        exit()

                    i += 1

# 131
