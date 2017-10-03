def pixels(tweedee):
    som = 0
    for lijst in tweedee:
        for getal in lijst:
            if getal > 0:
                som += 1
    return som

lijstlang = [[5,9,0],[12,0,0,0,0],[1]]

a = pixels(lijstlang)
print(a)


