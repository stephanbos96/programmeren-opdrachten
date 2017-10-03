text = eval(input('Geef lijst met minimaal 10 strings: '))

nieuwe_lijst =[]
for woord in text:
    if len(woord) == 4:
        nieuwe_lijst.append(woord)

print (nieuwe_lijst)
