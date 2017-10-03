invoer = '5-9-7-1-7-8-3-2-4-6'

lijst = invoer.split('-')
nieuwe_lijst =[]
for text in lijst:
    nummer = int(text)
    nieuwe_lijst.append(nummer)

nieuwe_lijst.sort()


max = max(nieuwe_lijst)
min = min(nieuwe_lijst)
aantal = len(nieuwe_lijst)

som = sum(nieuwe_lijst)
gemiddelde = som // aantal

print('Gesorteerde list van ints: ', nieuwe_lijst)
print('grootste getal: ', max)
print('Kleinste getal: ', min)
print('Aantal getallen: ', aantal)
print('Som van de getallen: ', som)
print('Gemiddelde: ', gemiddelde)

