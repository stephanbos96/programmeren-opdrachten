def standaardprijs(afstandKM):
    if eval(afstandKM) <50:
        prijs = 0.80*eval(afstandKM)

    elif eval(afstandKM) >= 50:
        prijs = 15 + (eval(afstandKM)) * 0.6

    return prijs

def ritprijs(leeftijd, weekendrit, prijs):
    if weekendrit.lower() == 'ja':
        if eval(leeftijd) < 12 or eval(leeftijd) >= 65:
            rit = prijs * 0.65
        else:
            rit = prijs*0.6
    else:
        if eval(leeftijd) < 12 or eval(leeftijd) >= 65:
            rit = prijs*0.7
        else:
            rit = prijs
    return rit




afstandKM = input('vul hier het aantal kilometers in: ')
weekendrit = input('vindt u reis plaats in het weekend: ')
leeftijd = input('wat is uw leeftijd: ')
prijs = standaardprijs(afstandKM)

print('________________________________')

print(ritprijs(leeftijd, weekendrit, prijs))



