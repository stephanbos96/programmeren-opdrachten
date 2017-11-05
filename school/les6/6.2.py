def fourLetter(lst):
    if len(lst) < 10:
        return "De lijst moet minimaal 10 objecten bevatten"

    fourLetterList = []

    for i in lst:
        if len(i) == 4:
            fourLetterList.append(i)

    return "De nieuw-gemaakte lijst met alle vier-letter strings is:" + str(fourLetterList)

lst = eval(input("Geef lijst met minimaal 10 strings: "))

print(fourLetter(lst))
