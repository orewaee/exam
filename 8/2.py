# https://inf-ege.sdamgia.ru/problem?id=29195

l = list("РЕГИНА")

array = []
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    word = f"{a}{b}{c}{d}{e}"

                    terms = [
                        word.count("Р") == 1,
                        word.count("Г") == 1,
                        word.count("Н") == 1 or word.count("Н") == 0
                    ]

                    if all(terms):
                        array.append(word)

print(len(array)) # 1080
