prijs = 4356

def kosten(prijs):
    try:
        personen = eval(input('Hoeveel personen gaan er mee op reis: '))
        kosten_pp = prijs/int(personen)
        if personen <0:
            print('Negatieve getallen zijn niet toegestaan')
        else:
            print('Er gaan {} personen mee\nHet bedrag per persoon is {}'.format(personen, kosten_pp))
    except ZeroDivisionError:
        print('Delen door 0 kan niet')
    except NameError:
        print('Gebruik cijfers in plaats van getallen')
    except:
        print('Error')

kosten(prijs)



