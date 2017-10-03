import csv

try:
    with open('producten.csv') as productsfile:
        reader = csv.DictReader(productsfile, delimiter=';')

        artikelnummer = ''
        kleinste_voorraad = -1
        totaal = 0
        naam = ''
        hoogsteprijs = 0
        for row in reader:
            totaal += int(row['Voorraad'])
            voorraad = int(row['Voorraad'])
            if kleinste_voorraad == -1 or voorraad < kleinste_voorraad:
                kleinste_voorraad = voorraad
                artikelnummer = row['Artikelnummer']
                prijs = float(row['Prijs'])

            if prijs > hoogsteprijs:
                hoogsteprijs = prijs
                naam = row['Naam']
        print('Het duurste artikel is de {} \nDit artikel kost euro {} '.format(naam, str(hoogsteprijs)))
        print('Er zijn slechts {} in voorraad van het product met nummer {}'.format(str(kleinste_voorraad), artikelnummer))
        print('In totaal hebben wij {} producten in ons magazijn liggen'.format(str(totaal)))

except IOError:
    print('Kan bestand niet lezen')
