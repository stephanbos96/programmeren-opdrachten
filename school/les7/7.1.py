som = 0
aantal = 0
while True:
    getal = int(input('Voer een getal in: '))
    if getal == 0:
        break
    else:
        som += getal
    aantal += 1
print('Er zijn {} getallen ingevoerd, de som is {}'.format(str(aantal),str(som)))

