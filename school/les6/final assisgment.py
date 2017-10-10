def toon_aantal_kluizen_vrij():
    file = open('kluizen.txt')
    regels = file.readlines()
    file.close()
    aantal = 12 - len(regels)
    print('{} zijn er vrij'.format(str(aantal)))

def nieuwe_kluis():
    beschikbarekluizen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    bestand = open('kluizen.txt')
    regels = bestand.readlines()
    bestand.close()

    for regel in regels:
        kluisinfo = regel.split(';')
        kluisnummer = int(kluisinfo[0].strip())

        if kluisnummer in beschikbarekluizen:
            beschikbarekluizen.remove(kluisnummer)

    if len(beschikbarekluizen) > 0:
        kluiscode = input('Voer de kluiscode in voor uw nieuwe kluis: ')
        if len(kluiscode) <4:
            print('Minimaal 4 tekens')
            return
        print('u lrijgt kluis met nummer {} en code {}'.format(beschikbarekluizen[0], kluiscode))

        bestand = open('kluizen.txt', 'a')
        bestand.write('{};{}\n'.format(beschikbarekluizen[0],kluiscode))
        bestand.close()
    else:
        print('Er is helaas geen kluis meer vrij!')

def kluis_openen():
    kluis_bewerken('openen')

def kluis_bewerken(actie):
    kluiscode = input('Kluiscode?: ')
    kluisnummer = eval(input('Kluisnummer?: '))

    file = open('kluizen.txt')
    regels = file.readlines()
    file.close()

    gevonden = False
    for regel in regels:
        lijst = regel.split(';')
        kn = int(lijst[0].strip())
        kc = lijst[1].strip()
        if kn == kluisnummer and kc == kluiscode:
            print('Kluisnummer {} gaan we {}'.format(str(kluisnummer), actie))
            gevonden = True
            if actie == 'teruggeven':
                regels.remove(regel)
                file = open('kluizen.txt', 'w')
                for nieuwe_regel in regels:
                    file.write(nieuwe_regel)
                file.close()

    if not gevonden:
        print('kluisnummer {} niet juist'. format(str(kluisnummer)))


def kluis_teruggeven():
    kluis_bewerken('teruggeven')


while True:
    print('1: ik wil weten hoeveel kluizen nog vrij zijn')
    print('2: ik wil een nieuwe kluis')
    print('3: Ik wil even iets uit me kluis halen')
    print('4: ik geef mijn kluis terug')
    print('5: Ik wil stoppen')

    keuze = eval(input('Maak uw keuze: '))
    if keuze == 1:
        toon_aantal_kluizen_vrij()

    elif keuze == 2:
        nieuwe_kluis()

    elif keuze == 3:
        kluis_openen()

    elif keuze == 4:
        kluis_teruggeven()

    elif keuze == 5:
        break
