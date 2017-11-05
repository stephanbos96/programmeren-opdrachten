def tafel(cijfer):
    for c in range(1,11):
        print("{} x {} = {}".format(c,cijfer,c * cijfer))

    print("")



def tafels(hoogsteTafel):

    for t in range(1, (hoogsteTafel + 1)):
        tafel(t)


tafels(10)
