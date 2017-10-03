import datetime
import csv

bestand = 'inloggers.csv'

while True:
    naam = input('Wat is je achternaam: ')
    if naam == 'einde':
        break

    voorl = input('Wat zijn je voorletters: ')
    gbdatum = input('Wat is je geboortedatum: ')
    email = input('Wat is je E-mail adres: ')
    formatted_time = datetime.datetime.now().strftime('%a %d %B %y at %I:%M')

    try:
        outfile = open(bestand, 'a', newline='')
        writer = csv.writer(outfile, delimiter=';')
        writer.writerow((formatted_time, naam, voorl, gbdatum, email))
        outfile.close()
    except IOError:
        print('I/O Error')
    finally:
        outfile.close()
