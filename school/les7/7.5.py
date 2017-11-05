def namen():
    names = {}

    while True:
        name = input("Volgende naam:")

        if name is "":
            break

        if name in names:
            names[name]= names[name] + 1
        else:
            names[name] = 1


    for n in names:
        hulpwerkwoord = "zijn studenten"

        if names[n] == 1:
            hulpwerkwoord = "is student"

        print("Er {} {} met de naam {}".format(names[n],hulpwerkwoord,n))

namen()
